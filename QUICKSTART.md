# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Installation

### 1. Clone/Navigate to Project Directory
```bash
cd "LT Data Fellowship/Nairobi House Prediction"
```

### 2. Set Up Environment
```bash
# Run setup script
bash setup.sh
```

Or manually:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import pandas; import numpy; import sklearn; print('All packages installed successfully!')"
```

## Project Workflow

### Phase 1: Data Collection (Day 1)
- Run `notebooks/day1_data_collection.ipynb`

### Phase 2: Data Cleaning (Day 2)
- Run `notebooks/day2_cleaning_feature_eng.ipynb`

### Phase 3: EDA & Modeling (Day 3-4)
- Run `notebooks/day3_eda_baseline.ipynb`
- Run `notebooks/day4_model_improvement.ipynb`

### Phase 4: Application Development (Day 5-6)
- Run `notebooks/day5_app_prep.ipynb`
- Run `notebooks/day6_dashboard_prep.ipynb`

## Running the Application

### Streamlit App
```bash
streamlit run app/app.py
```

### Dashboard
```bash
python dashboard/dashboard.py
```

## Troubleshooting
- If packages fail to install, try upgrading pip: `pip install --upgrade pip`
- For import errors, ensure virtual environment is activated
- Check Python version: `python --version`

## Next Steps
See [SPRINT_PROGRESS.md](SPRINT_PROGRESS.md) for daily tasks and progress tracking.
