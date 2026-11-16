import hashlib
import json
import torch
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class HoneypotXWatchdog:
    """Isolates compromised nodes and triggers rclone state preservation on breach."""
    def __init__(self, node_id: str, remote_bucket: str = "secure-mesh:checkpoints"):
        self.node_id = node_id
        self.remote_bucket = remote_bucket
        self.quarantined = False

    def inspect_telemetry(self, safety_score: float, gradient_norm: float) -> bool:
        if safety_score < 0.75 or gradient_norm > 12.0:
            self.quarantined = True
            logging.critical(f"[{self.node_id}] HoneypotX Tripwire Triggered! Safety={safety_score:.3f}")
            return False
        return True

    def emergency_checkpoint_sync(self, state_dict: dict, local_path: str = "/tmp/mesh_emergency.pt"):
        torch.save(state_dict, local_path)
        digest = hashlib.sha256(json.dumps(str(state_dict)).encode()).hexdigest()[:16]
        logging.info(f"[{self.node_id}] State serialized ({digest}). Syncing -> {self.remote_bucket}")
