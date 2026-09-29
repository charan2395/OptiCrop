from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent

# -----------------------------
# Load Model
# -----------------------------
with open(BASE_DIR / "model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Load Scaler
# -----------------------------
if (BASE_DIR / "scaler.pkl").exists():
    with open(BASE_DIR / "scaler.pkl", "rb") as file:
        scaler = pickle.load(file)
elif (BASE_DIR / "scaler(1).pkl").exists():
    with open(BASE_DIR / "scaler(1).pkl", "rb") as file:
        scaler = pickle.load(file)
else:
    raise FileNotFoundError(
        "Scaler file not found. Keep scaler.pkl or scaler(1).pkl in the project folder."
    )


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from form
        n = float(request.form["n"])
        p = float(request.form["p"])
        k = float(request.form["k"])
        temp = float(request.form["temp"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Create input dataframe
        data = pd.DataFrame(
            [[
                n,
                p,
                k,
                temp,
                humidity,
                ph,
                rainfall
            ]],
            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )

        # Scale input
        scaled_data = scaler.transform(data)

        # Prediction
        result = model.predict(scaled_data)[0]

        # -----------------------------
        # Get probabilities if available
        # -----------------------------
        top_predictions = []

        if hasattr(model, "predict_proba") and hasattr(model, "classes_"):

            probabilities = model.predict_proba(scaled_data)[0]

            prediction_data = list(
                zip(model.classes_, probabilities)
            )

            prediction_data.sort(
                key=lambda x: x[1],
                reverse=True
            )

            for crop, probability in prediction_data[:5]:

                top_predictions.append({
                    "crop": str(crop),
                    "probability": round(
                        float(probability) * 100,
                        2
                    )
                })

        # -----------------------------
        # Send everything to result.html
        # -----------------------------
        return render_template(
            "result.html",

            prediction=str(result),

            n=n,
            p=p,
            k=k,
            temp=temp,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall,

            top_predictions=top_predictions,

            model_name=type(model).__name__
        )

    except Exception as e:

        return f"""
        <h2>Prediction Error</h2>
        <p>{str(e)}</p>
        <a href="/">Go Back</a>
        """, 400


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )