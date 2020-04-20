# Q6- Solving ode of 5th ques by using relaxlation method

import numpy as np
import matplotlib.pyplot as plt

xsol=np.empty(100)
for i in range(10001):
    xsol[1:-1]=0.5*(xsol[2:]+xsol[:-2])+0.05
    t=np.linspace(0,10,len(xsol))
    if i==10000:
        plt.plot(t,xsol,'r',label="Solution")
    else:
        pass
    if i==5000 or i==7000 or i==8000 or i==6000:
        plt.plot(t,xsol,'b')
    else:
        pass        

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()    
    
        
