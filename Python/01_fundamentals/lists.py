# A list representing current readings from a circuit (in Amperes)
current_readings = [1.2, 2.5, 0.8, 3.1, 1.9]

# 1. Access and print the second reading (2.5)
second_reading = current_readings[1]
print("The second reading is:", second_reading)

# 2. Access and print the very last reading using a negative index
last_reading = current_readings[-1]
print("The last reading is:", last_reading)

# 3. Python has a built-in function called len() that returns the total number of items.
# Print the total number of readings in the list.

total_items = len(current_readings)
print("Total number of samples:", total_items)

#--------------------------------------------------------------------------

# A sequence of signal amplitudes
signal_data = [0.1, 0.2, 1.5, 9.8, 8.7, 1.2, 0.3, 0.2]

# 1. Slice the "anomaly" from index 2 up to and including index 4 (values: 1.5, 9.8, 8.7)
# Remember: the stop index must be one higher than the index you want to include!
anomaly_window = signal_data[2:5]
print("The anomaly window is:", anomaly_window)

# 2. Shortcut trick: If you leave the start empty like [:3], Python starts from the beginning.
# Slice the first 3 elements of the signal using this shortcut.
first_three = signal_data[:2]
print("The first three samples are:", first_three)