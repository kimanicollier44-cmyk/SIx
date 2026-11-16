import torch
import torch.nn as nn

class SpikingNeuralNetworkCodec(nn.Module):
    """Converts continuous analog telemetry vectors into discrete spike trains and back."""
    def __init__(self, dim: int = 64, threshold: float = 0.5):
        super().__init__()
        self.dim = dim
        self.threshold = threshold

    def encode_to_spikes(self, analog_tensor: torch.Tensor, time_steps: int = 10) -> torch.Tensor:
        membrane = torch.zeros_like(analog_tensor)
        spike_trains = []
        for _ in range(time_steps):
            membrane = 0.85 * membrane + analog_tensor
            spikes = (membrane >= self.threshold).float()
            membrane = membrane * (1.0 - spikes)
            spike_trains.append(spikes)
        return torch.stack(spike_trains, dim=0)

    def decode_to_analog(self, spike_trains: torch.Tensor) -> torch.Tensor:
        return spike_trains.mean(dim=0)
