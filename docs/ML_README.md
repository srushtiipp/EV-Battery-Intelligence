# EV Battery Intelligence - Data & ML

## Dataset

Source: Severson battery dataset.

The extracted dataset contains 46 batteries.

The cleaned battery data is stored in:

`data/processed/battery_clean.csv`

The engineered battery-level features are stored in:

`data/processed/battery_features.csv`

## Feature Engineering

Early-life behavior from the first 100 cycles was used to create battery-level features.

Features used by the model:

- `capacity_mean_100`
- `capacity_at_100`
- `capacity_min_100`
- `ir_mean_100`
- `temp_mean_100`
- `temp_max_100`
- `charge_time_mean_100`
- `capacity_drop`

The prediction target is:

- `cycle_life`

`cycle_life` is not used as an input feature.

## Model

Current working model:

**Linear Regression**

The trained model is saved at:

`models/cycle_life_linear_model.pkl`

## Evaluation

The dataset was split into:

- 36 training batteries
- 10 testing batteries

Random state:

`42`

Results:

- MAE: 119.34 cycles
- RMSE: 136.50 cycles
- R2: 0.571

## Prediction Output

Predictions for all 46 batteries are stored in:

`data/processed/predictions.csv`

The prediction script is:

`src/predict_cycle_life.py`

Run it with:

```bash
python src/predict_cycle_life.py

