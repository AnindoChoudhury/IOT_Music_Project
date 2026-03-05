import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train():
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(basedir, "data", "emotion_dataset.csv")
    model_dir = os.path.join(basedir, "ml_model")
    model_path = os.path.join(model_dir, "model.pkl")
    
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}. Please run dataset_generator.py first.")
        return
        
    df = pd.DataFrame(pd.read_csv(data_path))
    
    X = df[["temperature", "humidity", "heart_rate", "skin_conductivity"]]
    y = df["emotion"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training RandomForestClassifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Model accuracy: {acc * 100:.2f}%")
    print(classification_report(y_test, y_pred))
    
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
        
    print(f"Model successfully saved to {model_path}.")

if __name__ == "__main__":
    train()
