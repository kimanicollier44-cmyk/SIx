import torch

class DistributedConsensusValidator:
    """Validates consensus state across distributed edge nodes using median voting."""
    def __init__(self, tolerance: float = 0.15):
        self.tolerance = tolerance

    def validate_states(self, node_states: list[torch.Tensor]) -> torch.Tensor:
        stacked = torch.stack(node_states, dim=0)
        median_state = torch.median(stacked, dim=0).values
        diff = torch.abs(stacked - median_state)
        valid_mask = (diff <= self.tolerance).float()
        return (stacked * valid_mask).sum(dim=0) / valid_mask.sum(dim=0).clamp(min=1.0)
