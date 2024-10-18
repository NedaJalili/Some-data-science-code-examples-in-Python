import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes(projection="3d")
x=np.arange(-3,3,0.25)
y=np.arange(-2,2,0.25)
X,Y=np.meshgrid(x,y)
z1=np.exp(-X**2-Y**2)
z2=np.exp((-(X-1)**2)-((Y-1)**2))
Z=(z1-z2)**2
ax.plot_surface(X,Y,Z)
plt.show()
