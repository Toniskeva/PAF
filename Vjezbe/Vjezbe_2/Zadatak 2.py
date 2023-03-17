import matplotlib.pyplot as plt
import numpy as np

v0=float(input('Uneite početnu brzinu tijela u m/s: '))
kut=float(input('Uneite kut izbačaja u stupnjevima: '))
g=10
t=0
y=0
x=0
dt=0.001
vy=v0*np.sin((kut/180)*np.pi)
vx=v0*np.cos((kut/180)*np.pi)
lista_y=[]
lista_x=[]
lista_t=[]
while t<=9.99:
    t=t+dt
    lista_t.append(t)
    vy=vy-g*dt
    y=y+vy*dt
    lista_y.append(y)
    vx=vx
    x=x+vx*dt
    lista_x.append(x)
listat=np.asarray(lista_t)
listay=np.asarray(lista_y)
listax=np.asarray(lista_x)
fig, axes =plt.subplots(1,3)
axes[0].set_title('y-t graf')
axes[0].set_ylabel('y(m)')
axes[0].set_xlabel('t(s)')
axes[0].plot(listat,listay)
axes[1].set_title('x-t graf')
axes[1].set_ylabel('x(m)')
axes[1].set_xlabel('t(s)')
axes[1].plot(listat,listax)
axes[2].set_title('y-x graf')
axes[2].set_ylabel('y(m)')
axes[2].set_xlabel('x(m)')
axes[2].plot(listax,listay)
plt.show()