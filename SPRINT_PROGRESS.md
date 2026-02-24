# Sprint Progress Tracker

## Project: Nairobi House Prediction
**Start Date:** 16/02/2026 
**End Date:** 22/02/2026  
Shadrack Kimaau

---

##  Overall Progress

- [x] Day 1: Data Collection
- [x] Day 2: Data Cleaning & Feature Engineering
- [x] Day 3: EDA & Baseline Models
- [x] Day 4: Model Improvement
- [x] Day 5: App Preparation
- [x] Day 6: Dashboard & Deployment

---

## Day 1: Data Collection
**Date:** 16/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Identify data sources
- [x] Download/collect raw data
- [x] Initial data inspection
- [x] Document data sources

### Deliverables
- [x] Completed notebook: `day1_data_collection.ipynb`
- [x] Raw data in `data/raw/raw_listings.csv`
- [x] Data dictionary started

### Notes
- Successfully scraped house listing data from real estate website
- Collected 1000+ property listings from Nairobi
- Initial dataset contains: price, bedrooms, bathrooms, location, size, and additional features
- Data stored in CSV format for further processing

---

## Day 2: Data Cleaning & Feature Engineering
**Date:** 17/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Handle missing values
- [x] Remove duplicates
- [x] Feature encoding
- [x] Create new features
- [x] Data validation

### Deliverables
- [x] Completed notebook: `day2_cleaning_feature_eng.ipynb`
- [x] Processed data in `data/processed/cleaned_listings.csv`
- [x] Feature engineering module in `src/`

### Notes
- Handled missing values using appropriate strategies (median for numerical, mode for categorical)
- Removed duplicate listings
- Encoded categorical features (Neighborhood, Property_Type, Furnishing_Status)
- Created new features: Price_Per_Bedroom, Has_Pool, Has_Garden, Has_Parking
- Cleaned and validated all data fields
- Final dataset ready for modeling with 900+ clean records

---

## Day 3: EDA & Baseline Models
**Date:** 18/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Statistical analysis
- [x] Data visualizations
- [x] Correlation analysis
- [x] Train baseline models
- [x] Evaluate baseline performance

### Deliverables
- [x] Completed notebook: `day3_eda_baseline.ipynb`
- [x] Baseline model saved in `models/`
- [x] Performance metrics documented

### Notes
- Comprehensive EDA with distribution analysis, correlation heatmaps, and feature relationships
- Key finding: Neighborhood and Bedrooms are strong price predictors
- Trained Linear Regression as baseline model
- Baseline R² score: ~0.25 (25% variance explained)
- Identified need for more complex models to capture non-linear relationships

---

## Day 4: Model Improvement
**Date:** 19/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Feature selection
- [x] Advanced model training
- [x] Model comparison
- [x] Final model selection
- [x] Performance evaluation

### Deliverables
- [x] Completed notebook: `day4_model_improvement.ipynb`
- [x] Multiple models trained and saved
- [x] Model comparison report with metrics
- [x] Feature importance analysis

### Notes
- Trained three models: Linear Regression (baseline), Random Forest, and XGBoost
- Best model: XGBoost with ~40% R² score (improvement from baseline)
- Feature importance: Neighborhood, Bedrooms, and Size_SqM are top predictors
- Acknowledged model limitations: 40% R² indicates overfitting and noisy data
- Project goal is end-to-end completion, not perfect accuracy
- Model saved for deployment despite moderate performance

---

## Day 5: App Preparation
**Date:** 20/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Design app interface structure
- [x] Created app.py template
- [x] Implement prediction function
- [x] Add input validation
- [x] Test app locally
- [x] Complete documentation

### Deliverables
- [x] Notebook: `day5_app_prep.ipynb`
- [x] Streamlit app structure in `app/app.py`
- [x] Fully functional app (188 lines of code)

### Notes
- App structure designed with Streamlit framework
- Implemented complete user input form with all property features
- Added prediction function with model loading and preprocessing
- Included input validation and error handling
- App successfully predicts house prices based on user inputs

---

## Day 6: Dashboard & Deployment
**Date:** 21-22/02/2026  
**Status:** ✅ Completed

### Tasks
- [x] Create interactive dashboard
- [x] Add visualizations
- [x] Prepare presentation
- [x] Final testing
- [x] Documentation completion

### Deliverables
- [x] Completed notebook: `day6_dashboard_prep.ipynb`
- [x] Interactive dashboard in `dashboard/dashboard.py` (311 lines)
- [x] Presentation materials ready
- [x] Complete documentation (README, QUICKSTART, DASHBOARD_DEPLOYMENT)

### Notes
- Built interactive Dash dashboard with multiple visualizations
- Implemented price distribution, correlation heatmap, and feature importance charts
- Added model performance metrics display
- Included data exploration tools and interactive filters
- Created comprehensive documentation for setup and deployment
- Prepared presentation outline with project workflow


---

## Challenges & Solutions

### Challenges Encountered

1. **Web Scraping (Biggest Challenge)**
   - Had to learn web scraping from scratch while implementing the project
   - Multiple failed attempts before understanding the concepts properly
   - Used bad practices initially (no rate limiting, too aggressive requests)
   - Got my IP blocked by the website due to improper scraping techniques
   - Struggled with parsing HTML structure and extracting data correctly

2. **Data Quality Issues**
   - Significant amount of missing values in scraped data
   - Inconsistent formatting across different listings
   - Required extensive cleaning and validation

3. **Model Performance**
   - Initial baseline model had very poor performance (~25% R²)
   - Difficulty in capturing complex relationships with simple models
   - Limited feature set affecting model accuracy

4. **Time Management**
   - Balancing learning new concepts with project deadlines
   - Each day's objectives were ambitious and required focused effort

### Solutions Implemented

1. **Web Scraping Best Practices**
   - Researched and learned proper web scraping ethics and techniques
   - Implemented rate limiting and delays between requests
   - Added user-agent headers and respectful request patterns
   - Used proper error handling and retry mechanisms
   - Successfully collected 1000+ listings without further IP blocks

2. **Data Cleaning Strategy**
   - Developed systematic approach for handling missing values
   - Removed duplicates and outliers systematically

3. **Model Improvement Approach**
   - Tried multiple algorithms (Linear Regression, Random Forest, XGBoost)
   - Focused on feature engineering to improve predictive power
   - Accepted model limitations and focused on completing the pipeline

4. **Structured Workflow**
   - Created daily notebooks to track progress systematically
   - Used modular code in `src/` folder for reusability
   - Maintained detailed documentation throughout

---

## Key Learnings

### Technical Skills Applied

1. **Transferring Classroom Knowledge to Real-World Projects**
   - Successfully applied theoretical ML concepts to practical problem
   - Bridged the gap between learning and implementation - incredibly exciting!
   - Realized that real projects require more than just knowing algorithms

2. **Web Scraping & Data Collection**
   - Learned ethical web scraping practices the hard way
   - Importance of respecting website rate limits and robots.txt
   - Data collection is often the hardest part of ML projects

3. **Data Cleaning is Critical**
   - Real-world data is messy and requires extensive preprocessing
   - 80% of the work is data preparation, 20% is modeling
   - Good data quality directly impacts model performance

4. **Feature Engineering Matters**
   - Creating meaningful features significantly improves models
   - Domain knowledge (real estate) helps in feature creation
   - Simple features like Price_Per_Bedroom can be highly informative

5. **Model Selection & Evaluation**
   - Tree-based models (Random Forest, XGBoost) work better for tabular data
   - Linear models struggle with non-linear relationships
   - Proper train-test split is essential for honest evaluation

6. **Project Management**
   - Breaking down complex projects into daily goals helps maintain progress
   - Documentation throughout the project saves time later
   - Completing the full pipeline is more valuable than perfect accuracy

7. **Realistic Expectations**
   - Not all ML projects achieve high accuracy, and that's okay
   - Model limitations should be acknowledged transparently
   - The learning process and technical skills gained are the real value

### Personal Growth

- **Confidence Boost:** Successfully completing an end-to-end ML project independently
- **Problem-Solving:** Learning to debug and fix issues autonomously
- **Resilience:** Overcoming the IP blocking setback and continuing forward
- **Practical Experience:** Hands-on practice that complements theoretical knowledge

---

## Project Completion

✅ **All Sprint Goals Achieved!**

- ✅ Data Collection: Successfully scraped 1000+ listings
- ✅ Data Processing: Cleaned and engineered features
- ✅ Modeling: Trained and evaluated multiple models
- ✅ Application: Built fully functional Streamlit prediction app
- ✅ Dashboard: Created interactive Dash analytics dashboard
- ✅ Documentation: Comprehensive guides and documentation complete

### Potential Future Enhancements
- Deploy application to cloud platform (Streamlit Cloud, Heroku, or AWS)
- Collect more data to improve model accuracy
- Add more advanced features (property age, proximity to amenities)
- Implement CI/CD pipeline for automated testing and deployment
- Add user feedback mechanism to continuously improve predictions

---

## Author

**Shadrack Kimaau**  
GitHub: [shadrack-kimaau](https://github.com/shadrack-kimaau)

---

**Last Updated:** 24/02/2026
