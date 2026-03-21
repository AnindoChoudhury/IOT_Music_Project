import pickle
import os


def test_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    model_path = os.path.join(project_root, "ml_model", "model.pkl")

    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
            print("✅ Model loaded successfully!")
    except FileNotFoundError:
        print("❌ Error: model.pkl not found! Did you run training.py first?")
        return

    test_cases = [
        {"name": "Calm Resting", "data": [[21.5, 37.0, 70.0, 87.0]]},
         {"name": "Stressed mode", "data": [[31.0, 44.0, 97.0, 243.0]]},
         {"name": "Physically Active", "data": [[31.0, 40.0, 97.0, 639.0]]},
         {"name": "Excited Life", "data": [[23.0, 39.0, 72.0, 236]]}
         ]

    print("\n--- Running Predictions ---")
    for test in test_cases:
        prediction = model.predict(test["data"])
        print(f"Scenario: {test['name']}")
        print(f"Input Data: {test['data'][0]}")
        print(f"Predicted Emotion: -> **{prediction[0]}** <-\n")


if __name__ == "__main__":
    test_model()
