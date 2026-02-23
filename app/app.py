"""
Streamlit App for Nairobi House Prediction

This app provides an interactive interface for predicting house prices in Nairobi.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Nairobi House Price Predictor",
    page_icon="",
    layout="wide"
)

# Load model and encoders
@st.cache_resource
def load_model():
    """Load the trained model and preprocessing objects"""
    model_path = Path('models')
    model = joblib.load(model_path / 'model.pkl')
    scaler = joblib.load(model_path / 'scaler.pkl')
    neighborhood_encoder = joblib.load(model_path / 'neighborhood_encoder.pkl')
    
    with open(model_path / 'model_metadata.json', 'r') as f:
        metadata = json.load(f)
    
    return model, scaler, neighborhood_encoder, metadata

# Prediction function
def predict_price(model, scaler, neighborhood_encoder, 
                  size, bedrooms, bathrooms, 
                  has_backup_generator, has_garden, has_swimming_pool, 
                  has_fibre_internet, has_parking, neighborhood):
    """Make price prediction based on input features"""
    total_rooms = bedrooms + bathrooms
    
    try:
        neighborhood_encoded = neighborhood_encoder.transform([neighborhood])[0]
    except:
        neighborhood_encoded = 0
    
    # Create DataFrame with proper feature names to avoid warning
    feature_names = [
        'Size_Numeric', 'Bedrooms_Numeric', 'Bathrooms', 'Total_Rooms',
        'Has_Backup_Generator', 'Has_Garden', 'Has_Swimming_Pool',
        'Has_Fibre_Internet', 'Has_Parking', 'Neighborhood_Encoded'
    ]
    
    features = pd.DataFrame([[
        size, bedrooms, bathrooms, total_rooms,
        has_backup_generator, has_garden, has_swimming_pool,
        has_fibre_internet, has_parking, neighborhood_encoded
    ]], columns=feature_names)
    
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    
    return prediction


def main():
    """Main function for the Streamlit app"""
    # Load model
    model, scaler, neighborhood_encoder, metadata = load_model()
    
    # Title and description
    st.title(" Nairobi House Price Predictor")
    st.markdown("""
    Get instant price predictions for houses in Nairobi based on property features.
    This model uses **XGBoost** and has an **R² score of {:.2%}**.
    """.format(metadata['test_r2']))
    
    st.divider()
    
    # Input form
    st.header("Property Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Basic Features")
        size = st.slider("Size (sq meters)", 50, 1000, 250, 10)
        bedrooms = st.slider("Bedrooms", 1, 10, 3)
        bathrooms = st.slider("Bathrooms", 1, 10, 2)
    
    with col2:
        st.subheader("Location")
        # Load neighborhoods
        data = pd.read_csv('data/processed/cleaned_listings.csv')
        neighborhoods = sorted(data['Neighborhood'].unique().tolist())
        neighborhood = st.selectbox("Neighborhood", neighborhoods, index=neighborhoods.index('Lavington') if 'Lavington' in neighborhoods else 0)
        
        # Show summary stats
        st.info(f"📍 {len(neighborhoods)} neighborhoods available")
    
    with col3:
        st.subheader("Amenities")
        has_parking = st.checkbox(" Parking", value=True)
        has_garden = st.checkbox(" Garden", value=False)
        has_swimming_pool = st.checkbox(" Swimming Pool", value=False)
        has_backup_generator = st.checkbox(" Backup Generator", value=False)
        has_fibre_internet = st.checkbox(" Fibre Internet", value=True)
    
    st.divider()
    
    # Predict button
    if st.button(" Predict Price", type="primary", width='stretch'):
        with st.spinner("Calculating prediction..."):
            prediction = predict_price(
                model, scaler, neighborhood_encoder,
                size, bedrooms, bathrooms,
                has_backup_generator, has_garden, has_swimming_pool,
                has_fibre_internet, has_parking, neighborhood
            )
        
        # Display results
        st.success(" Prediction Complete!")
        
        # Main metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(" Predicted Price", f"KES {prediction:,.0f}", help="Estimated monthly rent")
        
        with col2:
            price_per_sqm = prediction / size
            st.metric(" Price per sq meter", f"KES {price_per_sqm:,.0f}")
        
        with col3:
            price_per_bedroom = prediction / bedrooms
            st.metric(" Price per bedroom", f"KES {price_per_bedroom:,.0f}")
        
        st.divider()
        
        # Price category
        if prediction < 200000:
            category = " Budget"
            description = "Affordable housing option"
        elif prediction < 400000:
            category = " Mid-Range"
            description = "Good value for money"
        elif prediction < 600000:
            category = " Premium"
            description = "High-end property"
        else:
            category = " Luxury"
            description = "Exclusive luxury property"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"**Price Category:** {category}")
            st.caption(description)
        
        with col2:
            st.info(f"**Model Performance:** R² = {metadata['test_r2']:.2%}")
            st.caption(f"RMSE: KES {metadata['test_rmse']:,.0f}")
        
        # Property summary
        st.subheader(" Property Summary")
        summary_df = pd.DataFrame({
            'Feature': ['Size', 'Bedrooms', 'Bathrooms', 'Total Rooms', 'Neighborhood', 
                       'Parking', 'Garden', 'Pool', 'Generator', 'Fibre Internet'],
            'Value': [
                f"{size} m²", str(bedrooms), str(bathrooms), str(bedrooms + bathrooms), neighborhood,
                '✅' if has_parking else '❌',
                '✅' if has_garden else '❌',
                '✅' if has_swimming_pool else '❌',
                '✅' if has_backup_generator else '❌',
                '✅' if has_fibre_internet else '❌'
            ]
        })
        st.dataframe(summary_df, width='stretch', hide_index=True)
    
    # Footer
    st.divider()
    st.caption(" Nairobi House Price Predictor | Data Fellowship Project 2026")


if __name__ == "__main__":
    main()
