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
        {"name": "Calm Resting", "data": [[36.5, 100.0, 90.0, 300]]},
    ]

    print("\n--- Running Predictions ---")
    for test in test_cases:
        prediction = model.predict(test["data"])
        print(f"Scenario: {test['name']}")
        print(f"Input Data: {test['data'][0]}")
        print(f"Predicted Emotion: -> **{prediction[0]}** <-\n")


if __name__ == "__main__":
    test_model()
