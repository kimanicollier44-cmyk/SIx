import torch
import torch.nn as nn

class ErrorReductionMesh(nn.Module):
    """
    Error reduction mesh module handling calcium trace multiplication 
    and resilient tensor alignment for SI-X.
    """
    def __init__(self, feature_dim=64):
        super().__init__()
        self.feature_dim = feature_dim
        # Optional projection layers if dynamic input sizes need alignment
        self.adapter_a = nn.Linear(32, feature_dim)
        self.adapter_b = nn.Linear(64, feature_dim)

    def forward(self, tensor_a: torch.Tensor, tensor_b: torch.Tensor) -> torch.Tensor:
        # Ensure dimensions match before combining tensors
        if tensor_a.shape[-1] != tensor_b.shape[-1]:
            if tensor_a.shape[-1] == 32:
                tensor_a = self.adapter_a(tensor_a)
            if tensor_b.shape[-1] == 32:
                tensor_b = self.adapter_b(tensor_b) if tensor_b.shape[-1] != 64 else tensor_b
                
        # Handle non-singleton dimension 0 alignment if necessary
        if tensor_a.shape[0] != tensor_b.shape[0]:
            min_batch = min(tensor_a.shape[0], tensor_b.shape[0])
            tensor_a = tensor_a[:min_batch]
            tensor_b = tensor_b[:min_batch]

        # Calcium trace multiplication / error reduction logic
        calcium_weighted = tensor_a * tensor_b * 0.85
        return calcium_weighted
