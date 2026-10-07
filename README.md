# ⚡ Edge Anomaly Detection & Compiled Runtime Engine

An industrial telemetry pipeline for real-time anomaly detection, demonstrating model compilation and optimized cross-platform execution runtimes.

## 📌 Features
- **Tree-Based Anomaly Scoring:** Trains lightweight tree ensembles to isolate operational anomalies in high-frequency sensor streams.
- **Interoperable Open Format Export:** Converts trained estimators to open graph formats (ONNX) for runtime compilation.
- **Inference Latency Optimization:** Compares default Python execution against hardware-compiled inference runtimes.

## 📐 System Architecture
```text
[ High-Frequency Sensor Stream ]
               │
               ▼
   ┌───────────────────────┐
   │ Anomaly Classifier    │
   │ (Gradient Boosting)   │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │ ONNX Model Export     │
   └───────────┬───────────┘
               │
               ▼
   ┌───────────────────────┐
   │ Hardware-Optimized    │
   │ Inference Runtime     │
   └───────────────────────┘
