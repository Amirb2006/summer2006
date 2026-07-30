import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,0.04,400)

f = 50 
omega = 2* np.pi * f

v_rectified = np.abs(15 * np.sin(omega * t))

noise = np.random.normal(0,0.4,400)

v_noisy = v_rectified + noise

plt.plot(t, v_noisy,color ="blue",label = "noisy signal",)
plt.plot(t, v_rectified,color = "red", label = "clean signal")

plt.title("DC power supply simulation")
plt.xlabel("time(s)")
plt.ylabel("voltsge(v)")
plt.grid(True)
plt.legend()
plt.show()