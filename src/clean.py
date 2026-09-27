from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INTERIM = PROJECT_ROOT / "data" / "interim"
INPUT_PATH = INTERIM / "01_loaded.parquet"
OUTPUT_PATH = INTERIM / "02_cleaned.parquet"

df = pd.read_parquet(INPUT_PATH)

# Missing report
print("Missing values before cleaning:")
print(df.isna().sum())

# Valid ranges for oyster polyhouse
rules = {
    "humidity_pct": "50 <= humidity_pct <= 100",
    "temperature_c": "10 <= temperature_c <= 35",
    "co2_ppm": "400 <= co2_ppm <= 2000",
    "yield_kg": "yield_kg is not null",
}
print("\nValidation rules:")
for column, rule in rules.items():
    print(f"- {column}: {rule}")

valid = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
    & df["yield_kg"].notna()
)
df = df[valid].copy()

# Short gap: forward-fill sensor columns only
cols = ["temperature_c", "humidity_pct", "co2_ppm"]
df[cols] = df[cols].ffill(limit=2)

# Drop remaining rows with null target
df = df.dropna(subset=["yield_kg"])

# Duplicates by timestamp
df = df.drop_duplicates(subset=["timestamp"], keep="last")

df.to_parquet(OUTPUT_PATH, index=False)
print(f"\nClean rows: {len(df)}")
print(f"Duplicate timestamps remaining: {df.duplicated(subset=['timestamp']).sum()}")
print(f"Null target values remaining: {df['yield_kg'].isna().sum()}")
print(f"Saved cleaned snapshot: {OUTPUT_PATH}")