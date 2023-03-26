import numpy as np
import matplotlib.pyplot as plt
import math

M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
Kut=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
lista=[]
for i in range(len(M)):
    s=M[i]*Kut[i]
    lista.append(s)
xy=sum(lista)/len(lista)
lista2=[]
for j in range(len(Kut)):
    S=(Kut[j])**2
    lista2.append(S)
sr=sum(lista2)/len(lista2)
k=xy/sr
lista_m=[]
for z in range(len(M)):
    lista_m.append(M[z]**2)
srednja_m=sum(lista_m)/len(lista_m)
sigma=math.sqrt((1/len(M))*((srednja_m/sr)-k**2))
polje1=np.asarray(M)
polje2=np.asarray(Kut)
y=k*polje2
print('Modul torzije Dt iznosi:{}{}{}'.format(k, u"\u00B1",sigma))
plt.xlabel('φ [rad]')
plt.ylabel('M [Nm]')
plt.plot(polje2,polje1,'r.', label='Zadane točke')
plt.plot(polje2,y, label='Pravac regresije')
plt.title('Pravac regresije')
plt.legend()
plt.show()