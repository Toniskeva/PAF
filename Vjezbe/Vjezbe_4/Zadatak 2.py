import numpy as np
import matplotlib.pyplot as plt
import math
import particle as particle

p1=particle.Particle(10,60,0,0)
g=9.81
D=2*p1.v*np.cos(p1.k)*math.sqrt((p1.v*np.sin(p1.k))**2/g**2)
print(D)
lista_greska=[]
for dt in np.linspace(0.01,0.1,1000):
    n=D-p1.range(dt)/D*100
    if n>0:
        lista_greska.append(n)
    if n<0:
        lista_greska.append(-n)
plt.plot(np.linspace(0.01,0.1,1000),lista_greska)
plt.xlabel('dt[s]')
plt.ylabel('Pogreška[%]')
plt.show()