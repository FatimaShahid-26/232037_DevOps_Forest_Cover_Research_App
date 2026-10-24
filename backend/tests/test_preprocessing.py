import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from preprocessing import prepare_features


BASE_FEATURES = [
    "Elevation",
    "Aspect",
    "Slope",
    "Horizontal_Distance_To_Hydrology",
    "Vertical_Distance_To_Hydrology",
    "Horizontal_Distance_To_Roadways",
    "Hillshade_9am",
    "Hillshade_Noon",
    "Hillshade_3pm",
    "Horizontal_Distance_To_Fire_Points",
]

BASE_FEATURES += [
    f"Wilderness_Area{i}" for i in range(1, 5)
]

BASE_FEATURES += [
    f"Soil_Type{i}" for i in range(1, 41)
]

ENGINEERED_FEATURES = [
    "Hydro_Euclid_Dist",
    "Elev_Minus_VDH",
    "Elev_Minus_HDH_x0_2",
    "Hydro_Fire_Sum",
    "Hydro_Fire_AbsDiff",
    "Hydro_Road_Sum",
    "Fire_Road_Sum",
    "Hillshade_Mean",
    "Aspect_Sin",
    "Aspect_Cos",
]

SCHEMA = {
    "base_features": BASE_FEATURES,
    "model_features": BASE_FEATURES + ENGINEERED_FEATURES,
}


def sample_payload():
    return {
        "Elevation": 2800,
        "Aspect": 180,
        "Slope": 15,
        "Horizontal_Distance_To_Hydrology": 300,
        "Vertical_Distance_To_Hydrology": 50,
        "Horizontal_Distance_To_Roadways": 1000,
        "Hillshade_9am": 210,
        "Hillshade_Noon": 230,
        "Hillshade_3pm": 150,
        "Horizontal_Distance_To_Fire_Points": 700,
        "Wilderness_Area": 1,
        "Soil_Type": 10,
    }


def test_feature_count():
    X = prepare_features(sample_payload(), SCHEMA)

    assert X.shape == (1, 64)


def test_wilderness_encoding():
    X = prepare_features(sample_payload(), SCHEMA)

    assert X["Wilderness_Area1"].iloc[0] == 1
    assert X["Wilderness_Area2"].iloc[0] == 0


def test_soil_encoding():
    X = prepare_features(sample_payload(), SCHEMA)

    assert X["Soil_Type10"].iloc[0] == 1
    assert X["Soil_Type11"].iloc[0] == 0


def test_missing_elevation():
    payload = sample_payload()
    del payload["Elevation"]

    with pytest.raises(ValueError):
        prepare_features(payload, SCHEMA)


def test_invalid_soil_type():
    payload = sample_payload()
    payload["Soil_Type"] = 50

    with pytest.raises(ValueError):
        prepare_features(payload, SCHEMA)