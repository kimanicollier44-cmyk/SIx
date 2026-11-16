import torch
import torch.nn as nn

class BiphasicElectricalStimulator(nn.Module):
    """Generates charge-balanced biphasic electrical pulses for nanoscale filament stabilization."""
    def __init__(self, dim: int = 64):
        super().__init__()
        self.dim = dim

    def generate_biphasic_pulse(self, step_idx: int) -> float:
        phase = step_idx % 10
        if phase < 5:
            return 1.0  # Cathodic growth phase
        else:
            return -1.0 # Anodic recovery phase

    def forward(self, activation_inputs: torch.Tensor) -> torch.Tensor:
        pulse = self.generate_biphasic_pulse(2)
        return activation_inputs * pulse
