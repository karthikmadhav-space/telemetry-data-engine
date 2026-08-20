"""
Real-Time Telemetry Data Engine & Signal Filter
Author: Karthik Madhav
Target: Serial Ingestion & Visualization from Embedded Systems
"""

import time
import math
import numpy as np
import matplotlib.pyplot as plt

class TelemetryEngine:
    def __init__(self, alpha: float = 0.15):
        self.alpha = alpha  # Low-pass filter smoothing factor
        self.raw_buffer = []
        self.filtered_buffer = []
        self.timestamps = []

    def filter_signal(self, raw_val: float) -> float:
        """Applies an Exponential Moving Average (EMA) low-pass filter."""
        if not self.filtered_buffer:
            return raw_val
        prev_filtered = self.filtered_buffer[-1]
        return self.alpha * raw_val + (1.0 - self.alpha) * prev_filtered

    def ingest_sample(self, timestamp: float, raw_val: float):
        filtered_val = self.filter_signal(raw_val)
        self.timestamps.append(timestamp)
        self.raw_buffer.append(raw_val)
        self.filtered_buffer.append(filtered_val)

def generate_mock_sensor_stream(t: float) -> float:
    """Simulates IMU/Accelerometer signal with high-frequency noise."""
    base_signal = math.sin(2 * math.pi * 0.2 * t)
    noise = np.random.normal(0, 0.2)
    return base_signal + noise

if __name__ == "__main__":
    engine = TelemetryEngine(alpha=0.2)
    start_time = time.time()

    print("[INFO] Starting Telemetry Data Ingestion Stream...")
    for i in range(100):
        curr_time = time.time() - start_time
        raw_reading = generate_mock_sensor_stream(curr_time)
        engine.ingest_sample(curr_time, raw_reading)
        time.sleep(0.05)

    print(f"[SUCCESS] Processed {len(engine.raw_buffer)} samples successfully.")
