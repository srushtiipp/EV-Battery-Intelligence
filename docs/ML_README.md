## Data Cleaning

The extracted dataset initially contained 38,811 rows from 46 batteries.

During cleaning, 46 non-informative rows were removed. These were the first record of each battery and contained zero values for the measured battery parameters such as charge/discharge capacity, internal resistance, temperature, and charge time.

After cleaning, the dataset contains 38,765 rows from 46 batteries.

Validation after cleaning:
- Missing values: 0
- Duplicate rows: 0
- Completely zero measurement rows: 0

Individual zero values in the IR field were retained because the corresponding rows contained other valid measurements. These values were not artificially replaced.