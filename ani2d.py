import numpy as np
import functools
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

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


'''
def update(frame, ax, surfaces, xdata, ydata, zdata, anim=False):
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

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_xlabel('time')
ax.set_xlim3d([time.min(), time.max()])

ax.set_ylabel('space')
ax.set_ylim3d([space.min(), space.max()])

ax.set_zlabel('sol')
ax.set_zlim3d([sol.min(), sol.max()])

ax.view_init(elev=-145, azim=-145)

N = len(time)

surf = []

update_anim = functools.partial(update, ax=ax, surfaces=surf, 
                                xdata=t_mesh, ydata=x_mesh, zdata=sol, anim=True)
# I am _partial_ to this method of specifying arguments for the update function
# over specifying the fargs argument in animation.FuncAnimation because it allows
# us to also specify keyword arguments

ani = animation.FuncAnimation(fig, update_anim, N, interval=25, blit=False)
#ani.save('test.gif')

'''
N = len(time)

fig, ax = plt.subplots()
ax.set_xlabel("space")
ax.set_xlim([space.min(), space.max()])

ax.set_ylabel("sol")
ax.set_ylim([sol.min(), sol.max()])

def update2d(frame, ax, line, xdata, ydata, tdata, anim=False):
    if line is None:
        line, = ax.plot(xdata, ydata[frame, :])
    line.set_data(xdata, ydata[frame, :])
    ax.set_title(f"time={tdata[frame]:.3f}")
    return line,

line, = update2d(0, ax, None, space, sol, time, True)



ani = animation.FuncAnimation(fig, func=update2d, frames=N, interval=25, fargs=[ax, line, space, sol, time])
#ani.save('test2.gif')

plt.show()