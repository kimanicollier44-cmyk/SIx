import torch
import torch.nn as nn
import torch.nn.functional as F

class CreativeGenerativeEngine(nn.Module):
    """Combines multi-modal latent generation with valence-modulated artistic evolution."""
    def __init__(self, latent_dim: int = 64, output_dim: int = 128):
        super().__init__()
        self.G0 = 7.748e-5
        self.style_generator = nn.Linear(latent_dim, output_dim)
        self.content_generator = nn.Linear(latent_dim, output_dim)
        self.fusion_mixer = nn.Linear(output_dim * 2, output_dim)

        self.register_buffer("creative_synapse_efficacy", torch.rand(output_dim, output_dim) * 0.4 + 0.3)
        self.register_buffer("aesthetic_calcium_trace", torch.zeros(output_dim, output_dim))
        self.register_buffer("generation_counter", torch.tensor([0]))

    def forward(self, style_seed, content_seed, aesthetic_valence, mutation_rate: float = 0.02):
        self.generation_counter.add_(1)
        style_feat = F.gelu(self.style_generator(style_seed))
        content_feat = F.gelu(self.content_generator(content_seed))
        combined = torch.cat([style_feat, content_feat], dim=-1)
        creative_latent = F.relu(self.fusion_mixer(combined))

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", creative_latent, creative_latent) * 0.05
            self.aesthetic_calcium_trace.mul_(0.85).add_(coincidence)
            self.aesthetic_calcium_trace.sub_(torch.relu(self.aesthetic_calcium_trace - 2.0) * 0.15)

            mutation_mask = (torch.rand_like(self.creative_synapse_efficacy) < mutation_rate).float()
            random_drift = torch.randn_like(self.creative_synapse_efficacy) * 0.03
            valence_factor = aesthetic_valence.mean(dim=0).unsqueeze(1)
            delta = (self.aesthetic_calcium_trace * 0.01) + (valence_factor * 0.02) + (mutation_mask * random_drift)
            self.creative_synapse_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.creative_synapse_efficacy * 16.0) * self.G0
        return F.tanh(torch.einsum('oi,bi->bo', conductance, creative_latent))
