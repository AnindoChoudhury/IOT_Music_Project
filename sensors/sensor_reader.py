from sensors.sensor_simulator import simulator

def get_current_sensor_readings():
    """Wrapper to get readings from the global simulator instance."""
    return simulator.read_sensors()
    
def set_simulation_trend(emotion: str):
    """Wrapper to change the trend of the simulator dynamically."""
    simulator.set_trend(emotion)
