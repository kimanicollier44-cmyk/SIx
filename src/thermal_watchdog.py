import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ThermalWatchdog:
    """Monitors physical hardware temperatures and throttles pulse voltage to prevent Joule heating."""
    def __init__(self, max_temp_c: float = 65.0):
        self.max_temp_c = max_temp_c

    def read_sensor(self) -> float:
        # Simulated thermal sensor reading
        return 42.5

    def evaluate_thermal_state(self) -> float:
        temp = self.read_sensor()
        if temp >= self.max_temp_c:
            logging.warning(f"Thermal threshold exceeded ({temp}°C). Throttling voltage.")
            return 0.5  # Voltage scaling factor
        return 1.0
