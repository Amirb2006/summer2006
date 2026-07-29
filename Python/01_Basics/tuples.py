# Defining a tuple for a 3-phase AC voltage configuration (RMS values)
grid_phases = (230.0, 230.0, 230.0)  # L1, L2, L3

# Returning multiple values from a function
def get_signal_stats(signal):
    v_min = min(signal)
    v_max = max(signal)
    return v_min, v_max  # Returns a tuple: (v_min, v_max)

min_val, max_val = get_signal_stats([10.1, 12.5, 9.8, 11.2])
print(f"Min: {min_val}V, Max: {max_val}V")

#----------------------------------------------------------------------------
#changing tuples
# Tuples are immutable, so you cannot change their elements directly
#but we can convert them to a list, modify the list, and convert it back to a tuple
# Example: Changing the second phase voltage

print(grid_phases)  # Output: (230.0, 230.0, 230.0)

phase_list = list(grid_phases)  # Convert tuple to list
phase_list[1] = 240.0  # Change L2 voltage to 240       
grid_phases = tuple(phase_list)  # Convert list back to tuple

print(grid_phases)  # Output: (230.0, 240.0, 230.0)

#-----------------------------------------------------------------------------
#Adding items to a tuple
# Since tuples are immutable, we cannot add items directly. 
# However, we can add item with a similar method to changing a tuple
#we conver the tuple to a list, append the new item, and convert it back to a tuple
new_phase = 220.0  # New phase voltage to add
grid_phase = list(grid_phases)  # Convert tuple to list
grid_phase.append(new_phase)  # Append new phase voltage
grid_phase = tuple(grid_phase)  # Convert list back to tuple




