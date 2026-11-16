import torch

class CalciumHomeostaticController:
    """Implements SERCA/NCX biological mimics to prevent neural lockup and saturation."""
    def __init__(self, shape: tuple, saturation_limit: float = 2.0):
        self.calcium_trace = torch.zeros(shape)
        self.saturation_limit = saturation_limit

    def regulate(self, incoming_coincidence: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            self.calcium_trace.mul_(0.85).add_(incoming_coincidence * 0.05)
            excess = torch.relu(self.calcium_trace - self.saturation_limit)
            self.calcium_trace.sub_(excess * 0.2).clamp_(0.0, 2.5)
        return self.calcium_trace
