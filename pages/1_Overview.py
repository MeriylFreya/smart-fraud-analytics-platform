import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/processed_data.csv")

st.title("Fraud Overview")

# Metrics
total_transactions = len(df)

fraud_count = df['ActualFraud'].sum()

detection_rate = (
    fraud_count / total_transactions
) * 100

avg_fraud_amt = df[
    df['ActualFraud'] == 1
]['TransactionAmt'].mean()

# Metric cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    f"{total_transactions:,}"
)

col2.metric(
    "Fraud Count",
    int(fraud_count)
)

col3.metric(
    "Detection Rate",
    f"{detection_rate:.2f}%"
)

col4.metric(
    "Average Fraud Amount",
    f"${avg_fraud_amt:.2f}"
)

# Risk tier chart
risk_counts = df['RiskTier'].value_counts()

fig = px.bar(
    x=risk_counts.index,
    y=risk_counts.values,
    color=risk_counts.index,
    title="Risk Tier Distribution"
)

st.plotly_chart(fig, use_container_width=True)