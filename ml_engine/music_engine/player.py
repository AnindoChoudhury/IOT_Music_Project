import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None
        self.current_song_path = None
        self.is_playing = False
        
    def play_song(self, file_path):
        if not file_path or not os.path.exists(file_path):
            print("Invalid file path:", file_path)
            return False
            
        # Don't restart if it's already playing the same song
        if self.current_song_path == file_path and self.is_playing:
            return True
            
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(-1) # Loop indefinitely
            self.current_song = os.path.basename(file_path)
            self.current_song_path = file_path
            self.is_playing = True
            print(f"Playing: {self.current_song}")
            return True
        except Exception as e:
            print(f"Error playing {file_path}: {e}")
            return False
            
    def pause_song(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            return True
        return False
            
    def resume_song(self):
        if self.current_song and not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True
            return True
        elif self.current_song_path:
            return self.play_song(self.current_song_path)
        return False
            
    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.current_song = None
        self.current_song_path = None
        return True

player = MusicPlayer()
