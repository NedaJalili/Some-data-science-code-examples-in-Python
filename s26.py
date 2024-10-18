import numpy as np
x=[[2,3],[5,4],[7,6]]
x=np.array(x)
y=[[10,15],[14,20],[21,18]]
y=np.array(y)
z0=np.stack((x,y),axis=0)
z1=np.stack((x,y),axis=1)
print("x = ",x,"y = ",y)
print("-------------------------------------------------")
print("z0 = ",z0)
print("-------------------------------------------------")
print("z1 = ",z1)
