# Q9 - Solving using adaptive step-size control with the fourth-order Runge-Kutta method

import numpy as np
import matplotlib.pyplot as plt 

def f(x,y):
    return (y**2+y)/x

xtemp=1
x1=1
ytemp=-2
y1=-2
Y=[-2]
X=[1]
h=0.1
h1=0.9
h0=0.09

for i in range(50):
    while x1<3:
        if h<h0:
            h=h0
        elif h>h1:
            h=h1
        else:
            pass
        for i in range(1):
            
            k1=f(xtemp,ytemp)    
            k2=f(xtemp+h/2,ytemp+h*k1/2)
            k3=f(xtemp+h/2,ytemp+k2*h/2)
            k4=f(xtemp+h,ytemp+k3*h)
            y_s=ytemp+(k1+2*(k2+k3)+k4)*h/6
            xtemp=xtemp+h
            ytemp=y_s
        
        k11=f(x1,y1)    
        k21=f(x1+h,y1+h*k11)
        k31=f(x1+h,y1+k21*h)
        k41=f(x1+2*h,y1+k31*h*2)
        y_d=y1+(k11+2*(k21+k31)+k41)*h/6
        x1=x1+h
        y1=y_d
        X.append(xtemp)
        Y.append(y_s)
        tol=abs(y_s-y_d)
        if tol>1e-4:
            h=h/2
        if tol<0.5e-4:
            h=2*h
        else:
            pass
x=np.array(X)
y=np.array(Y)
plt.plot(x,y,'r',label="Numerical Solution")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()    
