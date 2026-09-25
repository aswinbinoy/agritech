from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw" / "polyhouse_sensors.csv"
INTERIM = PROJECT_ROOT / "data" / "interim"
INTERIM.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(
    RAW,
    parse_dates=["timestamp"],
    dtype={
        "temperature_c": "float64",
        "humidity_pct": "float64",
        "co2_ppm": "float64",
        "yield_kg": "float64",
    },
)

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nDataFrame info:")
df.info()
print("\nFirst five rows:")
print(df.head())

df.to_parquet(INTERIM / "01_loaded.parquet", index=False)