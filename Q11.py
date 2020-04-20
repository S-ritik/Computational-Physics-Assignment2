# Q11--Solving using 4th order Runge-Kutta method

import numpy as np
import matplotlib.pyplot as plt

def f1(t,u1,u2,u3):
    return u1+2*u2-2*u3+np.exp(-t)

def f2(t,u1,u2,u3):    
    return u2+u3-2*np.exp(-t)

def f3(t,u1,u2,u3):
    return u1+2*u2+np.exp(-t)

u1=3
u2=-1 
u3=1
U1=[3]
U2=[-1] 
U3=[1]
temp=0
T=[0]

for i in  range(1000):
    if temp<=1:
        k11=f1(temp,u1,u2,u3)
        k12=f2(temp,u1,u2,u3)
        k13=f3(temp,u1,u2,u3)
        k21=f1(temp+0.1/2,u1+0.1*k11/2,u2+0.1*k12/2,u3+0.1*k13/2)
        k22=f2(temp+0.1/2,u1+0.1*k11/2,u2+0.1*k12/2,u3+0.1*k13/2)
        k23=f3(temp+0.1/2,u1+0.1*k11/2,u2+0.1*k12/2,u3+0.1*k13/2)
        k31=f1(temp+0.1/2,u1+0.1*k21/2,u2+0.1*k22/2,u3+0.1*k23/2)
        k32=f2(temp+0.1/2,u1+0.1*k21/2,u2+0.1*k22/2,u3+0.1*k23/2)
        k33=f3(temp+0.1/2,u1+0.1*k21/2,u2+0.1*k22/2,u3+0.1*k23/2)
        k41=f1(temp+0.1,u1+0.1*k31,u2+0.1*k32,u3+0.1*k33)
        k42=f2(temp+0.1,u1+0.1*k31,u2+0.1*k32,u3+0.1*k33)
        k43=f3(temp+0.1,u1+0.1*k31,u2+0.1*k32,u3+0.1*k33)
        u11=u1+0.1*(k11+(k21+k31)*2+k41)/6
        u21=u2+0.1*(k12+(k22+k32)*2+k42)/6
        u31=u3+0.1*(k13+(k23+k33)*2+k43)/6
        u1=u11
        u2=u21
        u3=u31
        temp=temp+0.1
        U1.append(u11) ;U2.append(u21); U3.append(u31); T.append(temp)
    else:
        break

u1f=np.array(U1)
u2f=np.array(U2)
u3f=np.array(U3)
t=np.array(T)
plt.plot(t,u1f,'r',label='Numerical solution for u1')
plt.plot(t,u2f,'y',label='Numerical solution for u2')
plt.plot(t,u3f,'b','-',label='Numerical solution for u3')
plt.legend()
plt.xlabel('t')
plt.ylabel('U')
plt.show()
