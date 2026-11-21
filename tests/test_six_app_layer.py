import asyncio
from fastapi.testclient import TestClient

from src.app_gateway import app
from src.multimodal_engine import MultimodalEngine
from src.neural_router import InferenceRequest, Modality, NeuralRouter, RouteTarget


class _BlockGuard:
    def inspect(self, prompt: str, metadata: dict):
        if "drop table" in prompt.lower():
            return False, "Dangerous command pattern"
        return True, "Clean"


def test_router_routes_fast_and_blocked():
    router = NeuralRouter(safety_guard=_BlockGuard())

    blocked = router.route(InferenceRequest(prompt="DROP TABLE users;"))
    assert blocked.target == RouteTarget.SAFETY_BLOCKED

    fast = router.route(InferenceRequest(prompt="ping", low_latency_required=True))
    assert fast.target == RouteTarget.NEUROMORPHIC_FAST


def test_engine_neuromorphic_fast_pass():
    engine = MultimodalEngine()
    req = InferenceRequest(
        prompt="telemetry check",
        modality=Modality.SENSOR,
        sensor_telemetry={"temp": 42.5, "voltage": 3.3},
    )
    result = asyncio.run(engine.infer(req))
    assert result["status"] == "ok"
    assert result["route"] == RouteTarget.NEUROMORPHIC_FAST.value


def test_gateway_health_and_ask():
    client = TestClient(app)
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "online"

    ask_res = client.post(
        "/ask",
        json={"prompt": "sensor pulse", "low_latency_required": True},
    )
    assert ask_res.status_code == 200
    assert ask_res.json()["route"] == "neuromorphic_fast"
