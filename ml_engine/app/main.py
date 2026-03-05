from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.router import api_router
from app.config import config
import os

app = FastAPI(title="Emotion Music AI Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

# Ensure UI directory exists before mounting
os.makedirs(config.UI_DIR, exist_ok=True)
app.mount("/", StaticFiles(directory=config.UI_DIR, html=True), name="ui")
