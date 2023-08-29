import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
y = np.tan(x)

plt.figure(1)
plt.plot(x, y, color = 'm')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = tan(x)", fontsize = 14)
plt.show()