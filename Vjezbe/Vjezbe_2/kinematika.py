import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(F,m,t2):
    a=F/m
    v=0
    dt=0.001
    t=0
    s=0
    lista_t=[]
    lista_s=[]
    lista_v=[]
    lista_a=[]
    while t<=t2:
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

def kosi_hitac(v0,kut,t2):
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
    while t<=t2:
        t=t+dt
        lista_t.append(t)
        vy=vy-g*dt
        y=y+vy*dt
        lista_y.append(y)
        vx=vx
        x=x+vx*dt
        lista_x.append(x)
        if y<0:
            break
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