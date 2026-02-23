# Nairobi House Prediction

## Project Overview
An end-to-end machine learning project that predicts house prices in Nairobi, Kenya. This project demonstrates the complete ML workflow from web scraping and data collection to model training and deployment preparation.

**Goal:** Build a complete predictive system to estimate house prices based on property features (bedrooms, bathrooms, location, size, amenities).

**Focus:** This project emphasizes completing the full ML pipeline rather than achieving perfect accuracy, providing valuable learning experience across all stages of a data science project.

**Status:** ✅ **COMPLETED** - All 6 phases finished with working applications!

## Live Applications

- **Prediction App:** [nairobi-house-prediction.streamlit.app](https://nairobi-house-prediction.streamlit.app/) - Interactive price prediction tool
- **Analytics Dashboard:** Coming soon on Render - Comprehensive data visualizations

## Key Features
- Real-world data scraped from Nairobi real estate listings (460+ properties analyzed)
- Comprehensive data cleaning and feature engineering (37 features created)
- Exploratory Data Analysis with insightful visualizations
- Multiple ML models trained and compared (Linear Regression, Random Forest, XGBoost)
- Model evaluation with proper metrics and performance analysis (R² = 41%, +278% improvement)
- Complete Streamlit app and Plotly Dash dashboard for deployment
- Full documentation and deployment guides

## Project Structure
```
Nairobi House Prediction
├── app/                           # Streamlit application
│   └── app.py                    # Main app file
├── dashboard/                     # Interactive dashboard
│   └── dashboard.py              # Dashboard code
├── data/                          # Data storage
│   ├── raw/                      # Raw scraped data
│   │   └── raw_listings.csv      # Original listings
│   └── processed/                # Cleaned data
│       └── cleaned_listings.csv  # Ready for modeling
├── models/                        # Trained models
│   ├── model.pkl                 # XGBoost model (R² = 41%)
│   ├── scaler.pkl                # Feature scaler
│   ├── neighborhood_encoder.pkl  # Label encoder
│   ├── model_metadata.json       # Model performance metrics
│   ├── model_comparison.csv      # All models comparison
│   └── feature_importance.csv    # Feature rankings
├── notebooks/                     # Analysis notebooks
│   ├── day1_data_collection.ipynb
│   ├── day2_cleaning_feature_eng.ipynb
│   ├── day3_eda_baseline.ipynb
│   ├── day4_model_improvement.ipynb
│   ├── day5_app_prep.ipynb
│   └── day6_dashboard_prep.ipynb
├── src/                           # Source code modules
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   └── utils.py
├── scripts/                       # Utility scripts
│   └── scraper.py                # Web scraping script
├── presentation/                  # Presentation materials
├── Procfile                       # Deployment configuration
├── DASHBOARD_DEPLOYMENT.md        # Dashboard deployment guide
├── config.yaml                    # Configuration file
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Technical Stack
- **Python 3.12+**
- **Data Processing:** Pandas, NumPy, SciPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Machine Learning:** Scikit-learn, XGBoost, LightGBM
- **Web Frameworks:** Streamlit (prediction app), Dash (analytics dashboard)
- **Deployment:** Streamlit Cloud, Render, Gunicorn
- **Data Collection:** BeautifulSoup/Selenium for web scraping

## Project Workflow

### Day 1: Data Collection ✅
- Scraped 460+ house listings from Nairobi real estate websites
- Collected features: price, bedrooms, bathrooms, location, size, amenities
- Created data dictionary and stored raw data

### Day 2: Data Cleaning & Feature Engineering ✅
- Handled missing values (median for numerical, mode for categorical)
- Removed duplicate listings
- Encoded categorical features (Neighborhood, Property_Type)
- Created new features: Price_Per_SqM, Total_Rooms, Luxury_Score, Size_Category
- Final cleaned dataset: 460 records with 37 features

### Day 3: Exploratory Data Analysis & Baseline Model ✅
- Statistical analysis and distribution plots
- Correlation analysis identifying key price drivers
- Trained Linear Regression baseline model
- Baseline performance: R² = 0.109 (11% variance explained)

### Day 4: Model Improvement ✅
- Trained advanced models: Random Forest and XGBoost
- Compared model performance across different algorithms
- Best model: **XGBoost with R² = 0.411** (41% variance explained)
- Feature importance analysis: Size, Bedrooms, and Neighborhood as top predictors
- Saved models and metadata for deployment
- **+278% improvement over baseline!**

### Day 5: App Preparation ✅
- Created complete Streamlit app with interactive UI
- Implemented prediction function with input validation
- Built responsive interface with sliders, dropdowns, and checkboxes
- Added price categorization (Budget/Mid-Range/Premium/Luxury)
- Tested successfully with multiple scenarios
- **Status: Complete and tested locally**

### Day 6: Dashboard & Deployment ✅
- Created Plotly Dash dashboard with 8 visualizations:
  - Price distribution analysis
  - Feature importance charts
  - Model performance comparison
  - Neighborhood price analysis
  - Amenities impact visualization
  - Interactive scatter plots with filters
  - Correlation heatmaps
- Prepared deployment files (Procfile, requirements.txt)
- Tested dashboard locally
- **Status: Complete and deployment-ready**

## Model Performance

| Model | R² Score | MAE (KES) | RMSE (KES) | Notes |
|-------|----------|-----------|------------|-------|
| Linear Regression | 0.109 | 123,957 | 159,024 | Baseline model |
| Random Forest | 0.385 | 98,438 | 132,138 | Good improvement |
| **XGBoost** | **0.411** | **92,576** | **129,245** | **Best performance**  |

**Key Metrics:**
- **R² Score:** 0.411 (explains 41% of price variance)
- **RMSE:** KES 129,245 (average prediction error)
- **MAE:** KES 92,576 (mean absolute error)
- **Improvement:** +278% over baseline R²

**Top Features by Importance:**
1. Size_Numeric (Property size)
2. Bedrooms_Numeric
3. Neighborhood_Encoded (Location)
4. Total_Rooms
5. Bathrooms
6. Has_Backup_Generator
7. Has_Garden
8. Has_Swimming_Pool

## Getting Started

### Prerequisites
```bash
Python 3.8+
pip or conda
```

### Installation
```bash
# Clone repository
cd "Nairobi House Prediction"

# Install dependencies
pip install -r requirements.txt

# Or use setup script
bash setup.sh
```

### Quick Start
See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

## Usage

### Training Models
```python
# Run notebooks in order
jupyter notebook notebooks/day1_data_collection.ipynb
jupyter notebook notebooks/day2_cleaning_feature_eng.ipynb
jupyter notebook notebooks/day3_eda_baseline.ipynb
jupyter notebook notebooks/day4_model_improvement.ipynb
```

### Running the Applications

**Streamlit Prediction App:**
```bash
streamlit run app/app.py
# Opens at http://localhost:8501
```

**Plotly Dash Dashboard:**
```bash
python dashboard/dashboard.py
# Opens at http://localhost:8050
```

### Deployment

**Streamlit App (Streamlit Cloud):**
- Already deployed at [nairobi-house-prediction.streamlit.app](https://nairobi-house-prediction.streamlit.app/)
- See [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud/get-started)

**Dash Dashboard (Render/Heroku):**
- See [DASHBOARD_DEPLOYMENT.md](DASHBOARD_DEPLOYMENT.md) for detailed instructions
- Supports Render, Heroku, and Railway platforms

## Key Learnings & Insights
- **Data Quality:** Real-world data requires extensive cleaning and feature engineering
- **Model Selection:** Tree-based models (Random Forest, XGBoost) significantly outperform linear models
- **Feature Impact:** Property size, bedrooms, and location are the strongest price predictors
- **Amenities Value:** Backup generator (+KES 80K), garden (+KES 79K), and pool (+KES 42K) increase prices significantly
- **Neighborhood Effect:** Lake View, Lavington, and Kitisuru command premium prices
- **Deployment:** Building production-ready apps requires careful error handling and user experience design
- **Workflow:** End-to-end project completion from scraping to deployment provides comprehensive ML experience

## Documentation
- [INDEX.md](INDEX.md) - Project navigation and organization guide
- [SPRINT_PROGRESS.md](SPRINT_PROGRESS.md) - Detailed day-by-day progress tracking
- [QUICKSTART.md](QUICKSTART.md) - Setup and installation guide
- [DASHBOARD_DEPLOYMENT.md](DASHBOARD_DEPLOYMENT.md) - Dashboard deployment instructions
- [data/data_dictionary.md](data/data_dictionary.md) - Data field descriptions
- [models/README.md](models/README.md) - Model artifacts documentation

## Future Improvements
- [ ] Collect more comprehensive data (house condition, exact coordinates, historical prices)
- [ ] Implement advanced hyperparameter tuning (Optuna, GridSearch)
- [ ] Add geospatial features (distance to amenities, coordinates-based analysis)
- [ ] Create map visualizations with property locations
- [ ] Implement model monitoring and retraining pipeline
- [ ] Add user authentication for saved predictions
- [ ] Build API endpoint for programmatic access
- [ ] Integrate live data scraping and automatic updates

## Contributing
This is a learning project. Feel free to fork and experiment with your own improvements!

## License
This project is for educational and practice purposes.

## Author

**Shadrack Kimaau**  
GitHub: [shadrack-kimaau](https://github.com/shadrack-kimaau)

## Acknowledgments
- LT Data Fellowship Program
- BuyRentKenya for data inspiration
- Open-source ML community

---

## Project Statistics
- **Total Properties Analyzed:** 460
- **Neighborhoods Covered:** 34
- **Features Engineered:** 37
- **Models Trained:** 3
- **Best Model R²:** 41.1%
- **Code Lines:** 2000+
- **Notebooks:** 6
- **Applications Built:** 2

**Project Duration:** 16/02/2026 - 23/02/2026  
**Status:** ✅ COMPLETE  
**Last Updated:** 23/02/2026
