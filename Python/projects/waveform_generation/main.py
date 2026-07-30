import numpy as np


# Create 1000 equally spaced time points between 0 and 0.1 seconds
t = np.linspace(0, 0.1, 1000)

#----------------------------------

"""
We are going to generate 500 time samples between 0 and 0.04 seconds 
(which represents exactly two full periods of a 50 Hz wave).
Then, we will compute the sine wave values for every single point
instantly without a loop

"""

# 1. Define signal parameters
f = 50  # Frequency in Hz
omega = 2 * np.pi * f  # NumPy has its own built-in pi value!

# 2. Generate 500 time points between 0 and 0.04 seconds using linspace
t = np.linspace(0,0.04,500)

# 3. Calculate the sine wave values for all points at once.
# Hint: Use np.sin() instead of math.sin() so it works on the whole array!
v_t = 220 * np.sin(omega * t)

# 4. Print the shape (size) of your v_t array to confirm it has 500 points
print("Array size:", v_t.shape)

# 5. Print just the first 5 calculated voltage values using slicing
print("First 5 values:", v_t[:5])