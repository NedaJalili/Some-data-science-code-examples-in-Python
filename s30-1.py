import numpy as np
import matplotlib.pyplot as plt
teta=np.linspace(np.pi/2,3*np.pi/2,100)
y=1-np.cos(teta)**2
plt.plot(teta,y)
plt.xlabel("teta")
plt.ylabel("y")
plt.show()
