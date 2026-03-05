const API_BASE = '/api';

const emojis = {
    'Unknown': '❓',
    'Calm': '😌',
    'Happy': '😊',
    'Stressed': '😫',
    'Workout': '🔥',
    'Sad': '😢'
};

const gradients = {
    'Unknown': 'var(--grad-unknown)',
    'Calm': 'var(--grad-calm)',
    'Happy': 'var(--grad-happy)',
    'Stressed': 'var(--grad-stressed)',
    'Workout': 'var(--grad-workout)',
    'Sad': 'var(--grad-sad)'
};

// DOM Elements
const body = document.getElementById('app-body');
const statusDot = document.getElementById('monitoring-status-dot');
const statusText = document.getElementById('monitoring-status-text');

const elEmoji = document.getElementById('emotion-emoji');
const elEmotion = document.getElementById('emotion-text');
const elSong = document.getElementById('current-song');

const elTemp = document.getElementById('val-temp');
const elHum = document.getElementById('val-hum');
const elHr = document.getElementById('val-hr');
const elSkin = document.getElementById('val-skin');

let pollingInterval = null;

// API Calls
async function fetchState() {
    try {
        const res = await fetch(`${API_BASE}/state`);
        const data = await res.json();
        updateUI(data);
    } catch (e) {
        console.error("Error fetching state:", e);
    }
}

async function startMonitoring() {
    await fetch(`${API_BASE}/start`, { method: 'POST' });
    if(!pollingInterval) {
        pollingInterval = setInterval(fetchState, 3000);
    }
    fetchState();
}

async function stopMonitoring() {
    await fetch(`${API_BASE}/stop`, { method: 'POST' });
    if(pollingInterval) {
        clearInterval(pollingInterval);
        pollingInterval = null;
    }
    fetchState();
}

async function setTrend(emotion) {
    await fetch(`${API_BASE}/simulate-trend`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ emotion })
    });
}

// UI Updates
function updateUI(data) {
    // Status
    if (data.monitoring) {
        statusDot.className = 'dot online';
        statusText.textContent = 'System Online - Live Tracking';
        if(!pollingInterval) pollingInterval = setInterval(fetchState, 3000);
    } else {
        statusDot.className = 'dot offline';
        statusText.textContent = 'System Offline';
    }

    // Emotion
    const emotion = data.current_emotion || 'Unknown';
    elEmotion.textContent = emotion;
    elEmoji.textContent = emojis[emotion] || emojis['Unknown'];
    body.style.backgroundImage = gradients[emotion] || gradients['Unknown'];
    
    // Animate emoji slightly on update
    elEmoji.style.transform = 'scale(1.2)';
    setTimeout(() => elEmoji.style.transform = 'scale(1)', 300);

    // Song
    elSong.textContent = data.current_song || 'No track playing';

    // Sensors
    if (data.sensor_data && data.sensor_data.temperature !== undefined) {
        elTemp.textContent = data.sensor_data.temperature.toFixed(1);
        elHum.textContent = data.sensor_data.humidity.toFixed(1);
        elHr.textContent = data.sensor_data.heart_rate.toFixed(0);
        elSkin.textContent = data.sensor_data.skin_conductivity.toFixed(1);
    } else {
        elTemp.textContent = '--';
        elHum.textContent = '--';
        elHr.textContent = '--';
        elSkin.textContent = '--';
    }
}

// Event Listeners
document.getElementById('btn-start').addEventListener('click', startMonitoring);
document.getElementById('btn-stop-mon').addEventListener('click', stopMonitoring);

document.querySelectorAll('.btn-trend').forEach(btn => {
    btn.addEventListener('click', (e) => {
        setTrend(e.target.dataset.emotion);
    });
});

document.getElementById('btn-play').addEventListener('click', () => fetch(`${API_BASE}/music/play`, {method:'POST'}).then(fetchState));
document.getElementById('btn-pause').addEventListener('click', () => fetch(`${API_BASE}/music/pause`, {method:'POST'}).then(fetchState));
document.getElementById('btn-stop').addEventListener('click', () => fetch(`${API_BASE}/music/stop`, {method:'POST'}).then(fetchState));

// Hit init
fetchState();
