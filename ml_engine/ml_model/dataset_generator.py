import pandas as pd
import numpy as np
import os

def generate_dataset(num_samples_per_class=1000):
    # Determine the project root to properly place the file 
    # (assuming this script is run from project root or inside ml_model)
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(basedir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Emotion categories
    emotions = ["Stressed", "Calm", "Happy", "Sad", "Workout"]
    
    data = []
    
    for emotion in emotions:
        for _ in range(num_samples_per_class):
            if emotion == "Stressed":
                hr = np.random.normal(110, 10)
                skin = np.random.normal(8, 1)
                temp = np.random.normal(28, 5)
                hum = np.random.normal(70, 10)
            elif emotion == "Calm":
                hr = np.random.normal(70, 5)
                skin = np.random.normal(2, 1)
                temp = np.random.normal(22, 2)
                hum = np.random.normal(50, 5)
            elif emotion == "Happy":
                hr = np.random.normal(85, 5)
                skin = np.random.normal(4.5, 1)
                temp = np.random.normal(24, 2)
                hum = np.random.normal(50, 5)
            elif emotion == "Sad":
                hr = np.random.normal(65, 5)
                skin = np.random.normal(1.5, 0.5)
                temp = np.random.normal(20, 3)
                hum = np.random.normal(60, 10)
            elif emotion == "Workout":
                hr = np.random.normal(130, 8)
                skin = np.random.normal(7, 1.5)
                temp = np.random.normal(30, 3)
                hum = np.random.normal(60, 10)
                
            # Clip bounds
            temp = np.clip(temp, 18, 35)
            hum = np.clip(hum, 30, 90)
            hr = np.clip(hr, 60, 140)
            skin = np.clip(skin, 0.5, 10)
            
            data.append([temp, hum, hr, skin, emotion])
            
    df = pd.DataFrame(data, columns=["temperature", "humidity", "heart_rate", "skin_conductivity", "emotion"])
    
    # Shuffle dataset
    df = df.sample(frac=1).reset_index(drop=True)
    
    output_path = os.path.join(data_dir, "emotion_dataset.csv")
    df.to_csv(output_path, index=False)
    print(f"Dataset successfully generated at {output_path} with {len(df)} samples.")

if __name__ == "__main__":
    generate_dataset()
