import os
import random

class MusicRecommender:
    def __init__(self):
        self.basedir = os.path.dirname(os.path.abspath(__file__))
        self.playlists_dir = os.path.join(self.basedir, 'playlists')
        
    def recommend(self, emotion: str):
        emotion = emotion.lower()
        folder = os.path.join(self.playlists_dir, emotion)
        
        if not os.path.exists(folder):
            return None
            
        songs = [f for f in os.listdir(folder) if f.endswith(('.mp3', '.wav'))]
        if not songs:
            return None
            
        selected = random.choice(songs)
        return os.path.join(folder, selected)

recommender = MusicRecommender()
