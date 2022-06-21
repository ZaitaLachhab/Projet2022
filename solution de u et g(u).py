import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10)
u=0.1*np.exp(t)
u1=np.exp(t)/(np.exp(t)+9)
u2=np.sqrt(np.exp(2*t)/(99+np.exp(2*t)))

plt.plot(t, u,'b-.', label="g(u)=u")
plt.plot(t, u1, 'r-', label="g(u)=u(1-u)")
plt.plot(t, u2, 'g--', label="g(u)=u(1-u$^2$)")
plt.ylim([0, 1.5])
plt.legend( loc = 'upper right')