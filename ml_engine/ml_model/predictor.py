import os
import pickle
import pandas as pd


class EmotionPredictor:
    def __init__(self):
        # 1. Get the directory where predictor.py is located
        # Currently: emotion-music-ai/ml_engine/ml_model/
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 2. Go UP TWO folder levels to reach the main project root
        # Currently: emotion-music-ai/
        project_root = os.path.dirname(os.path.dirname(current_dir))

        # 3. Build the correct path to the model file
        # Target: emotion-music-ai/ml_model/model.pkl
        self.model_path = os.path.join(project_root, "ml_model", "model.pkl")
        self.model = None

        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
            print(f"EmotionPredictor: Successfully loaded model from {self.model_path}")
        else:
            print(
                f"Warning: Model not found at {self.model_path}. Please run training.py first."
            )

    def predict(self, temperature, humidity, heart_rate, skin_conductivity):
        # Safety check in case the model failed to load
        if not self.model:
            return "Error: Model not loaded."

        # Wrap the incoming raw numbers into a Pandas DataFrame
        features = pd.DataFrame(
            [[temperature, humidity, heart_rate, skin_conductivity]],
            columns=["temperature", "humidity", "heart_rate", "skin_conductivity"],
        )

        # Make the prediction and return the single result
        prediction = self.model.predict(features)
        return prediction[0]


# Initialize the Singleton instance
predictor = EmotionPredictor()