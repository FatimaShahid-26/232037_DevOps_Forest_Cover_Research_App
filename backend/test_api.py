import json
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parent

features = json.loads(
    (BASE / "test_payload.json").read_text()
)

models = [
    "decision_tree",
    "random_forest",
    "knn",
    "xgboost"
]

session = requests.Session()
session.trust_env = False

for model in models:

    response = session.post(
        "http://127.0.0.1:5000/predict",
        json={
            "model": model,
            "features": features
        },
        timeout=120
    )

    print("\nModel:", model)
    print("Status:", response.status_code)
    print("Response:", response.json())

    response.raise_for_status()

print("\nPASS: All four APIs work")