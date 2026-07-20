import numpy as np
import matplotlib.pyplot as plt

f = 50  
omega = 2 * np.pi * f  
t = np.linspace(0, 0.04, 500)

# 1. Clean signal
v_clean = 220 * np.sin(omega * t)

# 2. Generate Gaussian noise with a standard deviation (amplitude) of 25
# Syntax: np.random.normal(loc=0.0, scale=amplitude, size=num_points)
noise = np.random.normal(0, 25, 500)

# 3. Add the noise array to the clean signal array instantly
v_noisy = v_clean + noise

# --- Plotting Both Signals ---
plt.figure(figsize=(10, 5)) # Makes the plot window slightly wider

# Plot the noisy signal in red
plt.plot(t, v_noisy, color="red", alpha=0.6, label="Noisy Signal")

# Plot the clean signal in blue on top of it
plt.plot(t, v_clean, color="blue", linewidth=2, label="Clean Signal")

plt.title("Real-World Signal Simulation (Clean vs. Noisy)")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Volts)")
plt.grid(True)
plt.legend() # Shows the labels/colors box on the graph
plt.show()