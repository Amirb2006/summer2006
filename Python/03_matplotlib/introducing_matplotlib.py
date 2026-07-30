import numpy as np
import matplotlib.pyplot as plt # Import the plotting library

"""
We are going to generate 500 time samples between 0 and 0.04 seconds 
(which represents exactly two full periods of a 50 Hz wave).
Then, we will compute the sine wave values for every single point
instantly without a loop

"""


f = 50  
omega = 2 * np.pi * f  
t = np.linspace(0, 0.04, 500)

v_t = 220 * np.sin(omega * t)

# --- Plotting the Signal ---
plt.plot(t, v_t, label="AC Voltage") # Plots time on X-axis, voltage on Y-axis
plt.title("50 Hz Sinusoidal Voltage Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Volts)")
plt.grid(True) # Adds an engineering grid to the background
plt.show() # Displays the window with the graph