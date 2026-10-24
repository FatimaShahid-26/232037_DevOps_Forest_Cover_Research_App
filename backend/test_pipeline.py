import json
import joblib
from pathlib import Path

from preprocessing import prepare_features

BASE = Path(__file__).resolve().parent

bundle = joblib.load(BASE / "models/forest_bundle.joblib")

payload = json.loads(
    (BASE / "test_payload.json").read_text()
)

X = prepare_features(payload, bundle)

assert X.shape[1] == 64

for name, model in bundle["models"].items():

    X_input = (
        bundle["scaler"].transform(X)
        if name == "knn"
        else X
    )

    prediction = model.predict(X_input)[0]

    if name == "xgboost":
        prediction = bundle["label_encoder"].inverse_transform(
            [int(prediction)]
        )[0]

    print(name, "=>", int(prediction))

print("PASS: Direct model inference")