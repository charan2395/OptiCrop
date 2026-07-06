import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):
    """Load dataset"""
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """
    Handle missing values safely (NO inplace warnings)
    """

    # Numeric columns → fill with mean
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # Categorical columns → fill with mode
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def split_features(df):
    """Split dataset into features and target"""
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y


def scale_features(X):
    """
    Feature scaling for ML models
    (important for KNN, Logistic Regression, etc.)
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


def preprocess_pipeline(path):
    """
    Full preprocessing pipeline:
    load → clean → split → scale
    """
    df = load_data(path)
    df = clean_data(df)

    X, y = split_features(df)
    X_scaled, scaler = scale_features(X)

    return X_scaled, y, scaler