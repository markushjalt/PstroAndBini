import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter



# Fixing random state for reproducibility
#np.random.seed(19680801)


metadata = dict(title='Movie', artist='Bini')
writer = PillowWriter(fps=10, metadata=metadata)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(r,t):
    return np.cos(r/2+t)*np.exp(-np.square(r)/50)

xvec = np.linspace(-10, 10, 1000)
yvec = np.linspace(-10, 10, 1000)

xlist, ylist = np.meshgrid(xvec, yvec)

rlist = np.sqrt( np.square(xlist) + np.square(ylist) )

with writer.saving(fig, "exp3d.gif", 100):
    for tval in np.linspace(0,20,40):
        print(tval)
        zval = func(rlist, tval)
        ax.set_zlim(-1, 1)
        ax.plot_surface(xlist,ylist,zval,cmap=cm.viridis)

        writer.grab_frame()

        plt.cla()

