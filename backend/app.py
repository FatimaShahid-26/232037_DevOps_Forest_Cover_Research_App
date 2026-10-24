from pathlib import Path

import joblib
import numpy as np
from flask import Flask, request, jsonify

from preprocessing import prepare_features


BASE = Path(__file__).resolve().parent

bundle = joblib.load(
    BASE / "models/forest_bundle.joblib"
)

MODELS = bundle["models"]

COVER_TYPES = {
    1: "Spruce/Fir",
    2: "Lodgepole Pine",
    3: "Ponderosa Pine",
    4: "Cottonwood/Willow",
    5: "Aspen",
    6: "Douglas-fir",
    7: "Krummholz",
}

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "models": list(MODELS),
        "feature_count": len(bundle["model_features"])
    })


@app.get("/models")
def get_models():
    return jsonify({
        "models": list(MODELS.keys())
    })


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Expected a JSON object"
        }), 400

    model_name = data.get("model")
    features = data.get("features")

    if model_name not in MODELS:
        return jsonify({
            "error": "Invalid model name"
        }), 400

    try:
        X = prepare_features(features, bundle)

        model = MODELS[model_name]

        # KNN uses the original fitted scaler
        if model_name == "knn":
            X_input = bundle["scaler"].transform(X)
        else:
            X_input = X

        prediction = model.predict(X_input)[0]

        probabilities = model.predict_proba(X_input)[0]

        # XGBoost returns encoded classes 0-6
        if model_name == "xgboost":
            class_labels = bundle[
                "label_encoder"
            ].inverse_transform(model.classes_.astype(int))

            prediction = bundle[
                "label_encoder"
            ].inverse_transform([int(prediction)])[0]
        else:
            class_labels = model.classes_

        prediction = int(prediction)

        probability_map = {
            str(int(label)): float(prob)
            for label, prob in zip(class_labels, probabilities)
        }

        return jsonify({
            "model": model_name,
            "prediction": prediction,
            "cover_name": COVER_TYPES[prediction],
            "confidence": round(
                100 * probability_map[str(prediction)], 2
            ),
            "probabilities": probability_map,
            "disclaimer": "Research and teaching prototype only."
        })

    except (ValueError, KeyError, TypeError) as exc:
        return jsonify({
            "error": str(exc)
        }), 400

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "Prediction processing failed"
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )