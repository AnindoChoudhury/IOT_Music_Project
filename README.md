# Emotion Music AI

A full-stack Python application that predicts a user's emotional state using physiological sensor inputs and environmental data, then automatically plays music corresponding to that emotion.

## Prerequisites

- **Python 3.8+** installed on your system.
- Basic understanding of running commands in a terminal (Command Prompt or PowerShell).

## Installation

1. **Clone or Download the Repository**
   Ensure you have the project files on your local machine.

2. **Navigate to the Project Directory**
   Open your terminal and navigate to the root folder of the project:
   ```powershell
   cd "c:\Users\KIIT0001\OneDrive\Desktop\python-prac\IOT project\emotion-music-ai"
   ```

3. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```powershell
   pip install -r requirements.txt
   ```
   *(Optional but recommended: It is good practice to do this inside a virtual environment).*

## Running the Application

1. **Start the Backend Server**
   Start the FastAPI server using `uvicorn`:
   ```powershell
   uvicorn app.main:app --reload
   ```
   The `--reload` flag allows the server to automatically restart if you make any changes to the code.

2. **Access the Web Interface**
   Once the server is running, open your favorite web browser and navigate to:
   [http://localhost:8000/](http://localhost:8000/)

## Project Structure

- `app/`: Core FastAPI application and routing.
- `data/`: Datasets or collected data logs.
- `ml_model/`: Machine learning model predicting emotions based on sensor input.
- `music_engine/`: Module responsible for managing and playing songs.
- `sensors/`: Simulated hardware interfaces capturing physiological/environmental data.
- `ui/`: Frontend assets (HTML, CSS, JS) served as static files.
