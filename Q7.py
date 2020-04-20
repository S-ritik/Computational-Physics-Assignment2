# Q7- Solving 4 ivp problems

import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt


def f1(t,y):
    return (t*np.exp(3*t)-2*y)
def f2(t,y):
    return (1-(t-y)**2)
def f3(t,y):
    return (1+y/t)
def f4(t,y):
    return (np.cos(2*t)+np.sin(3*t))    

f1sol=si.solve_ivp(f1,(0,1),[0],t_eval=np.linspace(0,1,100))
f2sol=si.solve_ivp(f2,(2,3),[1],t_eval=np.linspace(2,3,100))
f3sol=si.solve_ivp(f3,(1,2),[2],t_eval=np.linspace(1,2,100))
f4sol=si.solve_ivp(f4,(0,1),[1],t_eval=np.linspace(0,1,100))

f1=np.array(f1sol.t*np.exp(3*f1sol.t)/5-np.exp(3*f1sol.t)/25+np.array(-2*f1sol.t)/25)
f3=np.array(f3sol.t*np.log(f3sol.t)+2*f3sol.t)
f4=np.array(np.sin(2*f4sol.t)/2-np.cos(3*f4sol.t)/3+4/3)
f2=np.array(f2sol.t+1/(f2sol.t-3))

plt.xlabel("x")
plt.ylabel("y")
plt.plot(f1sol.t,f1sol.y[0],'b',label="Numerical solution")
plt.plot(f1sol.t,f1,'r',label="Analytical solution")
plt.legend()
plt.show()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(f2sol.t,f2sol.y[0],'b',label="Numerical solution")
plt.plot(f2sol.t,f2,'r',label="Analytical solution")
plt.legend()
plt.show()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(f3sol.t,f3sol.y[0],'b',label="Numerical solution")
plt.plot(f3sol.t,f3,'r',label="Analytical solution")
plt.legend()
plt.show()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(f4sol.t,f4sol.y[0],'b',label="Numerical solution")
plt.plot(f4sol.t,f4,'r',label="Analytical solution")
plt.legend()
plt.show()
