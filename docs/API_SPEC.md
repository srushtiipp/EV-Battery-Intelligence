# API Specification

## GET /batteries

Returns available batteries.

## GET /batteries/{battery_id}

Returns current battery state.

Example response:

{
  "battery_id": "B037",
  "current_cycle": 180,
  "soh": 87.4,
  "degradation_rate": 0.0042,
  "risk": "HIGH",
  "cohort_percentile": 95,
  "predicted_cycle_life": 410,
  "prediction_uncertainty": 35
}

## GET /batteries/{battery_id}/history

Returns cycle-level historical data.

## GET /batteries/{battery_id}/prediction

Returns model prediction and uncertainty.

## GET /batteries/{battery_id}/risk

Returns battery risk information.
