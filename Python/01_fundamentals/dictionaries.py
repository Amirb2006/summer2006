# Sensor configuration dictionary
sensor_config = {
    "sensor_id": "ADC_01",
    "sampling_rate": 1000,  # Hz
    "gain": 1.5,
    "active": True
}

# Accessing values by key
fs = sensor_config["sampling_rate"]
print(f"Sampling frequency: {fs} Hz")

# Adding or updating keys
sensor_config["calibration_offset"] = 0.02
sensor_config["active"] = False

# Iterating through key-value pairs
for key, value in sensor_config.items():
    print(f"{key} -> {value}")