import numpy as np
a=np.array([[2,4,2],[2,1,2],[4,1,-2]])
b=np.array([15,-5,0])
x,y,z=np.linalg.solve(a,b)
print("x = ",x)
print("y = ",y)
print("z = ",z)
