# 🌱 OptiCrop: Smart Agricultural Production Optimization Engine

## 📌 Project Overview

OptiCrop is an AI-powered agricultural recommendation system developed using Machine Learning and Flask. It helps farmers, researchers, and policymakers identify the most suitable crop based on soil nutrients and environmental conditions.

The application predicts the best crop using parameters such as:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

The project aims to improve agricultural productivity, sustainability, and resource utilization through data-driven recommendations.

---

## 🎯 Features

- Intelligent Crop Recommendation
- Machine Learning Prediction
- User-Friendly Flask Web Interface
- Data Preprocessing
- Feature Scaling
- Model Evaluation
- Responsive Design
- Fast Prediction System

---

## 🛠 Technologies Used

### Programming Language

- Python 3.11

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Web Development

- Flask
- HTML5
- CSS3
- JavaScript

### Model Storage

- Pickle

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
OptiCrop/
│
├── app.py
├── wsgi.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
│
├── data/
│   └── Crop_data.csv
│
├── ml/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate.py
│   ├── model_comparison.py
│   └── graph_dashboard.py
│
├── utils/
│   └── predictor.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/charan2395/OptiCrop.git
```

### Move to Project

```bash
cd OptiCrop
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Clean Missing Values
3. Feature Scaling
4. Train Multiple ML Models
5. Compare Accuracy
6. Select Best Model
7. Save Model (.pkl)
8. Deploy Using Flask

---

## 📊 Input Parameters

| Feature | Description |
|----------|-------------|
| Nitrogen | Soil Nitrogen Level |
| Phosphorous | Soil Phosphorous Level |
| Potassium | Soil Potassium Level |
| Temperature | Temperature (°C) |
| Humidity | Relative Humidity (%) |
| pH | Soil pH |
| Rainfall | Rainfall (mm) |

---

## 🌾 Output

The application predicts the most suitable crop for the given environmental and soil conditions.

Example:

```
Recommended Crop

Rice
```

---

## 📈 Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- K-Means Clustering (Comparison)

---

## 👨‍💻 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation
- Disease Prediction
- Crop Yield Prediction
- Soil Image Analysis
- Multilingual Support
- Farmer Dashboard
- Cloud Deployment
- Mobile Application

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

### Prediction Page

(Add Screenshot Here)

---

## 🚀 Deployment

The project can be deployed on:

- Streamlit Community Cloud
- Render
- Railway
- PythonAnywhere

---

## 📄 License

This project is developed for educational and internship purposes.

---

## 👤 Author

**Charan**

GitHub:
https://github.com/charan2395

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
