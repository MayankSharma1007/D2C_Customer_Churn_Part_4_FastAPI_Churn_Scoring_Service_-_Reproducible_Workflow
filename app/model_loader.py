# ==========================================================
# MODEL LOADER
# ==========================================================
# Purpose:
# Loads the trained Gradient Boosting model
# when FastAPI application starts.
#
# This prevents reloading the model for every request.
# ==========================================================

import joblib
from pathlib import Path

# Model location
MODEL_PATH = Path("models/gradient_boosting.pkl")

# Load model
model = joblib.load(MODEL_PATH)

# Function to access model from other files
def get_model():
    return model


## Model Loading

#This module is responsible for loading the trained Gradient Boosting model from the models directory.

#Loading the model once during application startup improves performance by avoiding repeated disk reads during prediction requests.

#The module exposes a helper function that can be used throughout the application whenever model access is required.



### Observation

#- The model is loaded successfully at startup.
#- Only one copy of the model remains in memory.
#- Prediction latency is reduced.
#- The application becomes more scalable for multiple requests.