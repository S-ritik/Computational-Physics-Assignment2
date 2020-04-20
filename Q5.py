# Q5- Solving by using Shooting Method

import numpy as np
import matplotlib.pyplot as plt

def f(t,x,u):
    return -10

for utemp in np.linspace(46.05,55.05,10):
    
    xtemp=0
    T=0
    X=[0]
    for i in range(1001):
        m1=utemp
        k1=f(T,xtemp,utemp)
        m2=utemp+k1*0.01/2
        k2=f(T+0.01/2,xtemp+0.01*m1/2,m2)
        m3=utemp+k2*0.01/2
        k3=f(T+0.01/2,xtemp+m2*0.01/2,m3)
        m4=utemp+k3*0.01
        k4=f(T+0.01,xtemp+m3*0.01,m4)
        x=xtemp+(m1+2*(m2+m3)+m4)*0.01/6
        u=utemp+(k1+2*(k2+k3)+k4)*0.01/6
        utemp=u
        xtemp=x
        T=T+0.01
        X.append(x)
    
    t=np.linspace(0,T,len(X))
    x=np.array(X)

    if X[1001]==-4.485412041788095e-12:
         plt.plot(t,x,'r',label="Solution of ode")  # For desired solution (Winner candidate)
  
    else:
        
         plt.plot(t,x,'b') # For waste solutions

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()    
