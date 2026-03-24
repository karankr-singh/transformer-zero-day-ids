import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


def load_dataset(file_path):
    """
    Load NSL-KDD / CICIDS dataset from CSV file
    """
    df = pd.read_csv(file_path)
    print(f"[INFO] Dataset loaded with shape: {df.shape}")
    return df


def preprocess_data(df):
    """
    Preprocess the dataset:
    - Handle categorical features
    - Normalize numerical features
    - Encode labels
    """

    
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    categorical_cols = X.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("[INFO] Preprocessing completed")
    return X_scaled, y


def split_data(X, y, test_size=0.2):
    """
    Split dataset into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    print("[INFO] Data split completed")
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    # Example usage 
    dataset_path = "../data/NSL_KDD.csv"

    df = load_dataset(dataset_path)
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
