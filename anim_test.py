import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the plot for animation
def update(frame):
    plt.clf()  # Clear the previous frame
    x = np.linspace(0, 2 * np.pi, 1000)  # X values for the sine wave
    y = np.sin(x - 0.1 * frame)  # Update the sine wave with a phase shift
    y2 = np.cos(x - 0.1 * frame)
    y3 = np.sin(x - 0.1 * frame + np.pi)
    plt.plot(x, y, label='Sine Wave', color = 'blue')
    plt.plot(x, y2, label = 'Cos Wave', color = 'red')
    plt.plot(x, y3, label = 'Third', color = 'magenta')
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1.2, 1.2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Moving Waves Animation')
    plt.legend()

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Create an animation
ani = FuncAnimation(fig, update, frames=100, repeat=False, blit=False, interval=50)
#ani.save('moving_sine_wave.gif', writer='pillow', fps=30)

plt.show()
