# ==========================================================
# FASTAPI APPLICATION
# ==========================================================
# Purpose:
# Main API application entry point.
#
# Endpoints:
# 1. GET  /health
# 2. GET  /model_info
# 3. GET  /metrics
# 4. POST /predict
# 5. POST /batch_predict
# 6. POST /explain
# ==========================================================

from fastapi import FastAPI
from fastapi import HTTPException

from typing import List

from app.schemas import (
    CustomerInput,
    PredictionResponse
)

from app.predictor import (
    predict_customer,
    batch_predict,
    generate_explanation,
    determine_risk_level
)

from app.model_loader import get_model

# ==========================================================
# APP INITIALIZATION
# ==========================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description="D2C Customer Churn Intelligence & Retention API",
    version="1.0"
)

# Load model

model = get_model()

# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")

def health():

    return {
        "status": "ok",
        "message": "API is running successfully"
    }


# ==========================================================
# MODEL INFORMATION
# ==========================================================

@app.get("/model_info")

def model_info():

    return {

        "project":
        "D2C Customer Churn Intelligence & Retention API",

        "model_name":
        "Gradient Boosting Classifier",

        "version":
        "1.0",

        "target":
        "churn_next_60d",

        "author":
        "Mayank Sharma"
    }


# ==========================================================
# MODEL METRICS
# ==========================================================

@app.get("/metrics")

def metrics():

    return {

        "accuracy": 0.8065,

        "precision": 0.7847,

        "recall": 0.7687,

        "f1_score": 0.7766,

        "roc_auc": 0.8756
    }


# ==========================================================
# SINGLE CUSTOMER PREDICTION
# ==========================================================

@app.post(
    "/predict",
    response_model=PredictionResponse
)

def predict(customer: CustomerInput):

    try:

        prediction = predict_customer(
            customer.model_dump()
        )

        return prediction

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ==========================================================
# BATCH PREDICTION
# ==========================================================

@app.post("/batch_predict")

def batch_prediction(
    customers: List[CustomerInput]
):

    try:

        customer_list = [
            customer.model_dump()
            for customer in customers
        ]

        predictions = batch_predict(
            customer_list
        )

        return predictions

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ==========================================================
# EXPLANATION ENDPOINT
# ==========================================================

@app.post("/explain")

def explain(customer: CustomerInput):

    customer_dict = customer.model_dump()

    explanation = generate_explanation(
        customer_dict
    )

    probability = predict_customer(
        customer_dict
    )["churn_probability"]

    risk_level = determine_risk_level(
        probability
    )

    return {

        "risk_level":
        risk_level,

        "top_risk_factors":
        explanation
    }



## FastAPI Application

#The FastAPI application serves as the deployment layer for the churn prediction model.

#The application exposes multiple endpoints that allow external systems to:

#- Check service health
#- Retrieve model information
#- Access model performance metrics
#- Generate churn predictions
#- Process batch predictions
#- Obtain business explanations for churn risk

#The API acts as an interface between business applications and the machine learning model.



### Observation

#The FastAPI application successfully converts the machine learning model into a deployable service.

#Key capabilities include:

#- Real-time prediction generation.
#- Batch prediction support.
#- Model transparency through explanation endpoints.
#- Operational monitoring through health checks.
#- Access to model metadata and evaluation metrics.

#These endpoints collectively enable integration with CRM systems, retention platforms, dashboards, and business intelligence tools.