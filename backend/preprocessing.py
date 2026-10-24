import numpy as np
import pandas as pd


NUMERIC_COLS = [
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

WILDERNESS_COLS = [
    f"Wilderness_Area{i}" for i in range(1, 5)
]

SOIL_COLS = [
    f"Soil_Type{i}" for i in range(1, 41)
]


def prepare_features(payload, bundle):
    if not isinstance(payload, dict):
        raise ValueError("Expected an input object")

    expected = set(NUMERIC_COLS) | {
        "Wilderness_Area", "Soil_Type"
    }

    missing = expected - set(payload)
    extra = set(payload) - expected

    if missing or extra:
        raise ValueError(
            f"Missing: {sorted(missing)}, Extra: {sorted(extra)}"
        )

    row = {}

    for col in NUMERIC_COLS:
        value = payload[col]

        if isinstance(value, bool):
            raise ValueError(f"Invalid numeric value: {col}")

        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid numeric value: {col}")

        if not np.isfinite(value):
            raise ValueError(f"Non-finite value: {col}")

        row[col] = value

    # Validate categorical values
    wilderness = payload["Wilderness_Area"]
    soil = payload["Soil_Type"]

    if type(wilderness) is not int or not 1 <= wilderness <= 4:
        raise ValueError("Wilderness_Area must be 1-4")

    if type(soil) is not int or not 1 <= soil <= 40:
        raise ValueError("Soil_Type must be 1-40")

    # Restore original one-hot encoding
    for i in range(1, 5):
        row[f"Wilderness_Area{i}"] = int(wilderness == i)

    for i in range(1, 41):
        row[f"Soil_Type{i}"] = int(soil == i)

    df = pd.DataFrame([row])

    # Verify original schema
    df = df[bundle["base_features"]]

    # Same feature engineering as notebook
    hdh = df["Horizontal_Distance_To_Hydrology"]
    vdh = df["Vertical_Distance_To_Hydrology"]
    road = df["Horizontal_Distance_To_Roadways"]
    fire = df["Horizontal_Distance_To_Fire_Points"]

    aspect_rad = np.deg2rad(df["Aspect"])

    df["Hydro_Euclid_Dist"] = np.sqrt(hdh**2 + vdh**2)

    df["Elev_Minus_VDH"] = df["Elevation"] - vdh

    df["Elev_Minus_HDH_x0_2"] = (
        df["Elevation"] - 0.2 * hdh
    )

    df["Hydro_Fire_Sum"] = hdh + fire
    df["Hydro_Fire_AbsDiff"] = (hdh - fire).abs()
    df["Hydro_Road_Sum"] = hdh + road
    df["Fire_Road_Sum"] = fire + road

    df["Hillshade_Mean"] = df[
        ["Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm"]
    ].mean(axis=1)

    df["Aspect_Sin"] = np.sin(aspect_rad)
    df["Aspect_Cos"] = np.cos(aspect_rad)

    return df[bundle["model_features"]]