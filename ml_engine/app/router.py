import asyncio
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

from sensors.sensor_reader import get_current_sensor_readings, set_simulation_trend
from ml_model.predictor import predictor
from music_engine.recommender import recommender
from music_engine.player import player
from app.config import config

api_router = APIRouter()

# Global state
app_state = {
    "monitoring": False,
    "current_emotion": "Unknown",
    "sensor_data": {},
    "current_song": None,
}

async def monitoring_loop():
    while app_state["monitoring"]:
        # 1. Read Sensors
        sensor_data = get_current_sensor_readings()
        app_state["sensor_data"] = sensor_data
        
        # 2. Predict Emotion
        emotion = predictor.predict(
            sensor_data["temperature"],
            sensor_data["humidity"],
            sensor_data["heart_rate"],
            sensor_data["skin_conductivity"]
        )
        
        # 3. Handle Emotion Change & Music
        if emotion != app_state["current_emotion"]:
            print(f"Emotion changed: {app_state['current_emotion']} -> {emotion}")
            app_state["current_emotion"] = emotion
            
            # Recommend and play new song
            song_path = recommender.recommend(emotion)
            if song_path:
                player.play_song(song_path)
                app_state["current_song"] = player.current_song
            else:
                player.stop_song()
                app_state["current_song"] = None
                
        await asyncio.sleep(config.READ_INTERVAL_SECONDS)

@api_router.get("/state")
def get_state():
    return app_state

@api_router.post("/start")
def start_monitoring(background_tasks: BackgroundTasks):
    if not app_state["monitoring"]:
        app_state["monitoring"] = True
        background_tasks.add_task(monitoring_loop)
        return {"status": "Monitoring started"}
    return {"status": "Already monitoring"}

@api_router.post("/stop")
def stop_monitoring():
    app_state["monitoring"] = False
    player.stop_song()
    app_state["current_song"] = None
    app_state["current_emotion"] = "Unknown"
    return {"status": "Monitoring stopped"}

class TrendRequest(BaseModel):
    emotion: str

@api_router.post("/simulate-trend")
def simulate_trend(req: TrendRequest):
    allowed = ["Stressed", "Calm", "Happy", "Sad", "Workout"]
    if req.emotion not in allowed:
        raise HTTPException(status_code=400, detail="Invalid emotional trend.")
    set_simulation_trend(req.emotion)
    return {"status": f"Sensors trending towards {req.emotion}"}

@api_router.post("/music/play")
def play_music():
    if player.current_song_path and not player.is_playing:
        player.resume_song()
        return {"status": "Playing"}
    elif app_state["current_emotion"] != "Unknown":
        song_path = recommender.recommend(app_state["current_emotion"])
        if song_path:
            player.play_song(song_path)
            app_state["current_song"] = player.current_song
            return {"status": "Playing"}
    return {"status": "No song to play"}

@api_router.post("/music/pause")
def pause_music():
    player.pause_song()
    return {"status": "Paused"}

@api_router.post("/music/stop")
def stop_music():
    player.stop_song()
    app_state["current_song"] = None
    return {"status": "Stopped"}
