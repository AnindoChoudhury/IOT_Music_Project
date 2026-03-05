import os
import wave
import struct
import math

def generate_tone(filename, frequency, duration=3.0, volume=0.5):
    sample_rate = 44100.0
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1) # mono
        wav_file.setsampwidth(2) # 16-bit
        wav_file.setframerate(sample_rate)
        
        for i in range(int(sample_rate * duration)):
            value = int(volume * 32767.0 * math.sin(frequency * math.pi * 2 * (i / sample_rate)))
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

basedir = os.path.dirname(os.path.abspath(__file__))
emotions = {
    'stressed': 880, # higher pitch
    'calm': 220,     # low pitched
    'happy': 440,    # mid pitch A4
    'sad': 150,      # very low
    'workout': 1200  # very high
}

for emotion, freq in emotions.items():
    folder = os.path.join(basedir, 'playlists', emotion)
    os.makedirs(folder, exist_ok=True)
    generate_tone(os.path.join(folder, f'dummy_{emotion}.wav'), freq, duration=3.0)
    print(f"Created {emotion} dummy track.")
