def calculate_impedance(voltage, current):
    try:
        # If current is 0, Python raises a ZeroDivisionError
        z = voltage / current
        return z
    except ZeroDivisionError:
        print("Warning: Current is 0A! Infinite impedance detected.")
        return float('inf')  # Returns infinity safely
    except TypeError:
        print("Error: Inputs must be numerical values.")
        return None

# Test normal execution
print("Z =", calculate_impedance(120, 2))   # Z = 60.0

# Test zero division handling
print("Z =", calculate_impedance(120, 0))   # Safely returns inf without crashing

print("z =", calculate_impedance(120, "a"))