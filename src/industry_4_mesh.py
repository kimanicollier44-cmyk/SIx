import torch
import torch.nn as nn
import torch.nn.functional as F

class PhysicalMesh4Inf(nn.Module):
    """Unifies Industry 4.0 cyber-physical systems with valence memory and memristor crossbars."""
    def __init__(self, in_features: int = 128, out_features: int = 64):
        super().__init__()
        self.G0 = 7.748e-5
        self.sensor_fusion = nn.Linear(in_features, out_features)
        self.register_buffer("efficacy", torch.rand(out_features, in_features) * 0.4 + 0.3)

    def forward(self, industrial_telemetry: torch.Tensor, control_valence: torch.Tensor) -> torch.Tensor:
        features = F.gelu(self.sensor_fusion(industrial_telemetry))
        conductance = torch.round(self.efficacy * 16.0) * self.G0
        return torch.einsum('oi,bi->bo', conductance, features)
