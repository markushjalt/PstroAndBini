import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
#from matplotlib.animation import FFMpegWriter

fig = plt.figure()
l, = plt.plot([], [], 'k-')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(x):
    return 3 * np.sin(x)

metadata = dict(title = 'Movie', artist = 'Bini')
writer = PillowWriter(fps = 15, metadata=metadata)

xlist = []
ylist = []

with writer.saving(fig, "sinWave.gif", 100):
    for xval in np.linspace(-5, 5, 100):
        xlist.append(xval)
        ylist.append(func(xval))

        l.set_data(xlist, ylist)

        writer.grab_frame()
        