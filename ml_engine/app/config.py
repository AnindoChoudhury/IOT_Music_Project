import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UI_DIR = os.path.join(BASE_DIR, "ui")
    
    # Simulation settings
    READ_INTERVAL_SECONDS = 3

config = Config()
