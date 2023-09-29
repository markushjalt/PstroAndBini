import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import math
import functools


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig1, ax1 = plt.subplots()
line, = ax1.plot(x, y, color='k')

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 2*np.pi, -1, 1])
    return line,

ani1 = animation.FuncAnimation(fig1, func=update, frames=len(x), fargs=[x, y, line],
                              interval=25, blit=True)
#ani.save('test.gif')




eps=0.1
m=2000
n=100
dt=1.0/m
dx=1.0/(n*n)
time=np.zeros(m+1)
for i in range(m+1):
  time[i]=i*dt
space=np.zeros(2*n+1)
for j in range(2*n+1):
  space[j]=(j-n)*dx*n
sol=np.zeros((m+1,2*n+1))
for i in range(m):
  index_i=m-1-i
  for j in range(1,2*n):
    sol[index_i, j] =sol[index_i+1, j]-0.5*dt*math.log(eps+abs(sol[index_i+1, j+1]+sol[index_i+1, j-1]-2*sol[index_i+1, j])/dx)


def update3d(frame, ax, surfaces, xdata, ydata, zdata, anim=False):
    if surfaces and surfaces[0]:
        surfaces[0].remove()
        
    surfaces.clear()
    surf = ax.plot_surface(xdata[:frame, :], ydata[:frame, :], zdata[:frame, :], 
                           cmap=cm.coolwarm, linewidth=0, antialiased=False, animated=anim,
                           vmin=zdata.min(), vmax=zdata.max())
    
    surfaces.append(surf)
    return surfaces


# Indexing is ij, which means each ROW gives value at t[i]
t_mesh, x_mesh = np.meshgrid(time, space, indexing='ij')

fig3d, ax3d = plt.subplots(subplot_kw={"projection": "3d"})
ax3d.set_xlabel('time')
ax3d.set_xlim3d([time.min(), time.max()])

ax3d.set_ylabel('space')
ax3d.set_ylim3d([space.min(), space.max()])

ax3d.set_zlabel('sol')
ax3d.set_zlim3d([sol.min(), sol.max()])

ax3d.view_init(elev=-145, azim=-145)

N = len(time)

surf = []

update_anim = functools.partial(update3d, ax=ax3d, surfaces=surf, 
                                xdata=t_mesh, ydata=x_mesh, zdata=sol, anim=True)
# I am _partial_ to this method of specifying arguments for the update function
# over specifying the fargs argument in animation.FuncAnimation because it allows
# us to also specify keyword arguments

ani3d = animation.FuncAnimation(fig3d, update_anim, N, interval=25, blit=False)
#ani.save('test.gif')

plt.show()