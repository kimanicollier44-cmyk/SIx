from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class Modality(str, Enum):
    TEXT = "text"
    VISION = "vision"
    AUDIO = "audio"
    SENSOR = "sensor"
    MULTIMODAL = "multimodal"


class RouteTarget(str, Enum):
    NEUROMORPHIC_FAST = "neuromorphic_fast"
    LOCAL_SLM = "local_slm"
    FRONTIER_REASONING = "frontier_reasoning"
    SAFETY_BLOCKED = "safety_blocked"


@dataclass
class InferenceRequest:
    prompt: str
    modality: Modality = Modality.TEXT
    attachments: List[Dict[str, Any]] = field(default_factory=list)
    sensor_telemetry: Optional[Dict[str, float]] = None
    low_latency_required: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RouteDecision:
    target: RouteTarget
    reason: str
    estimated_vram_mb: int
    requires_safety_audit: bool = True
    timestamp: float = field(default_factory=time.time)


class NeuralRouter:
    def __init__(self, safety_guard: Optional[Any] = None, audit_logger: Optional[Any] = None) -> None:
        self.safety_guard = safety_guard
        self.audit_logger = audit_logger

    def classify_modality(self, req: InferenceRequest) -> Modality:
        if req.sensor_telemetry and (req.prompt or req.attachments):
            return Modality.MULTIMODAL
        if req.sensor_telemetry:
            return Modality.SENSOR
        if len(req.attachments) > 1:
            return Modality.MULTIMODAL
        if len(req.attachments) == 1:
            mime = str(req.attachments[0].get("mime_type", ""))
            if mime.startswith("image/") or mime.startswith("video/"):
                return Modality.VISION
            if mime.startswith("audio/"):
                return Modality.AUDIO
        return req.modality

    def _check_guard(self, req: InferenceRequest) -> tuple[bool, str]:
        if self.safety_guard is None:
            return True, "OK"
        if hasattr(self.safety_guard, "inspect_prompt"):
            return self.safety_guard.inspect_prompt(req.prompt, req.metadata)
        if hasattr(self.safety_guard, "inspect"):
            return self.safety_guard.inspect(req.prompt, req.metadata)
        return True, "OK"

    def route(self, req: InferenceRequest) -> RouteDecision:
        effective_modality = self.classify_modality(req)

        allowed, reason = self._check_guard(req)
        if not allowed:
            decision = RouteDecision(
                target=RouteTarget.SAFETY_BLOCKED,
                reason=f"Blocked by Safety Layer: {reason}",
                estimated_vram_mb=0,
            )
            self._log(req, decision)
            return decision

        if effective_modality == Modality.SENSOR or req.low_latency_required:
            decision = RouteDecision(
                target=RouteTarget.NEUROMORPHIC_FAST,
                reason="Low-latency / telemetry payload routed to PyTorch neuromorphic mesh",
                estimated_vram_mb=256,
            )
            self._log(req, decision)
            return decision

        complex_keywords = ("architect", "prove", "debug", "analyze", "synthesize", "code", "multi-step")
        is_complex = (
            effective_modality in (Modality.VISION, Modality.AUDIO, Modality.MULTIMODAL)
            or len(req.prompt) > 280
            or any(k in req.prompt.lower() for k in complex_keywords)
        )

        if is_complex:
            decision = RouteDecision(
                target=RouteTarget.FRONTIER_REASONING,
                reason=f"Complex {effective_modality.value} query routed to multimodal reasoning engine",
                estimated_vram_mb=0,
            )
        else:
            decision = RouteDecision(
                target=RouteTarget.LOCAL_SLM,
                reason="Standard conversational query routed to local SLM / bridge",
                estimated_vram_mb=2048,
            )

        self._log(req, decision)
        return decision

    def _log(self, req: InferenceRequest, decision: RouteDecision) -> None:
        if self.audit_logger is not None and hasattr(self.audit_logger, "record"):
            self.audit_logger.record(
                event="neural_route",
                payload={
                    "target": decision.target.value,
                    "reason": decision.reason,
                    "modality": req.modality.value,
                    "timestamp": decision.timestamp,
                },
            )
