import torch
import torch.nn as nn
import torch.nn.functional as F

class ErrorReducedNeuromorphicCore(nn.Module):
    """Incorporates noise-filtering gates, homeostatic calcium correction, and fault-tolerant bounding."""
    def __init__(self, in_features: int = 128, out_features: int = 64):
        super().__init__()
        self.G0 = 7.748e-5
        self.register_buffer("synaptic_efficacy", torch.rand(out_features, in_features) * 0.4 + 0.3)
        self.register_buffer("calcium_trace", torch.zeros(out_features, in_features))
        self.register_buffer("error_correction_count", torch.tensor([0]))

    def filter_sensor_noise(self, raw_sensor_spikes: torch.Tensor, noise_threshold: float = 0.15) -> torch.Tensor:
        mask = (raw_sensor_spikes > noise_threshold).float()
        return raw_sensor_spikes * mask

    def forward(self, raw_spikes: torch.Tensor, valence_feedback: torch.Tensor, thermal_temp_c: float = 28.0) -> torch.Tensor:
        cleaned_spikes = self.filter_sensor_noise(raw_spikes)

        with torch.no_grad():
            coincidence = torch.einsum("bi,bo->oi", cleaned_spikes, cleaned_spikes) * 0.05
            self.calcium_trace.mul_(0.85).add_(coincidence)
            excess_calcium = torch.relu(self.calcium_trace - 2.0)
            if excess_calcium.sum() > 0:
                self.error_correction_count.add_(1)
            self.calcium_trace.sub_(excess_calcium * 0.2).clamp_(0.0, 2.5)

            thermal_factor = 1.0 + 0.0025 * (thermal_temp_c - 25.0)
            valence_factor = valence_feedback.mean(dim=0).unsqueeze(1)
            delta = ((self.calcium_trace * 0.01) + (valence_factor * 0.02)) / thermal_factor
            self.synaptic_efficacy.add_(delta).clamp_(0.01, 0.99)

        conductance = torch.round(self.synaptic_efficacy * 16.0) * self.G0
        return F.gelu(torch.einsum('oi,bi->bo', conductance, cleaned_spikes))
