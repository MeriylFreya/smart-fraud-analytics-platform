# AI-Powered Fraud Detection & Risk Intelligence Platform

## Live Dashboard

https://smart-fraud-analytics-platform.streamlit.app/

---

## Project Overview

This project presents an end-to-end AI-powered fraud detection and risk intelligence platform built using machine learning, explainable AI, behavioural analytics, and interactive dashboard visualization techniques.

The system was developed to identify fraudulent financial transactions, analyse behavioural fraud patterns, and transform model predictions into actionable business intelligence.

The project includes:
- data preprocessing and feature engineering,
- imbalance handling using SMOTE,
- multiple fraud detection models,
- threshold optimization,
- SHAP explainability,
- risk segmentation,
- business insights generation,
- and deployment through a multi-page Streamlit dashboard.

---

## Objectives

The primary objectives of this project were to:

- detect fraudulent transactions using machine learning,
- handle highly imbalanced financial data,
- improve interpretability using Explainable AI,
- analyse fraud behaviour patterns,
- build a real-time fraud operations dashboard,
- and generate business-oriented fraud prevention insights.

---

## Dataset Information

The project uses transaction and identity datasets containing anonymized financial transaction features.

### Dataset Characteristics

- Total merged records: 590,540
- Total features before preprocessing: 434
- Fraud rate: ~3.5%
- Severe class imbalance handled using SMOTE

The dataset includes:
- transaction information,
- payment-related features,
- behavioural variables,
- temporal patterns,
- and anonymized engineered features.

---

## Project Workflow

### 1. Data Preprocessing
- Merged transaction and identity datasets
- Missing value analysis
- Sparse column removal (>50% missing)
- Median and mode imputation
- Label encoding for categorical features
- Feature scaling using RobustScaler

### 2. Feature Engineering
Engineered features include:
- `HourOfDay`
- `AmtToMeanRatio`
- `IsHighAmount`

### 3. Imbalance Handling
- Stratified train-test split
- SMOTE applied only on training data

### 4. Model Training
Implemented models:
- LightGBM Classifier
- XGBoost Classifier
- Isolation Forest

### 5. Explainable AI
Used SHAP for:
- global feature importance,
- local transaction explanations,
- waterfall plots,
- and dependence analysis.

### 6. Risk Segmentation
Transactions segmented into:
- Critical Risk
- Suspicious
- Clear

### 7. Streamlit Deployment
Developed and deployed a multi-page fraud operations dashboard using Streamlit Community Cloud.

---

## Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|---|
| LightGBM | 0.9829 | 0.8427 | 0.4373 | 0.5758 | 0.9111 | 0.6003 |
| XGBoost | 0.9800 | 0.6856 | 0.4577 | 0.5490 | 0.8995 | 0.5721 |
| Isolation Forest | 0.9524 | 0.1707 | 0.2041 | 0.1859 | - | - |

### Best Performing Model
LightGBM achieved the strongest overall performance due to:
- highest ROC-AUC,
- highest PR-AUC,
- superior precision,
- and strong fraud detection capability on imbalanced financial data.

---

## Explainable AI with SHAP

SHAP (SHapley Additive Explanations) was used to improve model transparency and interpretability.

### SHAP Analysis Included
- Global SHAP Summary Plot
- SHAP Waterfall Plot for:
  - confirmed fraud transaction,
  - borderline transaction,
  - legitimate transaction
- SHAP Dependence Plot

### Key Fraud Signals Identified
- HourOfDay
- TransactionAmt
- card4 / card6
- behavioural variables (`V87`, `V294`, `C14`)

The engineered feature `HourOfDay` emerged as one of the most influential fraud indicators.

---

## Risk Segmentation

Transactions were categorized into operational risk tiers based on predicted fraud probability.

| Risk Tier | Probability Range |
|---|---|
| Critical Risk | >= 0.75 |
| Suspicious | 0.40 - 0.74 |
| Clear | < 0.40 |

This segmentation enables:
- analyst prioritization,
- adaptive fraud response,
- and operational monitoring workflows.

---

## Visualizations

The project includes multiple analytical and explainable AI visualizations.

### Implemented Charts
- SHAP Global Summary Plot
- Fraud Rate by Hour of Day
- Transaction Amount Distribution
- Risk Tier Donut Chart
- Precision-Recall Curve with Optimal Threshold
- Interactive Plotly Scatter Plot

---

## Dashboard Features

### Overview Page
Displays:
- total transactions,
- fraud count,
- detection rate,
- and average fraud amount.

### Transaction Explorer
Includes:
- searchable transactions,
- filterable risk tiers,
- and live fraud probability analysis.

### SHAP Explainer
Allows users to:
- enter a TransactionID,
- view SHAP waterfall explanations,
- and understand prediction reasoning in plain English.

---

## Business Insights

### Key Findings
- Fraud activity demonstrated strong temporal behaviour patterns.
- Fraudulent transactions were not limited to extremely large purchases.
- Behavioural variables significantly improved fraud prediction capability.

### Recommended Fraud Prevention Policies
1. Adaptive multi-factor authentication for high-risk transactions.
2. Enhanced monitoring during high-risk transaction hours.

### Estimated Business Impact
The fraud intelligence system could help financial organizations:
- reduce fraud-related losses,
- improve analyst efficiency,
- and minimize false-positive operational costs.

---

## Technologies Used

### Programming Language
- Python

### Data Science & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- XGBoost
- Imbalanced-learn

### Visualization
- Matplotlib
- Seaborn
- Plotly

### Explainable AI
- SHAP

### Deployment
- Streamlit Community Cloud

---

## Project Structure

```text
smart-fraud-analytics-platform/
│
├── app.py
├── analysis.ipynb
├── requirements.txt
├── README.md
│
├── data/
├── models/
├── pages/
├── charts/
└── screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/MeriylFreya/smart-fraud-analytics-platform.git
```

### Navigate to Project Folder

```bash
cd smart-fraud-analytics-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## Future Improvements

Potential future enhancements include:
- real-time fraud streaming,
- API integration,
- graph-based fraud detection,
- deep learning fraud models,
- adaptive thresholding,
- and real-time fraud alert systems.

---

## Conclusion

This project successfully developed a complete fraud detection and risk intelligence system using:
- machine learning,
- explainable AI,
- behavioural analytics,
- and interactive visualization techniques.

The integration of SHAP explainability, operational risk segmentation, and Streamlit deployment transformed the project into a practical and interpretable fraud analytics platform suitable for real-world financial environments.
