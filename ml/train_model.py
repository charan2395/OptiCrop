import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

from preprocess import preprocess_pipeline

# Load + preprocess
X, y, scaler = preprocess_pipeline("data/crop_data.csv")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# SAVE MODEL
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# SAVE SCALER (IMPORTANT)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model + Scaler saved successfully")