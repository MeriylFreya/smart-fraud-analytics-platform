import streamlit as st
import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("models/lgbm_model.pkl")

# Load data
df = pd.read_csv("data/processed_data.csv")

st.title("SHAP Transaction Explainer")

# Transaction input
transaction_id = st.number_input(
    "Enter Transaction ID",
    min_value=1,
    step=1
)

if int(transaction_id) in df['TransactionID'].astype(int).values:

    row = df[
        df['TransactionID'].astype(int) == int(transaction_id)
    ]

    X = row.drop(
        columns=[
            'FraudProbability',
            'ActualFraud',
            'RiskTier'
        ],
        errors='ignore'
    )

    # Comprehensive feature mapping for readability
    feature_labels = {
        'TransactionAmt': 'Transaction Amount ($)',
        'TransactionDT': 'Transaction Time',
        'TransactionDayOfWeek': 'Day of Week',
        'TransactionHour': 'Hour of Day',
        'addr1': 'Billing Address ID',
        'addr2': 'Shipping Address ID',
        'card1': 'Card Type',
        'card2': 'Card Category',
        'card3': 'Card Issuer',
        'card4': 'Card Network',
        'card5': 'Card Brand',
        'card6': 'Card Subtype',
    }
    
    # Add anonymized features with descriptions
    for i in range(1, 201):
        if f'V{i}' not in feature_labels:
            feature_labels[f'V{i}'] = f'Payment Pattern #{i}'
    
    # Add categorical features with descriptions
    for i in range(1, 15):
        if f'C{i}' not in feature_labels:
            feature_labels[f'C{i}'] = f'Customer Category {i}'
    
    # Create readable feature names
    readable_features = [feature_labels.get(col, col) for col in X.columns]

    # SHAP
    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    st.subheader("Fraud Probability")

    prob = model.predict_proba(X)[0][1]

    st.metric(
        "Predicted Fraud Risk",
        f"{prob*100:.2f}%"
    )

    # Waterfall plot with readable labels
    fig, ax = plt.subplots(figsize=(12,7))

    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values[0],
            base_values=explainer.expected_value,
            data=X.iloc[0],
            feature_names=readable_features
        ),
        max_display=8,
        show=False
    )

    st.pyplot(fig)

    st.markdown("""
    **How to read this chart:**
    - **Base Risk:** Starting fraud probability
    - **Red bars (↑):** Features that INCREASE fraud risk
    - **Blue bars (↓):** Features that DECREASE fraud risk
    """)

    # Plain English explanation
    st.subheader("Explanation")

    if prob >= 0.75:
        st.error(f"""
        ⚠️ **HIGH FRAUD RISK ({prob*100:.2f}%)**
        
        This transaction shows strong fraud indicators based on:
        - Unusual transaction patterns
        - Atypical behavioural signals
        - High-risk transaction characteristics
        
        **Recommendation:** Review immediately or flag for manual verification.
        """)

    elif prob >= 0.40:
        st.warning(f"""
        ⚡ **MODERATE FRAUD RISK ({prob*100:.2f}%)**
        
        This transaction contains mixed behavioural signals:
        - Some patterns are unusual but not conclusive
        - Requires additional verification
        - Could be legitimate or fraudulent
        
        **Recommendation:** Request additional verification from customer.
        """)

    else:
        st.success(f"""
        ✓ **LOW FRAUD RISK ({prob*100:.2f}%)**
        
        This transaction appears consistent with:
        - Normal customer behaviour
        - Expected transaction patterns
        - Legitimate activity indicators
        
        **Recommendation:** Safe to approve.
        """)

else:
    st.info("⚠️ Please enter a valid Transaction ID from the dataset")