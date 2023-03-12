import matplotlib.pyplot as plt
import numpy as np

F=float(input('Uneite iznos sile: '))
m=float(input('Uneite iznos mase: '))
a=F/m
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_ylabel('a')
axes.set_xlabel('t')
t=np.arange(0,10,0.1)
akc=[]
for i in range(len(t)):
    akc.append(a)
axes.plot(t,akc)
plt.show()