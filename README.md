# 📉 ChurnGuard AI: Customer Retention Predictor

ChurnGuard is a full-stack AI/ML application designed to predict customer churn using a Random Forest Classifier. It visualizes enterprise-level risk distribution and tenure analysis.

## 🏗️ Project Architecture
- **Frontend:** React-inspired HTML5/Tailwind UI with Chart.js.
- **Backend:** FastAPI (Python) serving ML predictions.
- **Model:** Scikit-learn Random Forest model trained on behavioral customer data.

## 📊 Business Logic
The model analyzes:
1. **Tenure:** Months the customer has been active.
2. **Support Calls:** High frequency of calls correlates with high churn.
3. **Financial Health:** Average balance and monthly charges.

## 🚦 Getting Started
1. Install Python requirements: `pip install fastapi uvicorn scikit-learn`
2. Run the API: `uvicorn main:app --reload`
3. Open `index.html` in your browser.
