import torch
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class WeightsVersionManager:
    """Manages semantic versioning and checkpoint rotation for AGI crossbar weights."""
    def __init__(self, checkpoint_dir: str = "./checkpoints"):
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def save_version(self, model_state: dict, version_tag: str):
        path = os.path.join(self.checkpoint_dir, f"si_x_weights_v{version_tag}.pt")
        torch.save(model_state, path)
        logging.info(f"Successfully saved crossbar weights version v{version_tag} -> {path}")

    def load_version(self, version_tag: str) -> dict:
        path = os.path.join(self.checkpoint_dir, f"si_x_weights_v{version_tag}.pt")
        logging.info(f"Loading crossbar weights from {path}")
        return torch.load(path)
