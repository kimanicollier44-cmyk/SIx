import torch

class AdversarialGradientDefense:
    """Detects and neutralizes adversarial gradient poisoning attacks on memristive crossbars."""
    def __init__(self, max_allowable_norm: float = 12.0):
        self.max_norm = max_allowable_norm

    def sanitize_gradients(self, gradient_tensor: torch.Tensor) -> torch.Tensor:
        norm = torch.norm(gradient_tensor)
        if norm > self.max_norm:
            return gradient_tensor * (self.max_norm / norm)
        return gradient_tensor
