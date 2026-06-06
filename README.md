# D2C Customer Churn Prediction and Retention API

## Project Information

**Project Title:** D2C Customer Churn Prediction and Retention API

**Author:** Mayank Sharma

**Part:** Part 4 – FastAPI Service & ML Workflow Deployment

---

# Project Overview

This project implements a production-ready FastAPI service for deploying a machine learning-based customer churn prediction model.

The API enables business teams, CRM systems, and customer retention teams to obtain real-time churn-risk predictions for individual customers or batches of customers.

The service loads a trained Gradient Boosting churn prediction model developed in Part 3 of the capstone project and exposes REST endpoints for inference, monitoring, validation, and testing.

The objective of this deployment layer is to bridge the gap between machine learning model development and real-world business usage by providing a scalable and reusable prediction interface.

---

# What Was Completed In Part 4

The following deliverables were implemented:

* FastAPI application deployment
* Model loading from serialized model artifact
* Single customer prediction endpoint
* Batch prediction endpoint
* Health check endpoint
* Input validation using Pydantic schemas
* Error handling and validation mechanisms
* Automated API testing using PyTest
* Reproducible environment configuration
* Monitoring strategy documentation
* Responsible use documentation
* Complete deployment-ready project structure

---

# Business Problem

Customer churn directly impacts revenue, customer lifetime value, and marketing costs.

Businesses often identify churn only after customers have already stopped engaging.

This system predicts customer churn risk before churn occurs, allowing retention teams to proactively engage at-risk customers and improve customer retention rates.

---

# Machine Learning Model Summary

The deployed model was developed in Part 3 of the project.

### Final Selected Model

Gradient Boosting Classifier

### Selection Reason

Among multiple evaluated models, Gradient Boosting achieved the strongest overall balance between:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Final Model Performance

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 0.8065 |
| Precision | 0.7847 |
| Recall    | 0.7687 |
| F1 Score  | 0.7766 |
| ROC-AUC   | 0.8756 |

---

# Project Structure

```text
Part_4_FastAPI_Service_&_ML_Workflow/
│
├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│   └── model_loader.py
│
├── models/
│   └── gradient_boosting.pkl
│
├── tests/
│   └── test_api.py
├──Part_4_Outputs/
│
├── monitoring_plan.md
├── responsible_use_note.md
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation Instructions

## Step 1: Clone Repository

```bash
git clone <repository_url>
cd Part_4_FastAPI_Service_&_ML_Workflow
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

## Step 3: Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Interactive API Documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative OpenAPI Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## 1. Health Check Endpoint

### Endpoint

```http
GET /health
```

### Purpose

Checks whether the API is running successfully.

### Example Response

```json
{
  "status": "ok",
  "message": "API is running successfully"
}
```

---

## 2. Single Prediction Endpoint

### Endpoint

```http
POST /predict
```

### Purpose

Predict churn risk for one customer.

### Sample Request

```json
{
  "city_tier": "Tier 1",
  "age_group": "25-34",
  "acquisition_channel": "Google Search",
  "loyalty_tier": "Gold",
  "preferred_category": "Skin Care",
  "marketing_consent": "Yes",
  "recency_days": 45,
  "frequency_180d": 4,
  "monetary_180d": 2500,
  "return_rate_180d": 0,
  "avg_discount_pct_180d": 12,
  "avg_rating_180d": 4.5,
  "category_diversity_180d": 3,
  "ticket_count_90d": 1,
  "negative_ticket_rate_90d": 0,
  "avg_resolution_hours_90d": 10,
  "days_since_signup": 450,
  "sessions_30d": 15,
  "product_views_30d": 35,
  "cart_adds_30d": 4,
  "wishlist_adds_30d": 2,
  "abandoned_carts_30d": 1,
  "email_opens_30d": 5,
  "campaign_clicks_30d": 2,
  "last_visit_days_ago": 7
}
```

### Example Response

```json
{
  "churn_probability": 0.24,
  "predicted_class": 0,
  "risk_level": "Low",
  "risk_explanation": "Customer shows healthy engagement and recent activity."
}
```

---

## 3. Batch Prediction Endpoint

### Endpoint

```http
POST /batch_predict
```

### Purpose

Predict churn risk for multiple customers simultaneously.

### Input

List of customer records.

### Output

List of prediction results.

---

# Input Validation

Input validation is implemented using Pydantic models.

Validation includes:

* Required field validation
* Missing value validation
* Numeric type validation
* Data format validation
* Request schema enforcement

Benefits:

* Prevents invalid model inputs
* Reduces runtime errors
* Improves API reliability

---

# Running Tests

Execute all API tests:

```bash
python -m pytest tests/ -v
```

The project contains automated test cases covering:

* Health endpoint testing
* Single prediction endpoint testing
* Batch prediction endpoint testing
* Validation testing
* Error handling testing
* Invalid payload testing

---

# Monitoring Strategy

The monitoring framework tracks:

## Data Drift

* Feature distribution changes
* Missing value increases
* Customer behavior changes

## Prediction Drift

* Churn probability distribution
* Prediction volume
* Risk-level distribution

## Business Metrics

* Retention success rate
* Revenue recovery
* Customer engagement

## API Metrics

* Request volume
* Response time
* Error rate
* Availability

Complete details are available in:

```text
monitoring_plan.md
```

---

# Responsible Use

This model should be used only as a decision-support tool.

The retention team should:

* Use predictions for prioritization
* Combine predictions with human judgment
* Review high-risk customers manually

The model should not be used for:

* Automatic customer termination
* Service denial
* Contractual decisions
* Fully automated actions

Complete guidance is available in:

```text
responsible_use_note.md
```

---

# Troubleshooting

## FastAPI Not Found

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Model Loading Error

Verify:

```bash
models/gradient_boosting.pkl
```

exists.

## Version Mismatch Error

Install compatible scikit-learn version:

```bash
pip install scikit-learn==1.6.1
```

## API Not Starting

Verify:

```bash
uvicorn app.main:app --reload
```

is executed from the Part 4 project root directory.

---

# Future Enhancements

Potential improvements include:

* Docker containerization
* Cloud deployment
* CI/CD pipeline integration
* Authentication and authorization
* Model versioning
* Real-time monitoring dashboards
* Automated retraining pipeline
* Drift detection automation

---

# Conclusion

This project successfully deploys a machine learning churn prediction model as a production-ready FastAPI service. The solution provides validated prediction endpoints, automated testing, monitoring guidelines, and responsible-use practices to support customer retention initiatives in a scalable and maintainable manner.

