import os
import pickle
import pandas as pd

class EmotionPredictor:
    def __init__(self):
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(basedir, "ml_model", "model.pkl")
        self.model = None
        self.load_model()
        
    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            print(f"Warning: Model not found at {self.model_path}.")
            
    def predict(self, temperature, humidity, heart_rate, skin_conductivity):
        if not self.model:
            return "Unknown"
            
        # Create a dataframe to match the expected feature names
        features = pd.DataFrame([[temperature, humidity, heart_rate, skin_conductivity]], 
                              columns=["temperature", "humidity", "heart_rate", "skin_conductivity"])
                              
        prediction = self.model.predict(features)
        return prediction[0]

# Singleton instance for easy import
predictor = EmotionPredictor()
