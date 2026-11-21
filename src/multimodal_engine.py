from __future__ import annotations

import os
from typing import Any, Dict, Optional

import httpx
import torch

from src.core_adapters import SixCoreAdapters
from src.neural_router import InferenceRequest, NeuralRouter, RouteTarget


class MultimodalEngine:
    def __init__(
        self,
        router: Optional[NeuralRouter] = None,
        adapters: Optional[SixCoreAdapters] = None,
        local_endpoint: str = os.getenv("SIX_LOCAL_MODEL_URL", "http://localhost:11434/v1/chat/completions"),
        cloud_endpoint: str = os.getenv("SIX_CLOUD_MODEL_URL", "https://api.openai.com/v1/chat/completions"),
        cloud_api_key: str = os.getenv("SIX_CLOUD_API_KEY", ""),
        local_model: str = os.getenv("SIX_LOCAL_MODEL", "llama3.2-vision"),
        cloud_model: str = os.getenv("SIX_CLOUD_MODEL", "gpt-4o"),
    ) -> None:
        self.adapters = adapters or SixCoreAdapters()
        self.router = router or NeuralRouter(safety_guard=self.adapters)
        self.local_endpoint = local_endpoint
        self.cloud_endpoint = cloud_endpoint
        self.cloud_api_key = cloud_api_key
        self.local_model = local_model
        self.cloud_model = cloud_model
        self.device = self._detect_device()

    @staticmethod
    def _detect_device() -> str:
        if torch.cuda.is_available():
            return "cuda"
        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    async def infer(self, req: InferenceRequest) -> Dict[str, Any]:
        decision = self.router.route(req)

        if decision.target == RouteTarget.SAFETY_BLOCKED:
            return {
                "status": "blocked",
                "route": decision.target.value,
                "reason": decision.reason,
                "response": f"Blocked: {decision.reason}",
            }

        if decision.target == RouteTarget.NEUROMORPHIC_FAST:
            raw_output = self._run_neuromorphic_mesh(req)
            bridged = self._apply_agi_bridge(raw_output, req)
            return {
                "status": "ok",
                "route": decision.target.value,
                "device": self.device,
                "reason": decision.reason,
                "response": bridged,
            }

        if decision.target == RouteTarget.LOCAL_SLM:
            text = await self._call_openai_compatible(
                url=self.local_endpoint,
                model=self.local_model,
                api_key="local",
                req=req,
            )
            bridged = self._apply_agi_bridge(text, req)
            return {
                "status": "ok",
                "route": decision.target.value,
                "model": self.local_model,
                "reason": decision.reason,
                "response": bridged,
            }

        text = await self._call_openai_compatible(
            url=self.cloud_endpoint,
            model=self.cloud_model,
            api_key=self.cloud_api_key,
            req=req,
        )
        bridged = self._apply_agi_bridge(text, req)
        return {
            "status": "ok",
            "route": decision.target.value,
            "model": self.cloud_model,
            "reason": decision.reason,
            "response": bridged,
        }

    def _run_neuromorphic_mesh(self, req: InferenceRequest) -> str:
        values = list((req.sensor_telemetry or {"signal": float(len(req.prompt))}).values())
        tensor = torch.tensor(values, dtype=torch.float32, device=self.device)
        activated = torch.tanh(tensor)

        mesh = self.adapters.error_mesh
        if mesh is not None:
            for fn_name in ("reduce_error", "stabilize", "forward", "step"):
                fn = getattr(mesh, fn_name, None)
                if callable(fn):
                    try:
                        activated = fn(activated)
                        break
                    except Exception:
                        continue

        as_list = activated.detach().cpu().tolist() if isinstance(activated, torch.Tensor) else activated
        return f"Neuromorphic Core [{self.device}] state vector: {as_list}"

    def _apply_agi_bridge(self, response_text: str, req: InferenceRequest) -> str:
        bridge = self.adapters.agi_bridge
        if bridge is None:
            return response_text
        for fn_name in ("bridge", "transform", "integrate", "process"):
            fn = getattr(bridge, fn_name, None)
            if callable(fn):
                try:
                    out = fn(response_text, {"modality": req.modality.value, "prompt": req.prompt})
                    if isinstance(out, str) and out.strip():
                        return out
                except Exception:
                    continue
        return response_text

    async def _call_openai_compatible(
        self,
        url: str,
        model: str,
        api_key: str,
        req: InferenceRequest,
    ) -> str:
        content: list[dict[str, Any]] = [{"type": "text", "text": req.prompt}]
        for item in req.attachments:
            if "image_url" in item:
                content.append({"type": "image_url", "image_url": {"url": item["image_url"]}})

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are Six, a multi-modal neural intelligence core with neuromorphic routing and safety auditing.",
                },
                {"role": "user", "content": content if len(content) > 1 else req.prompt},
            ],
        }
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

        async with httpx.AsyncClient(timeout=45.0) as client:
            resp = await client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
