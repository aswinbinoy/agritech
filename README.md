# Nexforz Agritech

A Python project workspace for predicting mushroom yield in a climate-controlled polyhouse.

## Project Brief

The goal of Nexforz Agritech is to predict the daily mushroom yield in kilograms (`kg`) using climate sensor readings from a controlled polyhouse:

- Temperature (`°C`)
- Relative humidity (`%`)
- Carbon dioxide concentration (`ppm`)

The project will use these environmental measurements as model inputs and daily mushroom yield (`kg`) as the prediction target.

## Current Setup

- Operating system: Windows
- Python version: 3.13.9
- Virtual environment: `venv`
- Dependency file: `requirements.txt`
- Smoke test: `test.py`

The current smoke test imports and reports versions for NumPy, pandas, Matplotlib, and scikit-learn. It also prints sample temperature, humidity, and pressure sensor readings.

## Project Structure

```text
agritech/
|-- data/
|   `-- raw/               # Raw input data
|-- models/                # Saved or trained models
|-- notebooks/             # Jupyter notebooks
|-- README.md
|-- requirements.txt
|-- src/                   # Project source code
|-- test.py
|-- .gitignore
`-- venv/                 # Local virtual environment; not committed
```

## Setup on Windows PowerShell

### 1. Create the virtual environment

Run this from the project directory if `venv` does not already exist:

```powershell
python -m venv venv
```

### 2. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current user, run PowerShell as your normal user and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The dependency file was generated from the working environment with:

```powershell
python -m pip freeze > requirements.txt
```

### 4. Run the smoke test

```powershell
python test.py
```

The test should print the sample sensor readings, installed package versions, and `Smoke test passed!`.

### 5. Deactivate the environment

```powershell
deactivate
```

## Development Notes

- Keep project source files outside `venv`.
- Update dependencies after installing or removing packages:

```powershell
python -m pip freeze > requirements.txt
```

- Do not commit the local virtual environment or generated Python cache files.
