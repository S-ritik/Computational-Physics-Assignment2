# Q13- to find the solution of second order ode using Euler method


import numpy as np
import matplotlib.pyplot as plt

def f(w,y,t):
    return 2*w/t-2*y/(t*t)+t*np.log(t)

w=np.empty(1001) # w is array containing value for y'. It is defined in such way so that w has same size that of t or size of mesh point
y=np.empty(1001) # y is array containing value for y. It is also defined in such a way for the same reason as that of w
t=np.empty(1001)
ysol=np.empty(1001)
w[0]=0    
y[0]=1
j=1
t[0]=1
ysol[0]=0

for i in range(1000,2000):
    w[j]=w[j-1]+0.001*f(w[j-1],y[j-1],i/1000)
    y[j]=y[j-1]+0.001*w[j-1]
    t[j]=i/1000
    ysol[j]=7*t[j]/4+(t[j]**3)*np.log(t[j])/2-3*t[j]**3/4
    j=j+1

print(t)
    
plt.plot(t,y,'ro',label="Euler solution")
plt.plot(t,ysol,label="Actual solution")
plt.xlabel("t")
plt.ylabel("y")
plt.axis([1, 2, 0, 1.2])
plt.legend()
plt.show()
