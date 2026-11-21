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

app = FastAPI(title="Six Neural Core App Gateway", version="0.2.1")
engine = MultimodalEngine()


class AskPayload(BaseModel):
    prompt: str
    modality: Modality = Modality.TEXT
    attachments: List[Dict[str, Any]] = Field(default_factory=list)
    sensor_telemetry: Optional[Dict[str, float]] = None
    low_latency_required: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


@app.get("/")
async def serve_ui() -> FileResponse:
    return FileResponse(WEB_INDEX)


@app.get("/health")
async def health() -> Dict[str, Any]:
    return {
        "status": "online",
        "device": engine.device,
        "loaded_modules": engine.adapters.loaded_modules,
    }


@app.post("/ask")
async def ask_six(payload: AskPayload) -> Dict[str, Any]:
    engine.adapters.sync_ui_state("Thinking")
    req = InferenceRequest(
        prompt=payload.prompt,
        modality=payload.modality,
        attachments=payload.attachments,
        sensor_telemetry=payload.sensor_telemetry,
        low_latency_required=payload.low_latency_required,
        metadata=payload.metadata,
    )
    result = await engine.infer(req)
    engine.adapters.sync_ui_state("Idle")
    return result


@app.websocket("/ws/core")
async def neural_core_ws(ws: WebSocket) -> None:
    await ws.accept()
    engine.adapters.sync_ui_state("Idle")
    await ws.send_json({"ui_state": "Idle"})
    try:
        while True:
            data = await ws.receive_json()
            engine.adapters.sync_ui_state("Listening")
            await ws.send_json({"ui_state": "Listening"})

            req = InferenceRequest(
                prompt=data.get("prompt", ""),
                modality=Modality(data.get("modality", "text")),
                attachments=data.get("attachments", []),
                sensor_telemetry=data.get("sensor_telemetry"),
                low_latency_required=bool(data.get("low_latency_required", False)),
                metadata=data.get("metadata", {}),
            )

            engine.adapters.sync_ui_state("Thinking")
            await ws.send_json({"ui_state": "Thinking"})
            result = await engine.infer(req)

            engine.adapters.sync_ui_state("Responding")
            await ws.send_json({"ui_state": "Responding", "payload": result})

            engine.adapters.sync_ui_state("Idle")
            await ws.send_json({"ui_state": "Idle"})
    except WebSocketDisconnect:
        engine.adapters.sync_ui_state("Idle")
