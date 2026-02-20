# Data Dictionary

## Nairobi House Prediction Dataset

### Overview
This document describes the features and structure of the dataset used for predicting house prices in Nairobi.

---

## Raw Data

### Source
- **Dataset Name:** Nairobi House Listings
- **Source:** raw_listings.csv (from web scraping of BuyRentKenya)
- **Date Collected:** February 17, 2026
- **Number of Records:** 502 properties
- **Number of Features:** 8
- **Memory Usage:** 0.27 MB

---

## Features

### Target Variable
| Feature Name | Type | Description | Example | Missing Values |
|--------------|------|-------------|---------|----------------|
| Price (KES) | int64 | House price in Kenyan Shillings | 5000000 | 0 (0.0%) |

### Property Features
| Feature Name | Type | Description | Example | Missing Values |
|--------------|------|-------------|---------|----------------|
| Property Type | object | Type of property (house, apartment, etc.) | House, Apartment | 0 (0.0%) |
| Bedrooms | object | Number of bedrooms | 3, 4 | 0 (0.0%) |
| Bathrooms | float64 | Number of bathrooms | 2.0, 3.5 | 16 (3.2%) |
| Size | object | Property size (may include units) | 120 sqm, 1500 sq ft | 240 (47.8%) |

### Location Features
| Feature Name | Type | Description | Example | Missing Values |
|--------------|------|-------------|---------|----------------|
| Location | object | Neighborhood or area in Nairobi | Westlands, Kilimani, Karen | 0 (0.0%) |

### Additional Features
| Feature Name | Type | Description | Example | Missing Values |
|--------------|------|-------------|---------|----------------|
| Listing Date | object | Date when property was listed | 2026-01-15 | 0 (0.0%) |
| Amenities | object | Property amenities and features | Pool, Parking, Garden, Security | 9 (1.8%) |

---

## Data Quality

### Missing Values
- **Total Missing Values:** 265 out of 4,016 values (6.60%)
- **Size:** 240 missing (47.8%) - Major issue, needs investigation
- **Bathrooms:** 16 missing (3.2%) - Can be imputed
- **Amenities:** 9 missing (1.8%) - Minor issue
- **All other features:** Complete data

### Outliers
- [To be investigated in EDA phase]

### Data Issues
- **Size:** Nearly half of the records missing size information - needs special handling
- **Bedrooms:** Stored as object type instead of numeric - requires type conversion
- **Size:** Stored as object with mixed units (sqm vs sq ft) - requires parsing and standardization
- **Listing Date:** Stored as object - needs conversion to datetime
- **Amenities:** Text data that needs parsing into separate features

---

## Processed Data

### New Features Created
| Feature Name | Type | Description | Formula/Method |
|--------------|------|-------------|----------------|
| [Day 2+] | | To be created during feature engineering | |

### Transformations Applied
- [To be documented during data cleaning and feature engineering]

### Planned Transformations
- Convert Bedrooms from object to integer
- Parse Size field and standardize units to square meters
- Convert Listing Date to datetime format
- Parse and encode Amenities as binary features
- Handle missing values in Size and Bathrooms
- Extract useful features from Listing Date (e.g., age of listing)

---

**Last Updated:** February 20, 2026 (Day 1 - Data Collection)
