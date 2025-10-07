import pandas as pd
import os
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def load_data():
    data_path = os.path.join(get_data_dir(), "diabetes.csv")
    data = pd.read_csv(data_path)
    print(f"Data loaded successfully. Shape: {data.shape}")
    return None

def data_preprocessing(data):
    data_path = os.path.join(get_data_dir(), "diabetes.csv")
    data = pd.read_csv(data_path)
    
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print(f"Data preprocessed. Training: {X_train_scaled.shape[0]}, Test: {X_test_scaled.shape[0]}")
    
    # Save to disk
    data_dir = get_data_dir()
    with open(os.path.join(data_dir, 'X_train.pkl'), 'wb') as f:
        pickle.dump(X_train_scaled, f)
    with open(os.path.join(data_dir, 'X_test.pkl'), 'wb') as f:
        pickle.dump(X_test_scaled, f)
    with open(os.path.join(data_dir, 'y_train.pkl'), 'wb') as f:
        pickle.dump(y_train.values, f)
    with open(os.path.join(data_dir, 'y_test.pkl'), 'wb') as f:
        pickle.dump(y_test.values, f)
    
    print("Preprocessed data saved to disk")
    return None

def separate_data_outputs():
    print("Data already saved to disk in previous task")
    return None

def build_model(filename):
    # Load from disk
    data_dir = get_data_dir()
    with open(os.path.join(data_dir, 'X_train.pkl'), 'rb') as f:
        X_train = pickle.load(f)
    with open(os.path.join(data_dir, 'X_test.pkl'), 'rb') as f:
        X_test = pickle.load(f)
    with open(os.path.join(data_dir, 'y_train.pkl'), 'rb') as f:
        y_train = pickle.load(f)
    with open(os.path.join(data_dir, 'y_test.pkl'), 'rb') as f:
        y_test = pickle.load(f)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    print("Training Random Forest model...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model trained! Accuracy: {accuracy:.4f}")
    
    model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, filename)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")
    return None

def load_model(filename):
    model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    model_path = os.path.join(model_dir, filename)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded from {model_path}")
    return model
