file = open("readme.md", "r")
print(type(file))
file.close()

#-----------------------------------------------------------

# OLD / RISKY WAY:
file = open("readme.md", "r")
data = file.read()
# If an error happens HERE, file.close() is never reached!
file.close()


#-----------------------------------------------------------


# PROFESSIONAL / SAFE WAY:
with open("readme.md", "r") as file:
    file = file.read()

print(file)
# File automatically closes HERE, even if an error occurs inside the block!


#-----------------------------------------------------------

#Let's say an oscilloscope saves voltage measurements to telemetry.csv

# 1. Writing dummy telemetry data
time_stamps = [0.00, 0.01, 0.02, 0.03]
voltages = [0.12, 1.45, 3.20, 4.95]

with open("telemetry.csv", "w") as f:
    f.write("Time(s),Voltage(V)\n")  # Write header line
    for t, v in zip(time_stamps, voltages):
        f.write(f"{t},{v}\n")

# 2. Reading and extracting data line-by-line
times = []
volts = []

with open("telemetry.csv", "r") as f:
    header = f.readline()  # Read and skip the first line (Header: Time(s),Voltage(V))
    
    for line in f:
        cleaned_line = line.strip()  # Removes trailing white space and newline (\n)
        if cleaned_line:  # Ensure line is not empty
            t_str, v_str = cleaned_line.split(",")  # Split by comma
            times.append(float(t_str))  # Convert string to float
            volts.append(float(v_str))

print("Extracted Voltages:", volts)  # Output: [0.12, 1.45, 3.2, 4.95]

