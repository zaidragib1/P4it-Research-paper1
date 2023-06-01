import numpy as np
from pylab import*

N=1000
k=3.5
m=0.2
y=np.zeros([N,2])

def derivspring(y, t):
    f0 = y[1]
    f1 = -(k/m) *y[0] - 9.8
    f = np.array([f0, f1])
    return f

def euler(y, t, dt, derivspring):
    y_next = y + dt * derivspring(y, t)
    return y_next

d=np.zeros([N,2])
d[0, 0] = 0
d[0,1] = 0
y[0,0]=0
y[0,1]=0
tau=20
dt=tau/float(N-1)

time=np.linspace(0,tau,N)

figure()
for j in range (N-1):
        y[j+1,:]=euler(y[j,:],time[j],dt,derivspring)
        d[j, :]=derivspring(y[j+1,:],time[j+1])
        y[j+1,:]=y[j,:]+d[j, :]*dt
        
xdata=[y[j,0] for j in range(N)]
ydata=[y[j,1] for j in range(N)]
plot (time,xdata,'-r')
plot (time,ydata,'-b')
legend['position','velocity']

show()


        
        
