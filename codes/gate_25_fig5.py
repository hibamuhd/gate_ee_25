import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
f = 1  # Frequency of the sine wave (in Hz)
t = np.linspace(0, 5, 5000)  # Time vector (from 0 to 5 seconds with 5000 points)
Vo = 5  # Amplitude of the sine wave (in volts)

# Calculate the sine wave
y = Vo * np.sin(2 * np.pi * f * t)

# Create a mask for positive and negative values of y
mask_positive = y >= 0
mask_negative = y < 0

# Plot the positive part of the sine wave in solid line
plt.plot(t[mask_positive], y[mask_positive], linestyle='-', color='black',label='y=sin')

# Plot the negative part of the sine wave in dashed line
plt.plot(t[mask_negative], y[mask_negative], linestyle='--', color='black')

plt.ylabel('Voltage (Vo)')
plt.grid(False)

# Add a horizontal line at y=0
plt.axhline(0, color='black', linestyle='--')

plt.legend()
plt.savefig('gate_25_fig5.png')
plt.show()

