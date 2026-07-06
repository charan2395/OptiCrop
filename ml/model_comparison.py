import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from preprocess import preprocess_pipeline

# Load + preprocess data
X, y, scaler = preprocess_pipeline("data/crop_data.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

# Compare results
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    results[name] = acc

# Print results
print("\n📊 MODEL COMPARISON RESULTS")
for name, acc in results.items():
    print(f"{name}: {acc:.2f}")

# Best model
best_model = max(results, key=results.get)
print("\n🏆 Best Model:", best_model)