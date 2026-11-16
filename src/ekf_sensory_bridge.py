import torch

class ExtendedKalmanSensorFilter:
    """Nonlinear state estimator filtering multi-modal sensor drift."""
    def __init__(self, state_dim: int = 16, process_noise: float = 1e-3, meas_noise: float = 5e-2):
        self.dim = state_dim
        self.x = torch.zeros(state_dim)
        self.P = torch.eye(state_dim)
        self.Q = torch.eye(state_dim) * process_noise
        self.R = torch.eye(state_dim) * meas_noise

    def step(self, z: torch.Tensor) -> torch.Tensor:
        x_pred = self.x + 0.05 * torch.tanh(self.x)
        F_jac = torch.eye(self.dim) + 0.05 * torch.diag(1.0 - torch.tanh(self.x) ** 2)
        P_pred = F_jac @ self.P @ F_jac.T + self.Q

        H_jac = torch.eye(self.dim)
        y = z - x_pred
        S = H_jac @ P_pred @ H_jac.T + self.R
        K = P_pred @ H_jac.T @ torch.linalg.inv(S)

        self.x = x_pred + K @ y
        self.P = (torch.eye(self.dim) - K @ H_jac) @ P_pred
        return self.x

def tactile_to_spike_train(filtered_pressure: torch.Tensor, steps: int = 10, threshold: float = 0.45) -> torch.Tensor:
    membrane = torch.zeros_like(filtered_pressure)
    spikes = []
    for _ in range(steps):
        membrane = 0.85 * membrane + filtered_pressure
        fired = (membrane >= threshold).float()
        membrane = membrane * (1.0 - fired)
        spikes.append(fired)
    return torch.stack(spikes, dim=0)
