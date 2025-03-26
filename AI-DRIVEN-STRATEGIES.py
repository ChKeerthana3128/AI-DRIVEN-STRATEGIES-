import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="Cerenti AI Solutions Dashboard", layout="wide", initial_sidebar_state="expanded")

# Header with branding
st.title("Cerneti AI Solutions Dashboard")
st.markdown("""
Welcome, Cerneti team! This interactive dashboard showcases how AI can transform your operations:
- **Dynamic Pricing**: Optimize revenue with real-time pricing.
- **24/7 Chatbots**: Enhance customer service while cutting costs.
- **Predictive Maintenance**: Reduce downtime with proactive asset care.
""")

# Sidebar for global settings
st.sidebar.title("Cerneti Control Panel")
currency = st.sidebar.selectbox("Currency", ["USD ($)", "EUR (€)", "GBP (£)"], index=0)
business_unit = st.sidebar.selectbox("Business Unit", ["Hotel Operations", "Taxi Fleet", "Facility Management"], index=0)

# Currency symbol mapping
currency_symbol = {"USD ($)": "$", "EUR (€)": "€", "GBP (£)": "£"}[currency]

# --- Section 1: AI-Powered Dynamic Pricing ---
st.header("1. AI-Powered Dynamic Pricing")
st.write(f"Boost revenue by adapting prices to demand and competition for {business_unit}.")
st.markdown("**Scenario**: Set prices for a hotel room, taxi ride, or facility service.")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    demand = st.number_input("Current Demand (e.g., bookings/rides)", min_value=0, value=100, step=10)
with col2:
    competitor_price = st.number_input(f"Competitor Price ({currency_symbol})", min_value=0.0, value=80.0, step=5.0)
with col3:
    avg_cost = st.number_input(f"Average Cost per Unit ({currency_symbol})", min_value=0.0, value=50.0, step=5.0)

# Advanced options expander
with st.expander("Advanced Pricing Settings"):
    sensitivity = st.slider("Price Sensitivity", 0.5, 2.0, 1.2, step=0.1)
    demand_threshold = st.number_input("High Demand Threshold", min_value=0, value=120, step=10)
    min_profit_margin = st.slider("Minimum Profit Margin (%)", 0, 50, 20)

# Calculate dynamic price
base_price = demand * 1.1  # Base price tied to demand
dynamic_price = base_price * sensitivity
if demand > demand_threshold:
    dynamic_price *= 1.2  # 20% boost for high demand
dynamic_price = max(dynamic_price, avg_cost * (1 + min_profit_margin / 100))  # Ensure profit margin

# Output
st.subheader("Pricing Results")
col1, col2 = st.columns(2)
with col1:
    st.metric("Base Price", f"{currency_symbol}{base_price:.2f}")
    st.metric("AI-Optimized Price", f"{currency_symbol}{dynamic_price:.2f}", f"{currency_symbol}{(dynamic_price - base_price):.2f}")
with col2:
    profit = dynamic_price - avg_cost
    st.metric("Profit per Unit", f"{currency_symbol}{profit:.2f}")
    st.write(f"**Competitor Gap**: {currency_symbol}{abs(dynamic_price - competitor_price):.2f} {'higher' if dynamic_price > competitor_price else 'lower'}")
if profit < 0:
    st.error("Warning: Price below cost! Adjust settings.")

# --- Section 2: AI Chatbots for 24/7 Customer Service ---
st.header("2. AI Chatbots for 24/7 Customer Service")
st.write(f"Improve service and cut costs for {business_unit} customers.")
st.markdown("**Scenario**: Handle inquiries for bookings, ride status, or support.")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    queries_per_day = st.number_input("Daily Queries", min_value=0, value=500, step=50)
with col2:
    current_cost = st.number_input(f"Current Cost per Query ({currency_symbol})", min_value=0.0, value=2.5, step=0.1)
with col3:
    current_response_time = st.number_input("Current Response Time (minutes)", min_value=0.0, value=5.0, step=0.5)

# AI improvement logic
ai_cost = 0.5  # Fixed AI cost per query
ai_response_time = 0.1  # 6 seconds
daily_savings = queries_per_day * (current_cost - ai_cost)
annual_savings = daily_savings * 365

# Output
st.subheader("Chatbot Benefits")
col1, col2 = st.columns(2)
with col1:
    st.metric("Current Daily Cost", f"{currency_symbol}{queries_per_day * current_cost:.2f}")
    st.metric("AI Daily Cost", f"{currency_symbol}{queries_per_day * ai_cost:.2f}", f"-{currency_symbol}{daily_savings:.2f}")
with col2:
    st.metric("Response Time", f"{current_response_time} min → {ai_response_time} min")
    st.metric("Annual Savings", f"{currency_symbol}{annual_savings:.2f}")
st.success(f"Deploying chatbots could save {currency_symbol}{annual_savings:.2f} yearly!")

# --- Section 3: AI-Driven Predictive Maintenance ---
st.header("3. AI-Driven Predictive Maintenance")
st.write(f"Minimize downtime for {business_unit} assets.")
st.markdown("**Scenario**: Assess a taxi, HVAC system, or equipment.")

# Input fields
asset_name = st.text_input("Asset Name", value="Taxi 1")
col1, col2 = st.columns(2)
with col1:
    failure_prob = st.slider("Failure Probability (0-1)", 0.0, 1.0, 0.5, step=0.05)
with col2:
    days_since_maintenance = st.number_input("Days Since Last Maintenance", min_value=0, value=30, step=5)

# Maintenance settings
with st.expander("Maintenance Settings"):
    threshold = st.slider("Failure Threshold", 0.0, 1.0, 0.7, step=0.05)
    downtime_cost = st.number_input(f"Cost of Downtime per Day ({currency_symbol})", min_value=0.0, value=200.0, step=10.0)

# Logic
needs_maintenance = failure_prob > threshold or days_since_maintenance > 60
downtime_risk = downtime_cost * failure_prob if needs_maintenance else 0

# Output
st.subheader("Maintenance Recommendation")
st.write(f"**Asset**: {asset_name}")
col1, col2 = st.columns(2)
with col1:
    st.write(f"**Failure Probability**: {failure_prob:.2f}")
    st.write(f"**Days Since Maintenance**: {days_since_maintenance}")
with col2:
    st.write(f"**Status**: {'Needs Maintenance' if needs_maintenance else 'Operational'}")
    st.write(f"**Potential Downtime Cost**: {currency_symbol}{downtime_risk:.2f}")
if needs_maintenance:
    st.warning(f"Schedule maintenance for {asset_name} to avoid {currency_symbol}{downtime_risk:.2f} in losses!")

# Call to Action
st.markdown("---")
st.subheader("Ready to Transform Cerneti?")
st.write("Input your real data to see tailored results. Contact us to integrate these AI solutions into your operations!")
st.button("Request a Demo")

# Footer
st.write(f"Built for Cerenti by [Your Name] | Interactive Demo | March 26, 2025")
