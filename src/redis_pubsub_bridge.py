import redis
import json
import torch
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class RedisTelemetryBroker:
    """Manages real-time pub/sub telemetry routing across distributed cluster nodes."""
    def __init__(self, host: str = 'localhost', port: int = 6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)
        self.pubsub = self.client.pubsub()

    def publish_telemetry(self, channel: str, state_tensor: torch.Tensor):
        payload = {
            "tensor_shape": list(state_tensor.shape),
            "data": state_tensor.flatten().tolist()
        }
        self.client.publish(channel, json.dumps(payload))

    def subscribe_channel(self, channel: str, callback):
        self.pubsub.subscribe(**{channel: callback})
        self.pubsub.run_in_thread(sleep_time=0.01)

if __name__ == "__main__":
    broker = RedisTelemetryBroker()
    mock_tensor = torch.randn(8, 64)
    broker.publish_telemetry("si_x:telemetry:edge", mock_tensor)
    logging.info("Published test telemetry payload to Redis broker.")
