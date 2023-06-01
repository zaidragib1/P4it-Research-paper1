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

def rk4(y,t,dt,dervis):
    k1=dt*dervis(y,t)
    k2=dt*dervis(y+(k1/2),t+dt/2)
    k3=dt*dervis(y+(k2/2),t+dt/2)
    k4=dt*dervis(y+k3,t+dt)

    y_next=y+ (k1+(2*k2)+(2*k3)+k4)/6
    return y_next

def deriv_pend(state,time):
    l=1
    g=9.81
    b=0.2
    B=0.01231
    y0=state[1]
    y1=-(g/l)*sin(state[0])-(b*state[1])+(B*cos(state[1]*time))
    dydt=array([y0,y1])
    return dydt

N=5000
y=zeros([N,2])
y1=zeros([N,2])
y[0,0]=0
y[0,1]=-0
time=50
dt=time/float(N-1)
totalt=linspace(0,time,N)

for i in range(N-1):
    y[i+1,:]=rk4(y[i,:],totalt[i],dt,deriv_pend)
    # y1[i+1,:]=euler(y1[i,:],totalt[i],dt,dervisspring)
    # d[:]=dervisspring(y[i+1,:],time[i+1])
# xdata=[y[i,0] for i in range(N)]
ydata=[y[i,1] for i in range(N)]
# y1data=[y1[i,1] for i in range(N)]

# plot(totalt,xdata,'r')
plot(totalt,ydata,'g')
# plot(totalt,y1data,'b')

show()