"""
Interactive Dashboard for Nairobi House Prediction

This dashboard provides visualizations and analytics for the house price prediction project.
"""

import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

# Load data
data = pd.read_csv('data/processed/cleaned_listings.csv')

# Load model artifacts
model_path = Path('models')
model = joblib.load(model_path / 'model.pkl')
scaler = joblib.load(model_path / 'scaler.pkl')
neighborhood_encoder = joblib.load(model_path / 'neighborhood_encoder.pkl')

# Load metrics
model_comparison = pd.read_csv(model_path / 'model_comparison.csv')
feature_importance = pd.read_csv(model_path / 'feature_importance.csv')

with open(model_path / 'model_metadata.json', 'r') as f:
    model_metadata = json.load(f)

# Initialize Dash app
app = dash.Dash(__name__, title='Nairobi House Price Dashboard')

# Define colors
colors = {
    'background': '#f8f9fa',
    'text': '#2c3e50',
    'primary': '#3498db',
    'secondary': '#2ecc71',
    'accent': '#e74c3c'
}

# Create visualizations
def create_price_distribution():
    """Create price distribution histogram"""
    fig = px.histogram(
        data, 
        x='Price (KES)', 
        nbins=50,
        title='Distribution of House Prices in Nairobi',
        color_discrete_sequence=[colors['primary']]
    )
    fig.update_layout(
        xaxis_title='Price (KES)',
        yaxis_title='Count',
        template='plotly_white',
        height=400
    )
    return fig

def create_feature_importance():
    """Create feature importance chart"""
    fig = px.bar(
        feature_importance.sort_values('Importance', ascending=True).tail(10),
        y='Feature',
        x='Importance',
        orientation='h',
        title='Top 10 Most Important Features',
        color='Importance',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        showlegend=False,
        template='plotly_white',
        height=400
    )
    return fig

def create_model_comparison():
    """Create model comparison chart"""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=model_comparison['Model'],
        y=model_comparison['Test R²'],
        name='Test R²',
        marker_color=colors['secondary']
    ))
    fig.update_layout(
        title='Model Performance Comparison (R² Score)',
        xaxis_title='Model',
        yaxis_title='R² Score',
        template='plotly_white',
        height=400
    )
    return fig

def create_neighborhood_analysis():
    """Create neighborhood analysis chart"""
    neighborhood_stats = data.groupby('Neighborhood').agg({
        'Price (KES)': ['mean', 'count']
    }).reset_index()
    neighborhood_stats.columns = ['Neighborhood', 'Avg_Price', 'Count']
    neighborhood_stats = neighborhood_stats[neighborhood_stats['Count'] >= 3]
    top_neighborhoods = neighborhood_stats.nlargest(15, 'Avg_Price')
    
    fig = px.bar(
        top_neighborhoods,
        x='Avg_Price',
        y='Neighborhood',
        orientation='h',
        title='Top 15 Neighborhoods by Average Price',
        color='Avg_Price',
        color_continuous_scale='RdYlGn_r'
    )
    fig.update_layout(
        template='plotly_white',
        height=500
    )
    return fig

def create_amenities_impact():
    """Create amenities impact chart"""
    amenity_cols = ['Has_Parking', 'Has_Swimming_Pool', 'Has_Gym', 'Has_Garden', 
                    'Has_CCTV', 'Has_Backup_Generator', 'Has_Fibre_Internet', 'Has_Gated_Community']
    
    amenity_prices = []
    for col in amenity_cols:
        avg_with = data[data[col] == 1]['Price (KES)'].mean()
        avg_without = data[data[col] == 0]['Price (KES)'].mean()
        amenity_prices.append({
            'Amenity': col.replace('Has_', '').replace('_', ' '),
            'With Amenity': avg_with,
            'Without Amenity': avg_without
        })
    
    amenity_df = pd.DataFrame(amenity_prices)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='With Amenity',
        x=amenity_df['Amenity'],
        y=amenity_df['With Amenity'],
        marker_color='lightgreen'
    ))
    fig.add_trace(go.Bar(
        name='Without Amenity',
        x=amenity_df['Amenity'],
        y=amenity_df['Without Amenity'],
        marker_color='lightcoral'
    ))
    
    fig.update_layout(
        title='Average Price by Amenity',
        xaxis_title='Amenity',
        yaxis_title='Average Price (KES)',
        barmode='group',
        template='plotly_white',
        height=450
    )
    return fig

def create_scatter_plot(bedroom_filter=None):
    """Create price vs size scatter plot"""
    if bedroom_filter and bedroom_filter != 'All':
        filtered_data = data[data['Bedrooms_Numeric'] == int(bedroom_filter)]
    else:
        filtered_data = data
    
    fig = px.scatter(
        filtered_data,
        x='Size_Numeric',
        y='Price (KES)',
        color='Bedrooms_Numeric',
        size='Total_Amenities',
        hover_data=['Neighborhood', 'Property Type'],
        title='Price vs Size (filtered by Bedrooms)',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        template='plotly_white',
        height=500
    )
    return fig

# Calculate key metrics
total_properties = len(data)
avg_price = data['Price (KES)'].mean()
median_price = data['Price (KES)'].median()
total_neighborhoods = data['Neighborhood'].nunique()

# Layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # Header
    html.Div([
        html.H1('🏠 Nairobi House Price Dashboard', 
                style={'textAlign': 'center', 'color': colors['text'], 'padding': '20px'}),
        html.P('Interactive Analytics for House Price Prediction Project',
               style={'textAlign': 'center', 'color': colors['text'], 'fontSize': '18px'})
    ]),
    
    # Key Metrics
    html.Div([
        html.Div([
            html.Div([
                html.H3(f'{total_properties}', style={'color': colors['primary'], 'margin': '0'}),
                html.P('Total Properties', style={'margin': '0'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                     'borderRadius': '5px', 'margin': '10px', 'flex': '1'}),
            
            html.Div([
                html.H3(f'KES {avg_price:,.0f}', style={'color': colors['secondary'], 'margin': '0'}),
                html.P('Average Price', style={'margin': '0'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                     'borderRadius': '5px', 'margin': '10px', 'flex': '1'}),
            
            html.Div([
                html.H3(f'KES {median_price:,.0f}', style={'color': colors['accent'], 'margin': '0'}),
                html.P('Median Price', style={'margin': '0'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                     'borderRadius': '5px', 'margin': '10px', 'flex': '1'}),
            
            html.Div([
                html.H3(f'{total_neighborhoods}', style={'color': colors['primary'], 'margin': '0'}),
                html.P('Neighborhoods', style={'margin': '0'})
            ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': 'white', 
                     'borderRadius': '5px', 'margin': '10px', 'flex': '1'}),
        ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'}),
    ]),
    
    # Model Performance Section
    html.Div([
        html.H2('📊 Model Performance', style={'color': colors['text'], 'padding': '20px'}),
        html.Div([
            html.Div([
                dcc.Graph(figure=create_model_comparison())
            ], style={'flex': '1', 'padding': '10px'}),
            
            html.Div([
                dcc.Graph(figure=create_feature_importance())
            ], style={'flex': '1', 'padding': '10px'}),
        ], style={'display': 'flex'}),
    ], style={'backgroundColor': 'white', 'margin': '20px', 'borderRadius': '5px'}),
    
    # Price Analysis Section
    html.Div([
        html.H2('💰 Price Analysis', style={'color': colors['text'], 'padding': '20px'}),
        html.Div([
            html.Div([
                dcc.Graph(figure=create_price_distribution())
            ], style={'flex': '1', 'padding': '10px'}),
            
            html.Div([
                dcc.Graph(figure=create_neighborhood_analysis())
            ], style={'flex': '1', 'padding': '10px'}),
        ], style={'display': 'flex'}),
    ], style={'backgroundColor': 'white', 'margin': '20px', 'borderRadius': '5px'}),
    
    # Amenities Impact Section
    html.Div([
        html.H2('🏊 Amenities Impact', style={'color': colors['text'], 'padding': '20px'}),
        dcc.Graph(figure=create_amenities_impact())
    ], style={'backgroundColor': 'white', 'margin': '20px', 'borderRadius': '5px', 'padding': '20px'}),
    
    # Interactive Scatter Plot Section
    html.Div([
        html.H2('🔍 Interactive Analysis', style={'color': colors['text'], 'padding': '20px'}),
        html.Div([
            html.Label('Filter by Bedrooms:', style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='bedroom-filter',
                options=[{'label': 'All', 'value': 'All'}] + 
                        [{'label': f'{i} Bedrooms', 'value': str(i)} 
                         for i in sorted(data['Bedrooms_Numeric'].unique())],
                value='All',
                style={'width': '200px'}
            )
        ], style={'padding': '20px'}),
        dcc.Graph(id='scatter-plot')
    ], style={'backgroundColor': 'white', 'margin': '20px', 'borderRadius': '5px', 'padding': '20px'}),
    
    # Footer
    html.Div([
        html.P(f'Dashboard | Model: {model_metadata["model_type"]} | R² Score: {model_metadata["test_r2"]:.2%} | Data Fellowship Project 2026',
               style={'textAlign': 'center', 'color': colors['text'], 'padding': '20px'})
    ])
])

# Callback for interactive scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('bedroom-filter', 'value')
)
def update_scatter_plot(bedroom_filter):
    return create_scatter_plot(bedroom_filter)


def main():
    """Run the dashboard"""
    app.run(debug=True, host='0.0.0.0', port=8050)


if __name__ == "__main__":
    main()
