

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

#------------------------------------------------------------------------------------------

try:
    # 1. CODE THAT MIGHT FAIL
    result = 100 / user_input
except ZeroDivisionError:
    # 2. RUNS ONLY IF ZeroDivisionError OCCURS
    print("Handled: Division by zero is undefined. Returning 0.")
    result = 0
except TypeError:
    # 3. RUNS ONLY IF INPUT TYPE IS WRONG (e.g., string instead of float)
    print("Handled: Input must be a valid number.")
    result = None
else:
    # 4. RUNS ONLY IF NO EXCEPTIONS OCCURRED AT ALL
    print("Calculation completed successfully!")
finally:
    # 5. ALWAYS RUNS NO MATTER WHAT (Cleanup code, releasing hardware resources)
    print("Operation finished.\n")

#---------------------------------------------------------------------------------
#raise Exception("This is a custom exception message.")  # Uncomment to raise a custom exception

def check_junction_temp(temp_celsius):
    if temp_celsius > 125.0:
        # Manually throw an exception to stop thermal runaway
        raise ValueError(f"CRITICAL OVERHEAT: {temp_celsius}°C exceeds max rating (125°C)!")
    return "Temperature nominal."

try:
    print(check_junction_temp(140.0))
except ValueError as error_msg:
    print(f"ALERT: {error_msg}")
