from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from src.multimodal_engine import MultimodalEngine
from src.neural_router import InferenceRequest, Modality

BASE_DIR = Path(__file__).resolve().parent.parent
WEB_INDEX = BASE_DIR / "web" / "index.html"

app = FastAPI(title="Six Neural Core App Gateway", version="0.2.0")
engine = MultimodalEngine()


class AskPayload(BaseModel):
    prompt: str
    modality: Modality = Modality.TEXT
    attachments: List[Dict[str, Any]] = Field(default_factory=list)
    sensor_telemetry: Optional[Dict[str, float]] = None
    low_latency_required: bool = False


@app.get("/")
async def serve_ui() -> FileResponse:
    return FileResponse(WEB_INDEX)


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "online", "device": engine.device}


@app.post("/ask")
async def ask_six(payload: AskPayload) -> Dict[str, Any]:
    req = InferenceRequest(
        prompt=payload.prompt,
        modality=payload.modality,
        attachments=payload.attachments,
        sensor_telemetry=payload.sensor_telemetry,
        low_latency_required=payload.low_latency_required,
    )
    return await engine.infer(req)


@app.websocket("/ws/core")
async def neural_core_ws(ws: WebSocket) -> None:
    await ws.accept()
    await ws.send_json({"ui_state": "Idle"})
    try:
        while True:
            data = await ws.receive_json()
            await ws.send_json({"ui_state": "Listening"})

            req = InferenceRequest(
                prompt=data.get("prompt", ""),
                modality=Modality(data.get("modality", "text")),
                attachments=data.get("attachments", []),
                sensor_telemetry=data.get("sensor_telemetry"),
                low_latency_required=bool(data.get("low_latency_required", False)),
            )

            await ws.send_json({"ui_state": "Thinking"})
            result = await engine.infer(req)

            await ws.send_json({"ui_state": "Responding", "payload": result})
            await ws.send_json({"ui_state": "Idle"})
    except WebSocketDisconnect:
        pass
