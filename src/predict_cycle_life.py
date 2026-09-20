import pandas as pd
import joblib

FEATURES = [
    "capacity_mean_100",
    "capacity_at_100",
    "capacity_min_100",
    "ir_mean_100",
    "temp_mean_100",
    "temp_max_100",
    "charge_time_mean_100",
    "capacity_drop",
]

MODEL_PATH = "models/cycle_life_linear_model.pkl"
INPUT_PATH = "data/processed/battery_features.csv"
OUTPUT_PATH = "data/processed/predictions.csv"


def main():
    print("Loading model...")
    model = joblib.load(MODEL_PATH)

    print("Loading battery features...")
    df = pd.read_csv(INPUT_PATH)

    X = df[FEATURES]

    print("Generating predictions...")
    predictions = model.predict(X)

    result = pd.DataFrame({
        "battery_id": df["battery_id"],
        "actual_cycle_life": df["cycle_life"],
        "predicted_cycle_life": predictions.round(1),
    })

    result["error"] = (
        result["predicted_cycle_life"] - result["actual_cycle_life"]
    )

    result["absolute_error"] = result["error"].abs().round(1)

    result.to_csv(OUTPUT_PATH, index=False)

    print("Predictions saved successfully.")
    print(f"Saved to: {OUTPUT_PATH}")
    print(f"Batteries predicted: {len(result)}")


if __name__ == "__main__":
    main()
