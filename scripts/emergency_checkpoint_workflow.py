#!/usr/bin/env python3
import os
import sys
import subprocess
import logging
import torch

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class EmergencyCheckpointManager:
    """
    Handles emergency state checkpointing and rclone secure-mesh synchronization 
    for SI-X edge nodes (e.g., Jetson Orin Nano).
    """
    def __init__(self, node_id: str = "jetson-orin-01", remote_target: str = "secure-mesh:checkpoints/si-x/"):
        self.node_id = node_id
        self.remote_target = f"{remote_target}{node_id}"

    def create_tensor_checkpoint(self, safety_score: float) -> str:
        os.makedirs("checkpoints", exist_ok=True)
        filename = f"checkpoints/emergency_state_{self.node_id}.pt"
        
        # Generate state tensor representing system health and neuron weights
        state_tensor = torch.tensor([safety_score, 1.0 - safety_score, 0.85], dtype=torch.float32)
        torch.save({
            "node_id": self.node_id,
            "safety_score": safety_score,
            "tensor_state": state_tensor
        }, filename)
        
        logging.info(f"Emergency checkpoint successfully generated at {filename}")
        return filename

    def sync_to_mesh(self, filepath: str):
        # Check if rclone is available and configured
        try:
            remotes = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True, check=True)
            if "secure-mesh:" not in remotes.stdout:
                logging.warning("rclone remote 'secure-mesh:' not found. Skipping remote sync.")
                return
        except (subprocess.SubprocessError, FileNotFoundError):
            logging.warning("rclone command not found or failed. Skipping remote synchronization.")
            return

        logging.info(f"Synchronizing {filepath} to {self.remote_target} via rclone...")
        result = subprocess.run(["rclone", "copy", filepath, self.remote_target], capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info("Checkpoint successfully synced to secure mesh!")
        else:
            logging.error(f"Failed to sync checkpoint: {result.stderr}")

def main():
    node_id = os.getenv("SI_X_NODE_ID", "jetson-orin-01")
    safety_score = float(os.getenv("SI_X_SAFETY_SCORE", "0.62"))
    
    manager = EmergencyCheckpointManager(node_id=node_id)
    ckpt_path = manager.create_tensor_checkpoint(safety_score=safety_score)
    manager.sync_to_mesh(ckpt_path)

if __name__ == "__main__":
    main()
