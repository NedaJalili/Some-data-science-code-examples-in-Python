import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1)
y1=np.sqrt(1-x**2)
y2=-np.sqrt(1-x**2)
plt.plot(x,y1,color="red")
plt.plot(x,y2,color="red")
plt.show()
