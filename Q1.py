#Q1- Solving 2 ode using Euler method

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):  #For 1st ode
    return -9*y
def g(x,y):   #For 2nd ode
    return -20*(y-x)**2+2*x

#Solving 1st ode
ytemp=np.exp(1)
Y=[ytemp]   #Array containing values of solution of 1st ode at mesh point
xtemp=0
for i in range(100):
    wtemp=ytemp
    w=wtemp+0.01*f(xtemp,wtemp)
    xtemp=xtemp+0.01
    ytemp=w
    Y.append(ytemp)
    
b=xtemp

#Solving 2nd ode
xtemp=1/3
xtemp=0
Z=[1/3]  #Array containing values of solution of 2nd ode at mesh point
for i in range(100):
    wtemp=xtemp
    w=wtemp+0.01*g(xtemp,wtemp)
    xtemp=xtemp+0.01
    xtemp=w
    Z.append(xtemp)

#Plotting solution

x=np.linspace(0,b,len(Y))
y=np.array(Y)
z=np.array(Z)
plt.plot(x,y,'b',label="Solution of 1st ode")
plt.plot(x,z,'r',label="Solution of 2nd ode")
plt.legend()
plt.show()


