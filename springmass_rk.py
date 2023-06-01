from numpy import *
from matplotlib.pyplot import *
def dervis(state,time):
    go=state[1]
    g1=-9.81
    g=array([go,g1])
    return g

def euler(y,t,dt,dervis):
    yn=y+dervis(y,t)*dt
    ynew=y+dervis(yn,t)*dt
    return ynew

def rk2(y,t,dt,dervis):
    k0=dt*dervis(y,t)
    k1=dt*dervis(y+k0,t+dt)
    y_next=y+ 0.5*(k0+k1)
    return y_next

def dervisspring(state,time):
    k=-3.5
    m=0.2
    g=9.81
    g0=state[1]
    g1=state[0]*(k/m)-g
    gi=array([g0,g1])
    return gi

N=5000
y=zeros([N,2])
y1=zeros([N,2])
y[0,0]=0
y[0,1]=-0

y1[0,0]=0
y1[0,1]=-0
time=20
dt=time/float(N-1)
totalt=linspace(0,time,N)

i=0
for i in range(N-1):
    y[i+1,:]=rk2(y[i,:],totalt[i],dt,dervisspring)
    y1[i+1,:]=euler(y1[i,:],totalt[i],dt,dervisspring)
    # d[:]=dervisspring(y[i+1,:],time[i+1])
xdata=[y[i,0] for i in range(N)]
ydata=[y[i,1] for i in range(N)]
y1data=[y1[i,1] for i in range(N)]

plot(totalt,xdata,'r')
plot(totalt,ydata,'g')
plot(totalt,y1data,'b')

show()