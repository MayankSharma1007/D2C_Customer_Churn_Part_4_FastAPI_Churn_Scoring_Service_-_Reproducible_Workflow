# Monitoring Plan

## Overview

This document describes the monitoring strategy for the D2C Customer Churn Prediction API after deployment. Continuous monitoring is essential to ensure model reliability, prediction quality, API availability, and business value.

---

## 1. Data Drift Monitoring

### Objective

Monitor whether incoming customer data differs significantly from the data used during model training.

### Features to Track

* recency_days
* frequency_180d
* monetary_180d
* return_rate_180d
* avg_discount_pct_180d
* avg_rating_180d
* category_diversity_180d
* ticket_count_90d
* negative_ticket_rate_90d
* avg_resolution_hours_90d
* days_since_signup
* sessions_30d
* product_views_30d
* cart_adds_30d
* wishlist_adds_30d
* abandoned_carts_30d
* email_opens_30d
* campaign_clicks_30d
* last_visit_days_ago

### Monitoring Approach

* Compare monthly production data distributions against training data distributions.
* Track mean, median, standard deviation, and percentiles.
* Flag features exhibiting significant shifts.
* Investigate sudden changes in customer behavior.

### Alert Conditions

* Major deviation in recency distributions.
* Significant change in customer spending behavior.
* Sudden increase in missing values.
* New categories not present during training.

---

## 2. Prediction Distribution Monitoring

### Objective

Monitor model prediction patterns over time.

### Metrics

* Average churn probability.
* Percentage of customers classified as churn.
* Percentage of customers classified as non-churn.
* Daily prediction volume.

### Alert Conditions

* Churn predictions exceed 80% of incoming requests.
* Churn predictions drop below 5%.
* Large changes in average churn probability.

### Business Importance

Abnormal prediction distributions may indicate model drift or data quality issues.

---

## 3. Business Outcome Monitoring

### Objective

Track whether predictions generate business value.

### Metrics

* Actual customer retention rate.
* Retention campaign success rate.
* Revenue recovered through interventions.
* Percentage of high-risk customers retained.
* Customer lifetime value changes.

### Review Frequency

* Weekly business review.
* Monthly model performance review.

---

## 4. API Health Monitoring

### Objective

Ensure API availability and responsiveness.

### Metrics

* Request count.
* Average response time.
* Error rate.
* Success rate.
* Concurrent users.

### Alert Conditions

* Response time > 2 seconds.
* Error rate > 5%.
* API downtime.
* Failed model loading.

---

## 5. Retraining Triggers

The model should be retrained when:

### Performance Triggers

* Accuracy drops significantly.
* Precision drops below acceptable levels.
* Recall drops below acceptable levels.
* Business KPIs deteriorate.

### Data Triggers

* Major feature distribution shifts.
* New customer behavior patterns emerge.
* Significant increase in missing values.

### Time-Based Trigger

* Retrain every 3–6 months even if no issues are detected.

---

## 6. Monitoring Responsibilities

### Data Science Team

* Monitor model performance.
* Investigate drift alerts.
* Retrain and validate models.

### Engineering Team

* Monitor API health.
* Resolve deployment issues.
* Maintain infrastructure.

### Business Team

* Track retention outcomes.
* Review campaign effectiveness.
* Provide feedback for future improvements.

---

## Conclusion

This monitoring plan ensures that the churn prediction API remains accurate, reliable, and aligned with business objectives after deployment.
