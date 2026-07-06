from flask import Flask, render_template, request
import numpy as np
import pickle
from utils.predictor import predict_crop

# ✅ STEP 1: CREATE FLASK APP (MUST BE FIRST)
app = Flask(__name__)

# Optional (if you still want direct usage)
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = [
        float(request.form["n"]),
        float(request.form["p"]),
        float(request.form["k"]),
        float(request.form["temp"]),
        float(request.form["humidity"]),
        float(request.form["ph"]),
        float(request.form["rainfall"])
    ]

    result = predict_crop(data)

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)