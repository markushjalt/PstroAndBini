import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the sine wave
amplitude = 1
frequency = 10
phase = 0

# Define the sampling rate and duration
sampling_rate = 1000
duration = 1

# Generate the time vector
time = np.arange(0, duration, 1/sampling_rate)

# Generate the sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + phase)

# Plot the sine wave
plt.plot(time, sine_wave)
# plt.plot(time,2*np.pi*frequency*time)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()