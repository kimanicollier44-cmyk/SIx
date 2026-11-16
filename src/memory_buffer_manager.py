import torch
import gc
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class MemoryBufferManager:
    """Manages high-frequency tensor memory pooling and garbage collection across MPS/CUDA backends."""
    def __init__(self, warning_threshold_mb: int = 4096):
        self.warning_threshold = warning_threshold_mb

    def optimize_memory(self):
        gc.collect()
        if torch.backends.mps.is_available():
            torch.mps.empty_cache()
            logging.info("Apple Silicon MPS cache emptied and garbage collected.")
        elif torch.cuda.is_available():
            torch.cuda.empty_cache()
            logging.info("CUDA memory cache emptied and garbage collected.")
