import matplotlib.pyplot as plt
import numpy as np

F=float(input('Inesite silu u N: '))
m=float(input('Unesite masu tijela u kg: '))
a=F/m
v=0
dt=0.001
t=0
s=0
lista_t=[]
lista_s=[]
lista_v=[]
lista_a=[]
while t<=9.999:
    v=v+a*dt
    lista_v.append(v)
    t=t+dt
    lista_t.append(t)
    s=s+v*dt
    lista_s.append(s)
    a=a
    lista_a.append(a)
#lista_t=np.arange(0,10.01,0.01)
#print(len(lista_s),len(lista_t))
#print(lista_s,lista_t)
listat=np.asarray(lista_t)
listas=np.asarray(lista_s)
listav=np.asarray(lista_v)
listaa=np.asarray(lista_a)
#plt.plot(listat,listas)
#plt.plot(listat,listav)
#plt.show()
#print(lista_t[-1])
fig, axes = plt.subplots(1,3)
axes[0].set_title('s-t graf')
axes[0].set_xlabel('t(s)')
axes[0].set_ylabel('s(m)')
axes[0].plot(listat,listas)
axes[1].set_title('v-t graf')
axes[1].set_xlabel('t(s)')
axes[1].set_ylabel('v(m/s)')
axes[1].plot(listat,listav)
axes[2].set_title('a-t graf')
axes[2].set_xlabel('t(s)')
axes[2].set_ylabel('a(m/s^2)')
axes[2].plot(listat,listaa)
plt.show()