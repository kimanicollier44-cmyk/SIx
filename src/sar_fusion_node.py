import torch
import torch.nn as nn
import torch.nn.functional as F

class SARNeuromorphicFusionNode(nn.Module):
    """Processes orbital radar telemetry and fuses spatial backscatter grids into the AGI crossbar."""
    def __init__(self, radar_channels: int = 1, latent_dim: int = 64):
        super().__init__()
        self.G0 = 7.748e-5
        self.sar_encoder = nn.Sequential(
            nn.Conv2d(radar_channels, 16, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(16),
            nn.GELU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(32),
            nn.GELU(),
            nn.AdaptiveAvgPool2d((8, 8)),
            nn.Flatten()
        )
        self.fc_proj = nn.Linear(32 * 8 * 8, latent_dim)
        self.register_buffer("synaptic_efficacy", torch.rand(latent_dim, latent_dim) * 0.4 + 0.3)
        self.register_buffer("calcium_trace", torch.zeros(latent_dim, latent_dim))

    def filter_sar_speckle(self, raw_sar_tensor: torch.Tensor) -> torch.Tensor:
        kernel = torch.ones(1, 1, 3, 3, device=raw_sar_tensor.device) / 9.0
        smoothed = F.conv2d(raw_sar_tensor, kernel, padding=1)
        return torch.clamp(raw_sar_tensor - (smoothed * 0.15), 0.0, 1.0)

    def forward(self, sar_backscatter, valence_feedback):
        cleaned_sar = self.filter_sar_speckle(sar_backscatter)
        spatial_feats = self.sar_encoder(cleaned_sar)
        latent_state = F.gelu(self.fc_proj(spatial_feats))

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", latent_state, latent_state) * 0.05
            self.calcium_trace.mul_(0.85).add_(coincidence)
            self.calcium_trace.sub_(torch.relu(self.calcium_trace - 2.0) * 0.15)
            valence_factor = valence_feedback.mean(dim=0).unsqueeze(1)
            delta = (self.calcium_trace * 0.01) + (valence_factor * 0.02)
            self.synaptic_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.synaptic_efficacy * 16.0) * self.G0
        return F.gelu(torch.einsum('oi,bi->bo', conductance, latent_state))
