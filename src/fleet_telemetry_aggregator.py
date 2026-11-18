import torch
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class FleetTelemetryAggregator:
    """Aggregates distributed edge telemetry from robotic swarms and orbital SAR nodes."""
    def __init__(self):
        self.node_registry = {}

    def register_node_telemetry(self, node_id: str, state_tensor: torch.Tensor):
        self.node_registry[node_id] = {
            "timestamp": torch.cuda.current_event() if torch.cuda.is_available() else 0,
            "tensor": state_tensor
        }

    def compute_fleet_consensus(self) -> torch.Tensor:
        tensors = [data["tensor"] for data in self.node_registry.values()]
        if not tensors:
            return torch.zeros(64)
        stacked = torch.stack(tensors, dim=0)
        return torch.median(stacked, dim=0).values

    def docker_fleet_summary(self) -> dict:
        """Dated snapshot of the fleet's published Docker images.

        Delegates to src.docker_fleet_registry (frozen catalogue,
        no network); kept separate from the live node telemetry above.
        """
        from src.docker_fleet_registry import registry_summary
        return registry_summary()
