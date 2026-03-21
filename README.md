# Emotion Music AI

A full-stack Python application that predicts a user's emotional state using physiological sensor inputs and environmental data, then automatically plays music corresponding to that emotion.

## Prerequisites

- **Python 3.8+** installed on your system.
- Basic understanding of running commands in a terminal (Command Prompt or PowerShell).

## Installation

1. **Clone or Download the Repository**
   Ensure you have the project files on your local machine.

2. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```powershell
   pip install -r requirements.txt
   ```
   *(Optional but recommended: It is good practice to do this inside a virtual environment).*

## Running the Application

1. **Start the Backend Server**
  Navigate to the root directory
```bash
python app.py
```
2. **Start the frontend**
   Navigate to utils/frontend
   ```bash
      npm run dev
   ```
3. **Access the Web Interface**
   Once the server is running, open your favorite web browser and navigate to:
   [http://localhost:8000/](http://localhost:8000/)

## Project Structure

- `app/`: Core Flask application and routing.
- `data/`: Datasets or collected data logs.
- `ml_model/`: Machine learning model predicting emotions based on sensor input.
- `music_engine/`: Module responsible for managing and playing songs.
- `sensors/`: Simulated hardware interfaces capturing physiological/environmental data.
- `utils/`: Frontend assets (React) and Music Recommender
