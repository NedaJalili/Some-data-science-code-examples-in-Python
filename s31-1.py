import matplotlib.pyplot as plt
import numpy as np
labs=np.array(["فيزيک","شيمي","رياضي","ادبيات","زبان","انديشه","ورزش"])
zahra=np.array([19,17,15,18,18.5,17,18])
reza=np.array([13,19,15,17,14,14,19])
x=np.arange(len(labs))

w=0.2
fig,ax=plt.subplots()
ax.bar(x-w/2,zahra,width=w,label="zahra")
ax.bar(x+w/2,reza,width=w,label="reza")
ax.set_xticks(x)
ax.set_xticklabels(labs)
plt.legend()
plt.show()
