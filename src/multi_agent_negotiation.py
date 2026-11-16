import torch
import torch.nn as nn
import torch.nn.functional as F
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class MultiAgentNegotiationEngine(nn.Module):
    """Facilitates decentralized task allocation and consensus negotiation among autonomous edge agents."""
    def __init__(self, latent_dim: int = 64):
        super().__init__()
        self.G0 = 7.748e-5
        self.proposal_encoder = nn.Linear(latent_dim, latent_dim)
        self.utility_evaluator = nn.Linear(latent_dim, 1)

        self.register_buffer("synaptic_efficacy", torch.rand(latent_dim, latent_dim) * 0.4 + 0.3)
        self.register_buffer("calcium_trace", torch.zeros(latent_dim, latent_dim))

    def forward(self, agent_proposals: torch.Tensor, global_valence: torch.Tensor) -> torch.Tensor:
        encoded = F.gelu(self.proposal_encoder(agent_proposals))
        utility_scores = torch.sigmoid(self.utility_evaluator(encoded))
        weighted_proposals = encoded * utility_scores

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", weighted_proposals, weighted_proposals) * 0.05
            self.calcium_trace.mul_(0.85).add_(coincidence)
            self.calcium_trace.sub_(torch.relu(self.calcium_trace - 2.0) * 0.15)
            valence_factor = global_valence.mean(dim=0).unsqueeze(1)
            delta = (self.calcium_trace * 0.01) + (valence_factor * 0.02)
            self.synaptic_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.synaptic_efficacy * 16.0) * self.G0
        return F.gelu(torch.einsum('oi,bi->bo', conductance, weighted_proposals))
