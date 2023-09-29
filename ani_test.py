import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')




# Define the update function
def update(num, ax):
    ax.view_init(elev=10., azim=num)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), fargs=(ax,))

# Save the animation
ani.save('3d_animation.gif', writer='ffmpeg')

plt.show()