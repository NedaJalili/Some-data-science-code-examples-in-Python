import matplotlib.pyplot as plt
import numpy as np

time=np.array([10,12.5,13,15,17,17.5,19])
score=np.array([7,17,15,12,18,19,20])

plt.xlabel("time",color="r")
plt.ylabel("score",color="r")
plt.title("time-score plot",color="r")

plt.plot(time,score,"or")
plt.show()
