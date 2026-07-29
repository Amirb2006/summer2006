import numpy as np

# A small array representing 6 noisy voltage samples
v_noisy = np.array([10.2, 12.8, 9.5, 11.1, 10.0, 13.2])

v_filtered = []

# Loop through the array starting from index 2 so we always have 3 points to average
for i in range(2, len(v_noisy)):
    # Take the average of current point and the 2 points before it
    avg = (v_noisy[i-2] + v_noisy[i-1] + v_noisy[i]) / 3
    v_filtered.append(avg) #description for append

#np.append is so inefficent so we use list.append which is faster than we convert
# the list into an array using np.array()

v_filtered = np.array(v_filtered)  # Convert the list back to a NumPy array for easier handling

print("Original:", v_noisy)
print("Filtered:", v_filtered)

"""
Definition and Usage
The append() method appends (adds) an element to the end of the list.
---------------------------
Syntax
list.append(elmnt)
---------------------------
Parameter Values 

Parameter	        Description
elmnt	            Required. An element of any type (string, number, object etc.)
"""

#-----------------------------------------------------------

#To create a 5-point moving average filter, we define a filter kernel 
#(a small array of weights):For 5 points, the weights are simply [0.2, 0.2, 0.2, 0.2, 0.2]
# since 1 / 5 = 0.2.

window_size = 5
kernel = np.ones(window_size) / window_size  # Creates array: [0.2, 0.2, 0.2, 0.2, 0.2]

# Apply the filter instantly!
v_filtered = np.convolve(v_noisy, kernel, mode='same')

"""
The numpy.convolve function computes the discrete, linear convolution of
two one-dimensional sequences.
It takes three main parameters:
a (the first input array), v (the second input array),
and an optional mode string ('full', 'same', or 'valid').
Function Parametersa: 
First one-dimensional input array of length M.
v: Second one-dimensional input array of length N.
mode: Controls the size of the output:

1. 'full': Returns the full convolution,
    evaluating all points of overlap (default length M + N - 1).

2. 'same': Returns an output of length max(M, N),
    matching the size of the largest input array (centered).

3. 'valid': Returns only those values that do not rely on zero-padding, 
    meaning edges where the smaller array completely overlaps 
    the larger one (length (max(M, N) - min(M, N) + 1)



"""
#-----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.04, 400)
f = 50 
omega = 2 * np.pi * f

v_rectified = np.abs(15 * np.sin(omega * t))
noise = np.random.normal(0, 0.4, 400)
v_noisy = v_rectified + noise

# --- Create the Moving Average Filter ---
window_size = 9  # a 9-point window to smooth out noise
kernel = np.ones(window_size) / window_size

# Apply np.convolve using v_noisy and kernel with mode='same'

v_filtered = np.convolve(v_noisy, kernel, mode='same')

# --- 3. Plotting ---
plt.figure(figsize=(10, 5))

# Plot the noisy signal in light gray/red background
plt.plot(t, v_noisy, color="gray", alpha=0.5, label="Noisy Signal")

# Plot the ideal clean signal in dashed blue
plt.plot(t, v_rectified, color="blue", linestyle="--", label="Ideal Clean Signal")

# Plot your newly filtered signal in solid green!
plt.plot(t, v_filtered, color="green", linewidth=2, label="Filtered (Moving Avg)")

plt.title("Digital Signal Processing: Moving Average Filter")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()