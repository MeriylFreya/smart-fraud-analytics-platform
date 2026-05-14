import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/processed_data.csv")

st.title("Transaction Explorer")

# Sidebar filters
risk_filter = st.sidebar.multiselect(
    "Select Risk Tier",
    options=df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk_filter)
]

# Search by TransactionID
transaction_id = st.text_input(
    "Enter Transaction ID"
)

if transaction_id:

    try:
        result = filtered_df[
            filtered_df['TransactionID']
            == int(transaction_id)
        ]

        st.dataframe(result)

        if not result.empty:

            st.metric(
                "Fraud Probability",
                f"{result['FraudProbability'].values[0]:.4f}"
            )

    except:
        st.error("Invalid Transaction ID")

# Table
st.dataframe(filtered_df.head(500))