import h5py
import pandas as pd
import os


INPUT_FILE = "data/raw/2017-05-12_batchdata_updated_struct_errorcorrect.mat"
OUTPUT_FILE = "data/processed/battery_summary.csv"


def extract_data():
    rows = []

    with h5py.File(INPUT_FILE, "r") as f:
        batch = f["batch"]

        number_of_batteries = batch["summary"].shape[0]

        print("Number of batteries:", number_of_batteries)

        for i in range(number_of_batteries):
            battery_id = f"B{i + 1:03d}"

            # Get cycle-life value
            cycle_life_ref = batch["cycle_life"][i, 0]
            cycle_life = float(f[cycle_life_ref][()][0, 0])

            # Get summary data
            summary_ref = batch["summary"][i, 0]
            summary = f[summary_ref]

            cycles = summary["cycle"][0, :]
            q_charge = summary["QCharge"][0, :]
            q_discharge = summary["QDischarge"][0, :]
            ir = summary["IR"][0, :]
            t_avg = summary["Tavg"][0, :]
            t_max = summary["Tmax"][0, :]
            t_min = summary["Tmin"][0, :]
            charge_time = summary["chargetime"][0, :]

            for j in range(len(cycles)):
                rows.append({
                    "battery_id": battery_id,
                    "cycle": float(cycles[j]),
                    "QCharge": float(q_charge[j]),
                    "QDischarge": float(q_discharge[j]),
                    "IR": float(ir[j]),
                    "Tavg": float(t_avg[j]),
                    "Tmax": float(t_max[j]),
                    "Tmin": float(t_min[j]),
                    "chargetime": float(charge_time[j]),
                    "cycle_life": cycle_life
                })

            print(f"Processed {battery_id}")

    df = pd.DataFrame(rows)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nExtraction complete!")
    print("Rows:", len(df))
    print("Columns:", list(df.columns))
    print("Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    extract_data()