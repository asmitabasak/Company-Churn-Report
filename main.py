from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load the model we saved from the Jupyter Notebook
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

class CustomerData(BaseModel):
    tenure: int
    charges: float
    balance: float
    support_calls: int

@app.post("/predict")
def predict(customer: CustomerData):
    features = np.array([[customer.tenure, customer.charges, customer.balance, customer.support_calls]])
    
    # Get probability of churn (1)
    probability = model.predict_proba(features)[0][1]
    
    return {
        "churn_risk": round(probability * 100, 2),
        "status": "High Risk" if probability > 0.5 else "Low Risk"
    }
