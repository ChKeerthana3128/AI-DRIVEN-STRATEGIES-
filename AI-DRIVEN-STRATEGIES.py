import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="AI Perspective Dashboard", layout="wide")

# Title and Introduction
st.title("AI Perspective: Leveraging Technology for Efficiency and Innovation")
st.markdown("""
Traditional companies can use AI to compete with startups. This dashboard explores three practical AI solutions:
- **AI-Powered Dynamic Pricing**
- **AI Chatbots for 24/7 Customer Service**
- **AI-Driven Predictive Maintenance**
""")

# Section 1: AI-Powered Dynamic Pricing
st.header("AI-Powered Dynamic Pricing")
st.write("Adjust prices in real-time based on demand, competitor rates, and customer behavior.")
# Simulate pricing data
dates = pd.date_range(start="2025-01-01", periods=30, freq="D")
demand = np.random.randint(50, 150, size=30)
competitor_prices = demand * 0.8 + np.random.normal(0, 10, 30)
dynamic_prices = demand * 1.2 + np.random.normal(0, 5, 30)

pricing_df = pd.DataFrame({
    "Date": dates,
    "Demand": demand,
    "Competitor Prices": competitor_prices,
    "Dynamic Prices": dynamic_prices
})
fig1 = px.line(pricing_df, x="Date", y=["Demand", "Competitor Prices", "Dynamic Prices"],
               title="Dynamic Pricing Simulation")
st.plotly_chart(fig1, use_container_width=True)

# Section 2: AI Chatbots for Customer Service
st.header("AI Chatbots for 24/7 Customer Service")
st.write("Handle inquiries instantly, reducing costs and improving response time.")
# Simulate chatbot metrics
metrics = pd.DataFrame({
    "Metric": ["Response Time (s)", "Cost per Query ($)", "Customer Satisfaction (%)"],
    "Before AI": [30, 2.5, 70],
    "With AI": [5, 0.5, 85]
})
fig2 = px.bar(metrics, x="Metric", y=["Before AI", "With AI"], barmode="group",
              title="Chatbot Impact")
st.plotly_chart(fig2, use_container_width=True)

# Section 3: AI-Driven Predictive Maintenance
st.header("AI-Driven Predictive Maintenance")
st.write("Predict equipment failures to reduce downtime and costs.")
# Simulate maintenance data
assets = ["Taxi 1", "Taxi 2", "Hotel AC 1", "Hotel AC 2"]
failure_prob = np.random.uniform(0, 1, 4)
maintenance_df = pd.DataFrame({"Asset": assets, "Failure Probability": failure_prob})
fig3 = px.bar(maintenance_df, x="Asset", y="Failure Probability",
              title="Predicted Failure Probabilities", color="Failure Probability")
st.plotly_chart(fig3, use_container_width=True)

# Sidebar for Interaction
st.sidebar.title("Dashboard Options")
price_factor = st.sidebar.slider("Adjust Pricing Sensitivity", 0.5, 2.0, 1.2)
st.sidebar.write(f"Dynamic Prices scaled by: {price_factor}")
# Update pricing chart based on slider
pricing_df["Dynamic Prices"] = demand * price_factor + np.random.normal(0, 5, 30)
fig1 = px.line(pricing_df, x="Date", y=["Demand", "Competitor Prices", "Dynamic Prices"],
               title="Dynamic Pricing Simulation (Adjusted)")
st.plotly_chart(fig1, use_container_width=True)
