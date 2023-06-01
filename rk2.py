import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def DErvis(y, t):
    f0 = y[1]
    f1 = -(k/m) *y[0] - 9.8
    f = np.array([f0, f1])
    return f

def Euler(y, t, dt, DErvis):
    y_next = y + dt * DErvis(y, t)
    return y_next

def Euler_Cramer(y, t, dt, Euler, DErvis):
    y_new = Euler(y, t, dt, DErvis) + dt * DErvis(Euler(y, t, dt, DErvis), t)
    return y_new

def rk2(y, t, dt, DErvis):
    k0 = dt * DErvis(y, t)
    k1 = dt * DErvis(y+k0, t+dt)
    return y + (k0 + k1)/2

def rk4(y, t, dt, DErvis):
    k1 = dt * DErvis(y, t)
    k2 = dt * DErvis(y+k1/2, t+dt/2)
    k3 = dt * DErvis(y+k2/2, t+dt/2)
    k4 = dt * DErvis(y+k3, t+dt)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6


k = 3.5
m = 0.2

N = 5000
y = np.zeros([N, 2])
y[0,0] = 0
y[0,1] = -0
tau = 20
dt = tau / float(N-1)
t = np.linspace(0, tau, N)
plt.figure()

for j in range(N-1):
    y[j+1, :] = Euler_Cramer(y[j, :], t[j], dt, Euler, DErvis)

xdata = [y[i, 0] for i in range(N)]
ydata = [y[h, 1] for h in range(N)]

plt.plot(t, xdata, '-r')
plt.plot(t, ydata, '-b')

plt.figure()
for i in range(N-1):
    y[i+1, :] = Euler(y[i, :], t[i], dt, DErvis)

xne = [y[k, 0] for k in range(N)]
yne = [y[m, 1] for m in range(N)]

plt.plot(t, xne, '-k')
plt.plot(t, yne, '-g')


plt.figure()

for ye in range(N-1):
    y[ye+1, :] =rk4(y[ye, :], t[ye], dt, DErvis)
y_1data = [y[m, 1] for m in range(N)]
x_1data = [y[n, 0] for n in range(N)]
plt.plot(x_1data, y_1data, '.-k')

plt.figure()

for it in range(N-1):
    y[it+1, :] = rk2(y[it, :], t[it], dt, DErvis)
xne1 = [y[g, 0] for g in range(N)]
yne1 = [y[h, 1] for h in range(N)]
plt.plot(xne1, yne1, '-b')


plt.show()