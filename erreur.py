import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,10)

err=[1e-05,1,1000,10000,95000,95000,95000,95000,95000,95000]

plt.plot(t,err, "r")
plt.yscale('log')

plt.grid(False,which="both")