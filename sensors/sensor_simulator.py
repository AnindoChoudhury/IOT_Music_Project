import random
import time

class SensorSimulator:
    def __init__(self):
        # Initial continuous state
        self.state = {
            "temperature": 22.0,
            "humidity": 50.0,
            "heart_rate": 70.0,
            "skin_conductivity": 2.0
        }
        self.trend = "Calm" # Can manually set a trend to force it to simulate specific emotions
        
    def _vary(self, value, min_val, max_val, max_step):
        step = random.uniform(-max_step, max_step)
        return max(min_val, min(value + step, max_val))
        
    def set_trend(self, emotion):
        """Force the simulator towards a specific emotion."""
        self.trend = emotion
        
    def read_sensors(self):
        """Generates realistic simulated sensor values based on current trend."""
        # Environmental changes are slow
        self.state["temperature"] = self._vary(self.state["temperature"], 18, 35, 0.2)
        self.state["humidity"] = self._vary(self.state["humidity"], 30, 90, 1.0)
        
        # Physiological changes depend heavily on the trend
        if self.trend == "Stressed":
            self.state["heart_rate"] = min(self.state["heart_rate"] + random.uniform(1, 5), 140)
            self.state["skin_conductivity"] = min(self.state["skin_conductivity"] + random.uniform(0.1, 0.5), 10.0)
        elif self.trend == "Workout":
            self.state["heart_rate"] = min(self.state["heart_rate"] + random.uniform(2, 8), 140)
            self.state["skin_conductivity"] = min(self.state["skin_conductivity"] + random.uniform(0.2, 0.8), 10.0)
            self.state["temperature"] = min(self.state["temperature"] + random.uniform(0.1, 0.3), 35)
        elif self.trend == "Calm":
            self.state["heart_rate"] = max(self.state["heart_rate"] - random.uniform(1, 4), 60)
            self.state["skin_conductivity"] = max(self.state["skin_conductivity"] - random.uniform(0.1, 0.5), 0.5)
        elif self.trend == "Sad":
            self.state["heart_rate"] = max(self.state["heart_rate"] - random.uniform(0.5, 3), 60)
            self.state["skin_conductivity"] = max(self.state["skin_conductivity"] - random.uniform(0.1, 0.3), 0.5)
        elif self.trend == "Happy":
            # Move towards middle-high
            hr_target = 85
            sc_target = 4.5
            self.state["heart_rate"] += (hr_target - self.state["heart_rate"]) * 0.1 + random.uniform(-2, 2)
            self.state["skin_conductivity"] += (sc_target - self.state["skin_conductivity"]) * 0.1 + random.uniform(-0.2, 0.2)
            
        # Ensure bounds after logic
        self.state["heart_rate"] = max(60, min(self.state["heart_rate"], 140))
        self.state["skin_conductivity"] = max(0.5, min(self.state["skin_conductivity"], 10.0))
            
        return self.state.copy()

simulator = SensorSimulator()

if __name__ == "__main__":
    while True:
        print(f"[{simulator.trend}] -> ", simulator.read_sensors())
        time.sleep(3)
