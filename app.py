from flask import Flask, jsonify
from flask_cors import CORS
import requests
import pickle
import os
from utils.backend.music_player import get_video_id_for_emotion

app = Flask(__name__)
CORS(app)


MODEL_PATH = os.path.join(os.path.dirname(__file__), "ml_model", "model.pkl")

# CONFIGURATION
THINGSPEAK_CHANNEL_ID = "3284630"
THINGSPEAK_READ_KEY = "CG1Z4WO9IN3HSKHP"

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
        print("✅ ML Model loaded successfully!")
except Exception as e:
    print(f"⚠️ Warning: Could not load model. Error: {e}")
    model = None


@app.route("/api/analyze", methods=["GET"])
def analyze_and_play():
    print("Frontend requested an analysis...")

    if model is None:
        return jsonify({"status": "error", "message": "ML Model is offline."}), 500

    try:
        # STEP 1: Fetch live data from ThingSpeak
        ts_url = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?api_key={THINGSPEAK_READ_KEY}&results=1"

        response = requests.get(ts_url)
        data = response.json()

        # Extract the most recent reading (the last item in the list)
        latest_feed = data["feeds"][0]

        # If ThingSpeak is empty, default to 0 to prevent crashes
        temperature = float(latest_feed.get("field1") or 0)
        humidity = float(latest_feed.get("field2") or 0)
        heartbeatrate = float(latest_feed.get("field3") or 0)
        skinsensitivity = float(latest_feed.get("field4") or 0)

        print(
            f"Live Data Caught -> temp : {temperature}, humidity: {humidity}, heartbeat: {heartbeatrate}, skinsensitivity:{skinsensitivity}"
        )

        #    ML Prediction

        live_sensor_array = [[temperature, humidity, heartbeatrate, skinsensitivity]]

        prediction = model.predict(live_sensor_array)
        emotion = prediction[0]
        videoid = get_video_id_for_emotion(emotion)
        print(f"Emotion Detected: {emotion}")

        print(f"Emotion Detected by ML: {emotion}")
        # Frontend Connect
        return jsonify(
            {
                "status": "success",
                "biometrics": {
                    "heart_rate": heartbeatrate,
                    "skinsensitivity": skinsensitivity,
                    "temperature": temperature,
                    "humidity": humidity,
                },
                "emotion": emotion,
                "videoid": videoid,
            }
        )

    except Exception as e:
        # If anything goes wrong (like no internet), don't crash the server!
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    print("Resonance Backend Server is running on Port 5000")
    app.run(debug=True, port=5000)
