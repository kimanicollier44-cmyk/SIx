import torch
import torch.nn as nn
import torch.nn.functional as F

class EthicalGoalAutomationCore(nn.Module):
    """Balances autonomous goal pursuit with strict ethical constraint filtering."""
    def __init__(self, latent_dim: int = 64, action_dim: int = 32):
        super().__init__()
        self.G0 = 7.748e-5
        self.goal_planner = nn.Linear(latent_dim, action_dim)
        self.ethics_evaluator = nn.Linear(action_dim, 1)

        self.register_buffer("synaptic_efficacy", torch.rand(action_dim, action_dim) * 0.4 + 0.3)
        self.register_buffer("calcium_trace", torch.zeros(action_dim, action_dim))
        self.register_buffer("autonomous_step_counter", torch.tensor([0]))

    def enforce_ethical_bounds(self, proposed_actions: torch.Tensor):
        safety_scores = torch.sigmoid(self.ethics_evaluator(proposed_actions))
        ethical_mask = (safety_scores >= 0.75).float()
        return proposed_actions * ethical_mask, safety_scores

    def forward(self, environmental_state, goal_vector, valence_feedback):
        self.autonomous_step_counter.add_(1)
        raw_actions = F.gelu(self.goal_planner(environmental_state + goal_vector))
        safe_actions, safety_scores = self.enforce_ethical_bounds(raw_actions)

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", safe_actions, safe_actions) * 0.05
            self.calcium_trace.mul_(0.85).add_(coincidence)
            self.calcium_trace.sub_(torch.relu(self.calcium_trace - 2.0) * 0.15)
            valence_factor = valence_feedback.mean(dim=0).unsqueeze(1) * safety_scores.mean()
            delta = (self.calcium_trace * 0.01) + (valence_factor * 0.02)
            self.synaptic_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.synaptic_efficacy * 16.0) * self.G0
        return F.tanh(torch.einsum('oi,bi->bo', conductance, safe_actions))
