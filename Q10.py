#  Q10-Solving using 4th order Runge-Kutta method

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return 1/(y**2+x**2)

h=1000
h1=1100
h0=900
x1=0
x2=0
y1=1
y2=1
Y=[1]
X=[0]
ytemp=1
xtemp=0
req=1

while x1<=3.5e6 or x2<=3.5e6:
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
        tol=np.abs(y_s-y_d)
        h_opt=h*((30*h*req)/tol)**0.25
        if h_opt>h:
            Y.append(y_d)
        else:
            h=h_opt
            k1=f(x2,y2)    
            k2=f(x2+h/2,y2+h*k1/2)
            k3=f(x2+h/2,y2+k2*h/2)
            k4=f(x2+h,y2+k3*h)
            y_s=ytemp+(k1+2*(k2+k3)+k4)*h/6
            x2=x2+h
            y2=y_s
            Y.append(y_d)
x=np.array(X)
y=np.array(Y)
plt.plot(x,y,'r',label="Numerical Solution")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()    
print("Value of the solution at t = 3.5 × 10^6",Y[len(Y)-1])
