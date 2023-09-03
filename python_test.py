import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


x = np.linspace(-np.pi, np.pi, 200)
y = np.tan(x)

fig, ax = plt.subplots()


fig.set_facecolor("r")
ax.plot(x, y, "--", color = 'm')
ax.set_xlabel("x", fontsize = 12)
ax.set_ylabel("y", fontsize = 12)
ax.set_title("y = tan(x)", fontsize = 14)

plt.show()

# test
