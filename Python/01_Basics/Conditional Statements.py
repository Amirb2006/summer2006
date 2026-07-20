frequency = 49.2

if frequency < 49.5:
    print("CRITICAL: Frequency drop! Triggering protection system.")
elif frequency > 50.5:
    print("WARNING: Over-frequency detected.")
else:
    print("Grid is stable.")

#-----------------------------------------------------------

"""
Imagine you are processing an electrocardiogram (ECG) biosignal.
The list below contains peak voltage values from a heart rate monitor.
You need to write a loop that checks each peak value.
If a peak is strictly greater than 2.0 Volts , it is classified as an "Anomaly".
Otherwise, it is "Normal".

ecg_peaks = [1.2, 2.4, 1.1, 3.2, 1.8]

"""

ecg_peaks = [1.2, 2.4, 1.1, 3.2, 1.8]

for peak in ecg_peaks:
    if peak > 2.0:
        print("peak in anomal")
    else:
        print("peak is normal")