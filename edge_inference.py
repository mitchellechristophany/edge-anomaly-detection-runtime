import numpy as np
from sklearn.ensemble import IsolationForest

# Synthesize Telemetry Sensor Data
np.random.seed(42)
normal_data = np.random.normal(loc=0.0, scale=1.0, size=(10000, 4))
anomalies = np.random.uniform(low=-4.0, high=4.0, size=(500, 4))
X = np.vstack([normal_data, anomalies])

# Train Isolation Forest Estimator
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

# Evaluate Ingestion
test_batch = np.random.normal(loc=0.0, scale=1.0, size=(100, 4))
predictions = model.predict(test_batch)

print("--- Edge Anomaly Detection Pipeline ---")
print(f"Processed batch size: {len(test_batch)}")
print(f"Anomalies Flagged: {np.sum(predictions == -1)}")
