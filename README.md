# Nairobi House Prediction

## Project Overview
An end-to-end machine learning project that predicts house prices in Nairobi, Kenya. This project demonstrates the complete ML workflow from web scraping and data collection to model training and deployment preparation.

**Goal:** Build a complete predictive system to estimate house prices based on property features (bedrooms, bathrooms, location, size, amenities).

**Focus:** This project emphasizes completing the full ML pipeline rather than achieving perfect accuracy, providing valuable learning experience across all stages of a data science project.

## Key Features
-  **Real-world data** scraped from Nairobi real estate listings
-  **Comprehensive data cleaning** and feature engineering
-  **Exploratory Data Analysis** with insightful visualizations
-  **Multiple ML models** trained and compared (Linear Regression, Random Forest, XGBoost)
-  **Model evaluation** with proper metrics and performance analysis
-  **App preparation** for deployment with Streamlit

## Project Structure
```
Nairobi House Prediction/
├── app/                           # Streamlit application
│   └── app.py                    # Main app file (template)
├── dashboard/                     # Interactive dashboard
│   └── dashboard.py              # Dashboard code
├── data/                          # Data storage
│   ├── raw/                      # Raw scraped data
│   │   └── raw_listings.csv      # Original listings
│   └── processed/                # Cleaned data
│       └── cleaned_listings.csv  # Ready for modeling
├── models/                        # Trained models
│   ├── baseline_model_metadata.json
│   ├── model_metadata.json
│   ├── model_comparison.csv
│   └── feature_importance.csv
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
├── config.yaml                    # Configuration file
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Technical Stack
- **Python 3.8+**
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Web Framework:** Streamlit (for app)
- **Data Collection:** BeautifulSoup/Selenium for web scraping

## Project Workflow

### Day 1: Data Collection 
- Scraped 1000+ house listings from Nairobi real estate websites
- Collected features: price, bedrooms, bathrooms, location, size, amenities
- Created data dictionary and stored raw data

### Day 2: Data Cleaning & Feature Engineering 
- Handled missing values (median for numerical, mode for categorical)
- Removed duplicate listings
- Encoded categorical features (Neighborhood, Property_Type, Furnishing_Status)
- Created new features: Price_Per_Bedroom, Has_Pool, Has_Garden, Has_Parking
- Final cleaned dataset: 900+ records

### Day 3: Exploratory Data Analysis & Baseline Model 
- Statistical analysis and distribution plots
- Correlation analysis identifying key price drivers
- Trained Linear Regression baseline model
- Baseline performance: R² ≈ 0.25 (25% variance explained)

### Day 4: Model Improvement 
- Trained advanced models: Random Forest and XGBoost
- Compared model performance across different algorithms
- Best model: XGBoost with R² ≈ 0.40 (40% variance explained)
- Feature importance analysis showed Neighborhood and Bedrooms as top predictors
- Saved models and metadata for deployment

**Model Performance Note:**
The 40% R² score indicates our model explains 40% of price variance. While below ideal, this reflects data quality challenges and missing features. The project continues to demonstrate the complete ML workflow and deployment process.

### Day 5: App Preparation 
- Designed Streamlit app structure
- Created app template with planned features
- Prepared prediction function framework
- Status: In progress

### Day 6: Dashboard & Deployment 
- Interactive dashboard creation (planned)
- Final testing and documentation
- Status: Not started

## Model Performance

| Model | R² Score | MAE | RMSE | Notes |
|-------|----------|-----|------|-------|
| Linear Regression | ~0.25 | High | High | Baseline model |
| Random Forest | ~0.38 | Medium | Medium | Good improvement |
| XGBoost | ~0.40 | Lower | Lower | Best performance |

**Top Features by Importance:**
1. Neighborhood (Location)
2. Bedrooms
3. Size_SqM
4. Bathrooms
5. Property_Type

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

### Running the App (Once Complete)
```bash
streamlit run app/app.py
```

## Key Learnings & Insights
- Real-world data often requires extensive cleaning and feature engineering
- Tree-based models (Random Forest, XGBoost) significantly outperform linear models for this problem
- Location (Neighborhood) is the strongest predictor of house prices in Nairobi
- Model performance is limited by data quality and missing important features
- End-to-end project completion is valuable even with moderate model accuracy

## Documentation
- [INDEX.md](INDEX.md) - Project navigation and organization guide
- [SPRINT_PROGRESS.md](SPRINT_PROGRESS.md) - Detailed day-by-day progress tracking
- [QUICKSTART.md](QUICKSTART.md) - Setup and installation guide
- [data/data_dictionary.md](data/data_dictionary.md) - Data field descriptions

## Future Improvements
- Collect more comprehensive data (house condition, exact coordinates, market trends)
- Implement hyperparameter tuning for better performance
- Add more feature engineering (neighborhood demographics, distance to amenities)
- Complete Streamlit app with full functionality
- Deploy to cloud platform (Heroku, Streamlit Cloud, AWS)
- Build interactive dashboard with Plotly

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

**Project Duration:** 16/02/2026 - 22/02/2026  
**Last Updated:** 21/02/2026
