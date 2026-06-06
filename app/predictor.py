# ==========================================================
# PREDICTION ENGINE
# ==========================================================
# Purpose:
# Performs churn prediction using the trained model.
#
# Responsibilities:
# 1. Generate churn probability
# 2. Generate churn class
# 3. Generate risk level
# 4. Generate business explanation
# 5. Return prediction response
# ==========================================================

import pandas as pd

from app.model_loader import get_model

# ----------------------------------------------------------
# LOAD TRAINED MODEL
# ----------------------------------------------------------

model = get_model()

# ----------------------------------------------------------
# RISK LEVEL CALCULATION
# ----------------------------------------------------------

def determine_risk_level(probability):

    if probability >= 0.70:
        return "High"

    elif probability >= 0.40:
        return "Medium"

    else:
        return "Low"


# ----------------------------------------------------------
# BUSINESS EXPLANATION ENGINE
# ----------------------------------------------------------

def generate_explanation(customer):

    reasons = []

    # Customer inactivity

    if customer["recency_days"] > 90:
        reasons.append(
            "Customer has been inactive for a long period."
        )

    # Low purchase frequency

    if customer["frequency_180d"] < 2:
        reasons.append(
            "Purchase frequency is significantly below average."
        )

    # Low spending

    if customer["monetary_180d"] < 500:
        reasons.append(
            "Customer spending is relatively low."
        )

    # Support complaints

    if customer["negative_ticket_rate_90d"] > 0.50:
        reasons.append(
            "High proportion of negative support interactions."
        )

    # Low engagement

    if customer["email_opens_30d"] < 2:
        reasons.append(
            "Low engagement with marketing communications."
        )

    # Cart abandonment

    if customer["abandoned_carts_30d"] > 2:
        reasons.append(
            "Frequent cart abandonment behaviour detected."
        )

    # Long gap since last visit

    if customer["last_visit_days_ago"] > 30:
        reasons.append(
            "Customer has not visited recently."
        )

    # No reasons triggered

    if len(reasons) == 0:

        reasons.append(
            "Customer currently shows healthy engagement patterns."
        )

    return reasons


# ----------------------------------------------------------
# SINGLE CUSTOMER PREDICTION
# ----------------------------------------------------------

def predict_customer(customer_dict):

    # Convert input into dataframe

    customer_df = pd.DataFrame([customer_dict])

    # Generate churn probability

    churn_probability = float(
        model.predict_proba(customer_df)[0][1]
    )

    # Generate churn class

    predicted_class = int(
        model.predict(customer_df)[0]
    )

    # Risk level

    risk_level = determine_risk_level(
        churn_probability
    )

    # Business explanation

    explanation = generate_explanation(
        customer_dict
    )

    # Final response

    return {
        "churn_probability": round(
            churn_probability,
            4
        ),
        "predicted_class": predicted_class,
        "risk_level": risk_level,
        "risk_explanation": explanation
    }


# ----------------------------------------------------------
# BATCH PREDICTION
# ----------------------------------------------------------

def batch_predict(customers):

    results = []

    for customer in customers:

        prediction = predict_customer(
            customer
        )

        results.append(prediction)

    return results



## Churn Prediction Engine

#This module contains the core business logic of the churn prediction service.

#The module performs:

#1. Churn probability estimation
#2. Churn classification
#3. Risk categorization
#4. Business-friendly explanation generation
#5. Batch prediction support

#Predictions are generated using the trained Gradient Boosting model developed in Part 3.

#To improve interpretability, an explanation engine converts customer behaviour patterns into human-readable risk factors that can be used by the retention team.




### Observation

#The prediction engine successfully transforms raw customer features into actionable business insights.

#Key capabilities include:

#- Probability estimation for churn risk.
#- Classification into churn or non-churn classes.
#- Risk categorization into High, Medium, and Low risk segments.
#- Generation of interpretable explanations.
#- Support for both individual and batch predictions.

#The explanation engine improves model transparency and makes predictions easier for business stakeholders to understand and act upon.