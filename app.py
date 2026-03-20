from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This allows your React frontend to talk to this Flask server safely
CORS(app)

# CONFIGURATION
THINGSPEAK_CHANNEL_ID = "3284630"
THINGSPEAK_READ_KEY = "CG1Z4WO9IN3HSKHP"


@app.route("/api/analyze", methods=["GET"])
def analyze_and_play():
    print("Frontend requested an analysis...")

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
            f"🫀 Live Data Caught -> temp : {temperature}, humidity: {humidity}, heartbeat: {heartbeatrate}, skinsensitivity:{skinsensitivity}"
        )

        #    ML Prediction

        if heartbeatrate > 100 or skinsensitivity > 3000:
            emotion = "Stressed"
            video_id = "5qap5aO4i9A"  # Calming Lo-Fi audio
        elif heartbeatrate < 60:
            emotion = "Calm"
            video_id = "jfKfPfyJRdk"  # Chill relaxed audio
        else:
            emotion = "High Energy"
            video_id = "gOsM-DYAEhY"  # Upbeat/Workout audio

        print(f"Emotion Detected: {emotion}")

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
                "video_id": video_id,
            }
        )

    except Exception as e:
        # If anything goes wrong (like no internet), don't crash the server!
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    print("Resonance Backend Server is running on Port 5000")
    app.run(debug=True, port=5000)
