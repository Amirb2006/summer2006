# A function to calculate electrical power
def calculate_power(voltage, current):
    power = voltage * current
    return power # Sends the result back

# How to use (call) the function:
p1 = calculate_power(220, 5)
print("Power is:", p1) # Output: 1100

#------------------------------------------------------------------------

"""
You are going to build a function that calculates the Root Mean Square (RMS) voltage of
a discrete signal sample.
The formula for the RMS value of a list of numbers is:

V_{rms} = sqrt{frac{1}{N} sum_{n=1}^{N} v[n]^2}

"""

#answer
import math


def V_RMS(voltage_samples):

    squared_Sum = 0
    for i in voltage_samples:
        squared_Sum += i ** 2 

    N = len(voltage_samples)
    mean_square = squared_Sum / N

    v_RMS = math.sqrt(mean_square)

    return v_RMS

v_signal = [10, -5, 12, 0, -8] 
result = V_RMS(v_signal)
print("The RMS voltage of the signal is:", result)