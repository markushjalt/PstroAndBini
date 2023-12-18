from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def func(y, t, a, b, c, d):
    V, K = y
    dydt = [a*V- b*V*K, c*V*K - d*K]
    return dydt

t = np.linspace(0, 20, 200)
y0 = [2, 1]

a = 1
b = 1
c = 1
d = 1

sol = odeint(func, y0, t, args=(a, b, c, d))

plt.figure(1)
plt.plot(t, sol[:, 0], 'b', label = 'Växtätare')
plt.plot(t, sol[:, 1], 'r', label = 'Köttätare')
plt.ylabel('Populationsstorlek')
plt.xlabel('Tid (år)')

plt.figure(2)
plt.plot(sol[:,0], sol[:,1])




def func2(y, t, a, b, c, d, e, f, h, g):
    N, V, K = y
    dydt = [a*N - b*N*V-h*N, c*N*V- d*V*K-g*V, e*V*K - f*K]
    return dydt

t = np.linspace(0, 20, 200)
y0_2 = [4, 2, 1]

a = 1
b = 2
c = 1
d = 2
e = 1.5
f = 1
g = 0.25
h = 0.25

sol2 = odeint(func2, y0_2, t, args=(a, b, c, d, e, f, g, h))

fig, ax = plt.subplots(subplot_kw=dict(projection ='3d'))
ax.plot(sol2[:,0], sol2[:,1], sol2[:,2])
plt.show()