import torch
import torch.nn as nn

class ValenceMemoryController(nn.Module):
    """Modulates calcium influx and atomic switch conductance states via valence reinforcement."""
    def __init__(self, dim: int = 64):
        super().__init__()
        self.dim = dim
        self.register_buffer("valence_weights", torch.zeros(dim, dim))

    def update_valence(self, activation_state: torch.Tensor, like_dislike_signal: torch.Tensor):
        with torch.no_grad():
            feedback = like_dislike_signal.mean(dim=0).unsqueeze(1)
            delta = torch.einsum("bi,bo->oi", activation_state, activation_state) * 0.01 * feedback
            self.valence_weights.add_(delta).clamp_(-1.0, 1.0)
