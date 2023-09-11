import numpy as np
import matplotlib.pyplot as plt
import cmath

theta = np.linspace(0,2*np.pi, 100)

g = 2
v = 1
m = 0.1

phi = v*np.exp(theta*1.j)
#THETA, PHI = np.meshgrid(theta, phi)
X, Y = np.meshgrid(phi.real, phi.imag)
#V = g*PHI**4 - m**2*PHI**2
V = g*np.sqrt(X**2 + Y**2)**4 - m**2*np.sqrt(X**2 + Y**2)**2
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#surf = ax.plot_surface(THETA, PHI, V)
surf = ax.plot_surface(X, Y, V)

plt.show()