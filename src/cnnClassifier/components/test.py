import os

# Accessing the MLFLOW_TRACKING_URI environment variable
mlflow_tracking_uri = os.environ.get('MLFLOW_TRACKING_URI')

# Checking if the variable exists and printing its value
if mlflow_tracking_uri:
    print(f"MLflow Tracking URI: {mlflow_tracking_uri}")
else:
    print("MLFLOW_TRACKING_URI environment variable is not set.")
