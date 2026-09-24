import pandas as pd
import numpy as np
import matplotlib
import sklearn


sensor = {
    "temperature": 27.5,
    "humidity": 68.2,
    "pressure": 1013.25
}

print("Sensor Readings")
print("-" * 30)

print(f"Temperature : {sensor['temperature']:.2f} °C")
print(f"Humidity    : {sensor['humidity']:.2f} %")
print(f"Pressure    : {sensor['pressure']:.2f} hPa")

print("\nEnvironment check")
print("-" * 30)

print(f"NumPy        : {np.__version__}")
print(f"Pandas       : {pd.__version__}")
print(f"Matplotlib   : {matplotlib.__version__}")
print(f"Scikit-learn : {sklearn.__version__}")

print("\nSmoke test passed!")