import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="AI Solutions Dashboard", layout="wide")

# Title and Introduction
st.title("AI Solutions Dashboard")
st.markdown("""
This dashboard demonstrates how traditional companies can leverage AI for efficiency and innovation:
- **AI-Powered Dynamic Pricing**: Adjust prices based on demand and competition.
- **AI Chatbots for 24/7 Customer Service**: Improve response times and reduce costs.
- **AI-Driven Predictive Maintenance**: Predict asset failures to minimize downtime.
""")

# --- Section 1: AI-Powered Dynamic Pricing ---
st.header("AI-Powered Dynamic Pricing")
st.write("Dynamically adjust prices based on demand and competitor rates.")

# Simulate pricing data
dates = pd.date_range(start="2025-03-01", periods=30, freq="D")
base_demand = np.random.randint(50, 150, size=30)
competitor_prices = base_demand * 0.9 + np.random.normal(0, 10, 30)
pricing_df = pd.DataFrame({
    "Date": dates,
    "Demand": base_demand,
    "Competitor Prices": competitor_prices,
    "Base Price": base_demand * 1.1  # Initial price slightly above demand
})

# Sidebar for pricing adjustments
st.sidebar.title("Dynamic Pricing Controls")
price_sensitivity = st.sidebar.slider("Price Sensitivity Factor", 0.5, 2.0, 1.2, step=0.1)
demand_threshold = st.sidebar.slider("Demand Threshold for Price Boost", 50, 150, 100)

# Calculate dynamic price
pricing_df["Dynamic Price"] = pricing_df["Base Price"] * price_sensitivity
pricing_df["Dynamic Price"] = np.where(
    pricing_df["Demand"] > demand_threshold,
    pricing_df["Dynamic Price"] * 1.2,  # 20% boost during high demand
    pricing_df["Dynamic Price"]
)

# Plot
fig1 = px.line(pricing_df, x="Date", y=["Demand", "Competitor Prices", "Base Price", "Dynamic Price"],
               title="Dynamic Pricing Over Time")
fig1.update_layout(yaxis_title="Price ($)")
st.plotly_chart(fig1, use_container_width=True)

# --- Section 2: AI Chatbots for 24/7 Customer Service ---
st.header("AI Chatbots for 24/7 Customer Service")
st.write("Enhance customer service with instant responses and cost savings.")

# Simulate chatbot performance
chatbot_data = pd.DataFrame({
    "Metric": ["Response Time (s)", "Cost per Query ($)", "Satisfaction (%)"],
    "Without AI": [30, 2.5, 70],
    "With AI": [5, 0.5, 85]
})

# Interactive filter
st.subheader("Performance Comparison")
metric_filter = st.selectbox("Select Metric to Highlight", chatbot_data["Metric"])
filtered_data = chatbot_data.melt(id_vars=["Metric"], var_name="Scenario", value_name="Value")
fig2 = px.bar(filtered_data, x="Metric", y="Value", color="Scenario", barmode="group",
              title="Chatbot Impact on Customer Service",
              text=filtered_data["Value"].round(1))
fig2.update_traces(textposition="auto")
fig2.add_shape(type="rect", x0=metric_filter, y0=0, x1=metric_filter, y1=filtered_data["Value"].max(),
               line=dict(color="red", width=2), fillcolor="rgba(255,0,0,0.1)")
st.plotly_chart(fig2, use_container_width=True)

# --- Section 3: AI-Driven Predictive Maintenance ---
st.header("AI-Driven Predictive Maintenance")
st.write("Predict when assets need maintenance to reduce downtime.")

# Simulate maintenance data
assets = ["Taxi 1", "Taxi 2", "Taxi 3", "Hotel AC 1", "Hotel AC 2"]
failure_probs = np.random.uniform(0, 1, len(assets))
last_maintenance = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 60)) for _ in assets]
maintenance_df = pd.DataFrame({
    "Asset": assets,
    "Failure Probability": failure_probs,
    "Last Maintenance": last_maintenance
})

# Sidebar for maintenance threshold
st.sidebar.title("Maintenance Controls")
failure_threshold = st.sidebar.slider("Failure Probability Threshold", 0.0, 1.0, 0.7)

# Highlight assets needing maintenance
maintenance_df["Needs Maintenance"] = maintenance_df["Failure Probability"] > failure_threshold

# Plot
fig3 = px.bar(maintenance_df, x="Asset", y="Failure Probability",
              title="Predicted Failure Probabilities",
              color="Needs Maintenance",
              hover_data=["Last Maintenance"],
              text=maintenance_df["Failure Probability"].round(2))
fig3.update_traces(textposition="auto")
fig3.add_hline(y=failure_threshold, line_dash="dash", line_color="red",
               annotation_text="Threshold", annotation_position="top right")
st.plotly_chart(fig3, use_container_width=True)

# Display assets needing attention
st.subheader("Assets Requiring Maintenance")
urgent_assets = maintenance_df[maintenance_df["Needs Maintenance"]][["Asset", "Failure Probability"]]
st.table(urgent_assets)

# Footer
st.markdown("---")
st.write("Built with Streamlit by [Your Name] | Data simulated for demonstration | March 26, 2025")
