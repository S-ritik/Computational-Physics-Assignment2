# Q3- Solving using Runge-Kuttta Method

import numpy as np
import matplotlib.pyplot as plt    

def f(x,y,u):
    return 2*u-y+x*np.exp(x)-x

wtemp=0
ytemp=0
xtemp=0
Y=[ytemp] #Array of solution at mesh point
X=[xtemp] #Array of mesh point
for i in range(100):
    m1=wtemp
    k1=f(xtemp,ytemp,wtemp)
    m2=wtemp+k1*0.01/2
    k2=f(xtemp+0.01/2,ytemp+0.01*m1/2,m2)
    m3=wtemp+k2*0.01/2
    k3=f(xtemp+0.01/2,ytemp+m2*0.01/2,m3)
    m4=wtemp+k3*0.01
    k4=f(xtemp+0.01,ytemp+m3*0.01,m4)
    y=ytemp+(m1+2*(m2+m3)+m4)*0.01/6
    w=wtemp+(k1+2*(k2+k3)+k4)*0.01/6
    wtemp=w
    ytemp=y
    xtemp=xtemp+0.01
    Y.append(y)
    X.append(xtemp)

x=np.array(X)
y=np.array(Y)
plt.plot(x,y,label="Solution of ode")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()    
