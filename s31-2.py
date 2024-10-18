import matplotlib.pyplot as plt
import numpy as np
labs=np.array(["فيزيک","شيمي","رياضي","ادبيات","زبان","انديشه","ورزش"])
zahra=np.array([19,17,15,18,18.5,17,18])
reza=np.array([13,19,15,17,14,14,19])
plt.bar(labs,zahra,label="zahra")
plt.bar(labs,reza,bottom=zahra,label="reza")
plt.legend()
plt.show()
