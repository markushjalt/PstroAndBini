import numpy as np
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Tom", "red", 30)
r1.introduce_self()

x = np.linspace(-2*np.pi, 2*np.pi, 100)
x_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
x_labels = ['-2π', '-π', 0, 'π', '2π']

y = np.sin(x)

plt.plot(x,y)
plt.xticks(x_ticks, x_labels)
plt.grid()
plt.show()

