import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def train():

    # 1. Get the directory where training.py is located
    # Currently: emotion-music-ai/ml_engine/ml_model/
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. Go UP TWO folder levels to reach the main project root
    # Currently: emotion-music-ai/
    project_root = os.path.dirname(os.path.dirname(current_dir))

    # 3. Build the correct path to the data file
    data_path = os.path.join(project_root, "data", "sensor_data.xlsx")

    # 4. Target the 'ml_model' folder at the ROOT of your project
    model_dir = os.path.join(project_root, "ml_model")
    model_path = os.path.join(model_dir, "model.pkl")

    # Create the ml_model directory if it doesn't exist yet
    os.makedirs(model_dir, exist_ok=True)

    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Data file not found at {data_path}. Please ensure it is inside the 'data' folder."
        )

    # 2. Load and format the data
    print("Loading data...")
    df = pd.read_excel(data_path, header=2, usecols=[0, 2, 4, 6, 8])
    df.columns = [str(c).strip() for c in df.columns]

    column_mapping = {
        "Temperature": "temperature",
        "Humidity": "humidity",
        "Heart Rate": "heart_rate",
        "GSR": "skin_conductivity",
        "Label": "label",
    }
    df = df.rename(columns=column_mapping)

    expected_features = ["temperature", "humidity", "heart_rate", "skin_conductivity"]

    # 3. Prepare features (X) and target (y)
    X = df[expected_features]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Train the model
    print("Training RandomForestClassifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # 5. Evaluate the model
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nModel accuracy: {acc * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    # 6. Save the model
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)

    print(f"Model successfully saved to {model_path}.")


if __name__ == "__main__":
    train()
