import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="AI Solutions Dashboard", layout="wide")

# Title and Introduction
st.title("AI Solutions Dashboard")
st.markdown("""
Enter your data below to see how AI can enhance efficiency and innovation:
- **AI-Powered Dynamic Pricing**: Calculate optimal prices.
- **AI Chatbots for 24/7 Customer Service**: Estimate performance improvements.
- **AI-Driven Predictive Maintenance**: Assess asset maintenance needs.
""")

# --- Section 1: AI-Powered Dynamic Pricing ---
st.header("AI-Powered Dynamic Pricing")
st.write("Input demand and competitor price to get an AI-optimized price.")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    demand = st.number_input("Current Demand (e.g., bookings)", min_value=0, value=100, step=10)
with col2:
    competitor_price = st.number_input("Competitor Price ($)", min_value=0.0, value=80.0, step=5.0)
with col3:
    sensitivity = st.slider("Price Sensitivity", 0.5, 2.0, 1.2, step=0.1)

# Calculate dynamic price
base_price = demand * 1.1  # Base price is 10% above demand
dynamic_price = base_price * sensitivity
if demand > 100:  # Boost price by 20% if demand exceeds threshold
    dynamic_price *= 1.2

# Output
st.subheader("Pricing Output")
st.write(f"**Base Price**: ${base_price:.2f}")
st.write(f"**AI-Optimized Dynamic Price**: ${dynamic_price:.2f}")
st.write(f"**Compared to Competitor**: {'Higher' if dynamic_price > competitor_price else 'Lower'} by ${abs(dynamic_price - competitor_price):.2f}")

# --- Section 2: AI Chatbots for 24/7 Customer Service ---
st.header("AI Chatbots for 24/7 Customer Service")
st.write("Input current metrics to see AI-driven improvements.")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    current_response_time = st.number_input("Current Response Time (seconds)", min_value=0, value=30, step=5)
with col2:
    current_cost = st.number_input("Current Cost per Query ($)", min_value=0.0, value=2.5, step=0.1)
with col3:
    current_satisfaction = st.number_input("Current Satisfaction (%)", min_value=0, max_value=100, value=70, step=5)

# Simulate AI improvements (example logic)
ai_response_time = max(5, current_response_time * 0.2)  # Reduced to 20% or min 5s
ai_cost = max(0.5, current_cost * 0.2)  # Reduced to 20% or min $0.5
ai_satisfaction = min(90, current_satisfaction + 15)  # Increased by 15%, max 90%

# Output
st.subheader("Chatbot Performance Output")
st.write(f"**Response Time**: {current_response_time}s → {ai_response_time:.1f}s")
st.write(f"**Cost per Query**: ${current_cost:.2f} → ${ai_cost:.2f}")
st.write(f"**Customer Satisfaction**: {current_satisfaction}% → {ai_satisfaction}%")

# --- Section 3: AI-Driven Predictive Maintenance ---
st.header("AI-Driven Predictive Maintenance")
st.write("Input asset details to predict maintenance needs.")

# Input fields
asset_name = st.text_input("Asset Name (e.g., Taxi 1)", value="Taxi 1")
failure_prob = st.slider("Estimated Failure Probability (0-1)", 0.0, 1.0, 0.5, step=0.05)
days_since_maintenance = st.number_input("Days Since Last Maintenance", min_value=0, value=30, step=5)
maintenance_threshold = st.slider("Failure Probability Threshold", 0.0, 1.0, 0.7, step=0.05)

# Calculate maintenance need
needs_maintenance = failure_prob > maintenance_threshold or days_since_maintenance > 60
recommendation = "Schedule Maintenance" if needs_maintenance else "No Action Needed"

# Output
st.subheader("Maintenance Output")
st.write(f"**Asset**: {asset_name}")
st.write(f"**Failure Probability**: {failure_prob:.2f}")
st.write(f"**Days Since Last Maintenance**: {days_since_maintenance}")
st.write(f"**Recommendation**: {recommendation}")
if needs_maintenance:
    st.warning("Action required based on high failure probability or overdue maintenance.")

# Footer
st.markdown("---")
st.write("Built with Streamlit by [Your Name] | Interactive demo | March 26, 2025")
