# Real-Time Embedded Telemetry & Data Visualization Engine

High-performance Python pipeline for serial data ingestion, numerical filtering, and real-time telemetry plotting from embedded sensor nodes.

---

### 🛠 Architecture & Tech Stack

```text
 [ Sensor Node ] ---> (UART Serial) ---> [ Python Ingestion ] ---> [ NumPy / SciPy ] ---> [ Real-Time Plot ]
  (IMU / Temp)        (115200 Baud)         (PySerial)               (Filtering)          (Matplotlib)

Language: Python 3.10+

Core Libraries: PySerial, NumPy, SciPy, Matplotlib

Protocols: Serial Communication (UART/USB)

🚀 Key Features
Non-blocking Serial Stream Reading: Runs on an isolated ingestion thread to prevent UI frame drops.

Low-Pass Noise Filtering: Implements rolling window exponential moving average filtering for noisy sensor inputs (e.g., IMU/accelerometer data).

Live Dynamic Plotting: Real-time Matplotlib canvas redrawing for multi-channel data stream analysis.
