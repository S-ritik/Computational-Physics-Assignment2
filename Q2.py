#Q2- Solving the given differential equation using Euler method

import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return y/t-(y/t)**2

j=1  # defining for use to store value of t on mesh point
ytemp=1 #defining a temporary variable
wtemp=1 #defining a temporary variable
Y=[1]
T=[1]
for i in range(10):
    w=wtemp+0.1*f(j,wtemp)
    j=j+0.1
    wtemp=w
    ytemp=w
    T.append(j)
    Y.append(ytemp)
    
b=j

t=np.array(T)
y=np.array(Y)
plt.plot(t,y,'r',label="Solution using Euler method")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
def ysol(t):
    return t/(1+np.log(t))
Ysol=[]
for i in range(11):
    gtemp=ysol(T[i])
    Ysol.append(gtemp)
plt.show()

print("Absolute error at each step are = ",np.array(T)-np.array(Ysol))
print("\nRelative error at each step are = ",(np.array(T)-np.array(Ysol))/np.array(Ysol))

    
    
