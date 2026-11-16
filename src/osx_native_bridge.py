import platform
import torch
import torch.nn as nn
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class OSXNativeBridge(nn.Module):
    """Initializes nanoscale crossbar directly on Apple Silicon's MPS backend."""
    def __init__(self, dim: int = 64):
        super().__init__()
        self.device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        logging.info(f"OSX Native Bridge initialized on target device: {self.device}")
        
        self.bridge_layer = nn.Linear(dim, dim).to(self.device)
        self.register_buffer("weights", torch.rand(dim, dim, device=self.device) * 0.5 + 0.25)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        tensor = x.to(self.device)
        return torch.matmul(tensor, self.weights.T)
