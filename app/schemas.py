# ==========================================================
# PYDANTIC SCHEMAS
# ==========================================================
# Purpose:
# Define request and response formats.
#
# FastAPI automatically validates incoming data
# using these schemas.
# ==========================================================

from pydantic import BaseModel
from typing import Optional

# ----------------------------------------------------------
# CUSTOMER INPUT SCHEMA
# ----------------------------------------------------------

class CustomerInput(BaseModel):

    city_tier: str
    age_group: str
    acquisition_channel: str

    loyalty_tier: Optional[str]

    preferred_category: str
    marketing_consent: str

    recency_days: int
    frequency_180d: int
    monetary_180d: float

    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float

    category_diversity_180d: int

    ticket_count_90d: int
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float

    days_since_signup: int

    sessions_30d: int
    product_views_30d: int
    cart_adds_30d: int
    wishlist_adds_30d: int
    abandoned_carts_30d: int

    email_opens_30d: int
    campaign_clicks_30d: int

    last_visit_days_ago: int


# ----------------------------------------------------------
# PREDICTION RESPONSE SCHEMA
# ----------------------------------------------------------

class PredictionResponse(BaseModel):

    churn_probability: float

    predicted_class: int

    risk_level: str

    risk_explanation: list[str]



## Input Validation Using Pydantic

#Pydantic models are used to validate incoming API requests.

#Validation ensures:

#- Correct data types
#- Required feature availability
#- Consistent prediction inputs
#- Reduced runtime errors

#The schema reflects the same features used during model training.



### Observation

#- Invalid requests are automatically rejected.
#- Missing fields generate validation errors.
#- Data quality improves before reaching the model.
#- FastAPI automatically generates documentation from schemas.