import torch
import torch.nn as nn
import torch.nn.functional as F

class ZeroShotAGICrossbar(nn.Module):
    """Central AGI crossbar capable of absorbing dynamically registered ANI experts."""
    def __init__(self, agi_dim: int = 64):
        super().__init__()
        self.agi_dim = agi_dim
        self.G0 = 7.748e-5
        self.experts = nn.ModuleDict()
        self.register_buffer("synaptic_efficacy", torch.rand(agi_dim, agi_dim) * 0.3 + 0.35)
        self.register_buffer("calcium_trace", torch.zeros(agi_dim, agi_dim))

    def register_ani_expert(self, name: str, input_dim: int):
        proj = nn.Linear(input_dim, self.agi_dim)
        nn.init.orthogonal_(proj.weight)
        self.experts[name] = proj

    def forward(self, expert_outputs: dict[str, torch.Tensor], valence: torch.Tensor) -> torch.Tensor:
        projected = [self.experts[k](v) for k, v in expert_outputs.items() if k in self.experts]
        unified = torch.stack(projected, dim=0).mean(dim=0)

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", unified, unified) * 0.04
            self.calcium_trace.mul_(0.85).add_(coincidence)
            self.calcium_trace.sub_(torch.relu(self.calcium_trace - 2.0) * 0.15)
            delta = (self.calcium_trace * 0.01) + (valence.mean(dim=0).unsqueeze(1) * 0.02)
            self.synaptic_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.synaptic_efficacy * 16.0) * self.G0
        return F.gelu(torch.einsum("oi,bi->bo", conductance, unified))
