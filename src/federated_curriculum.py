import torch

class CurriculumScheduler:
    """Ramps task difficulty [0.1 -> 1.0] as edge meta-learner accuracy stabilizes."""
    def __init__(self, initial_difficulty: float = 0.2, target_accuracy: float = 0.85):
        self.difficulty = initial_difficulty
        self.target_accuracy = target_accuracy

    def step(self, mean_accuracy: float) -> float:
        if mean_accuracy >= self.target_accuracy:
            self.difficulty = min(1.0, round(self.difficulty + 0.1, 2))
        elif mean_accuracy < self.target_accuracy - 0.15:
            self.difficulty = max(0.1, round(self.difficulty - 0.05, 2))
        return self.difficulty

def federated_synaptic_aggregation(node_weights: list[torch.Tensor], node_accuracies: list[float], byzantine_clip: float = 0.25) -> torch.Tensor:
    stacked = torch.stack(node_weights, dim=0)
    median_weights = torch.median(stacked, dim=0).values
    clipped = torch.clamp(stacked, median_weights - byzantine_clip, median_weights + byzantine_clip)
    scores = torch.tensor(node_accuracies, dtype=torch.float32)
    norm_weights = torch.softmax(scores * 5.0, dim=0).view(-1, 1, 1)
    return (clipped * norm_weights).sum(dim=0).clamp(0.01, 0.99)
