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

    y1=k1*dt
    y2=k1*dt/2
    y3=k2*dt/4
    y4=k3*dt
    
    y_next=y+ (k1+(2*k2)+(2*k3)+k4)/6
    
    hi=[y1,y2,y3,y4,y_next]
    return hi



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
y[0,0]=0
y[0,1]=-0

y1=zeros([N,2])
y1[0,0]=0
y1[0,1]=-0

y2=zeros([N,2])
y2[0,0]=0
y2[0,1]=-0

y3=zeros([N,2])
y3[0,0]=0
y3[0,1]=-0

y4=zeros([N,2])
y4[0,0]=0
y4[0,1]=-0
time=50
dt=time/float(N-1)
totalt=linspace(0,time,N)

for i in range(N-1):
    y[i+1,:]=rk4(y[i,:],totalt[i],dt,deriv_pend)[0]
    y1[i+1,:]=rk4(y1[i,:],totalt[i],dt,deriv_pend)[1]
    y2[i+1,:]=rk4(y2[i,:],totalt[i],dt,deriv_pend)[2]
    y3[i+1,:]=rk4(y3[i,:],totalt[i],dt,deriv_pend)[3]
    y4[i+1,:]=rk4(y4[i,:],totalt[i],dt,deriv_pend)[4]

    # y1[i+1,:]=euler(y1[i,:],totalt[i],dt,dervisspring)
    # d[:]=dervisspring(y[i+1,:],time[i+1])
# xdata=[y[i,0] for i in range(N)]
ydata=[y[i,1] for i in range(N)]
ydata1=[y1[i,1] for i in range(N)]
ydata2=[y2[i,1] for i in range(N)]
ydata3=[y3[i,1] for i in range(N)]
ydata4=[y4[i,1] for i in range(N)]
# y1data=[y1[i,1] for i in range(N)]
figure()
# plot(totalt,xdata,'r')
plot(totalt,ydata,'g')
plot(totalt,ydata1,'r')
plot(totalt,ydata2,'b')
plot(totalt,ydata3,'yellow')
# plot(totalt,ydata4,'orange')

# plot(totalt,y1data,'b')

show()