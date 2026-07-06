import numpy as np
import pickle

# Load model and scaler once
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


def predict_crop(data):
    """
    Predict crop based on input parameters
    data = [N, P, K, temperature, humidity, ph, rainfall]
    """

    # Convert to numpy array
    input_array = np.array(data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_array)

    # Predict
    prediction = model.predict(input_scaled)[0]

    return prediction