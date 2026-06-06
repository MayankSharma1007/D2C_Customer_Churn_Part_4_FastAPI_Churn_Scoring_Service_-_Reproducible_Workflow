# ==========================================================
# API TESTING
# ==========================================================
# Purpose:
# Validate all API endpoints.
#
# Test Coverage:
# 1. Health Endpoint
# 2. Model Info Endpoint
# 3. Metrics Endpoint
# 4. Single Prediction
# 5. Batch Prediction
# 6. Explain Endpoint
# 7. Missing Field Validation
# 8. Empty Payload Validation
# ==========================================================

from fastapi.testclient import TestClient

from app.main import app

# ==========================================================
# CREATE TEST CLIENT
# ==========================================================

client = TestClient(app)

# ==========================================================
# SAMPLE CUSTOMER
# ==========================================================

sample_customer = {

    "city_tier": "Tier 1",

    "age_group": "25-34",

    "acquisition_channel": "Google Search",

    "loyalty_tier": "Gold",

    "preferred_category": "Skin Care",

    "marketing_consent": "Yes",

    "recency_days": 20,

    "frequency_180d": 5,

    "monetary_180d": 2500,

    "return_rate_180d": 0.10,

    "avg_discount_pct_180d": 15,

    "avg_rating_180d": 4.5,

    "category_diversity_180d": 3,

    "ticket_count_90d": 1,

    "negative_ticket_rate_90d": 0.0,

    "avg_resolution_hours_90d": 12,

    "days_since_signup": 300,

    "sessions_30d": 10,

    "product_views_30d": 20,

    "cart_adds_30d": 5,

    "wishlist_adds_30d": 2,

    "abandoned_carts_30d": 1,

    "email_opens_30d": 4,

    "campaign_clicks_30d": 2,

    "last_visit_days_ago": 5
}

# ==========================================================
# TEST 1
# HEALTH ENDPOINT
# ==========================================================

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "ok"


# ==========================================================
# TEST 2
# MODEL INFO ENDPOINT
# ==========================================================

def test_model_info():

    response = client.get("/model_info")

    assert response.status_code == 200

    assert "model_name" in response.json()


# ==========================================================
# TEST 3
# METRICS ENDPOINT
# ==========================================================

def test_metrics():

    response = client.get("/metrics")

    assert response.status_code == 200

    assert "accuracy" in response.json()


# ==========================================================
# TEST 4
# SINGLE PREDICTION
# ==========================================================

def test_predict():

    response = client.post(
        "/predict",
        json=sample_customer
    )

    assert response.status_code == 200

    assert "churn_probability" in response.json()


# ==========================================================
# TEST 5
# BATCH PREDICTION
# ==========================================================

def test_batch_predict():

    response = client.post(
        "/batch_predict",
        json=[
            sample_customer,
            sample_customer
        ]
    )

    assert response.status_code == 200

    assert len(response.json()) == 2


# ==========================================================
# TEST 6
# EXPLANATION ENDPOINT
# ==========================================================

def test_explain():

    response = client.post(
        "/explain",
        json=sample_customer
    )

    assert response.status_code == 200

    assert "risk_level" in response.json()


# ==========================================================
# TEST 7
# MISSING FIELD VALIDATION
# ==========================================================

def test_missing_field():

    invalid_customer = sample_customer.copy()

    del invalid_customer["recency_days"]

    response = client.post(
        "/predict",
        json=invalid_customer
    )

    assert response.status_code == 422


# ==========================================================
# TEST 8
# EMPTY PAYLOAD VALIDATION
# ==========================================================

def test_empty_payload():

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 422



## API Testing

#A comprehensive test suite was developed to verify endpoint functionality, validation behaviour, and prediction workflow correctness.

#The tests cover:

#1. Health monitoring endpoint.
#2. Model metadata endpoint.
#3. Performance metrics endpoint.
#4. Single customer prediction.
#5. Batch customer prediction.
#6. Risk explanation endpoint.
#7. Missing field validation.
#8. Empty payload validation.

#Testing ensures that the API behaves consistently and can safely process production requests.



### Observation

#All critical API functionality is validated through automated tests.

#The test suite confirms:

#- Endpoint availability.
#- Correct response generation.
#- Input validation behaviour.
#- Prediction workflow integrity.
#- Error handling capability.

#The presence of automated tests improves reliability and supports future maintenance of the application.