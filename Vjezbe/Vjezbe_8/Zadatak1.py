import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self,v,m,q):
        self.v=v
        self.m=m
        self.q=q
        self.x=(0,0,0)
        self.pocetni=v,m
    def gibanje(self,E,B,dt):
        self.a=(self.q*(np.array(E)+np.cross(np.array(self.v),np.array(B))))/self.m
        self.v=self.v+self.a*dt
        self.x=self.x+self.v*dt
    def plot_trajectory(self,a,b,dt,E,B,cestica):
        lista_x=[]
        lista_y=[]
        lista_z=[]
        while a<b:
            self.gibanje(E,B,dt)
            lista_x.append(self.x[0])
            lista_y.append(self.x[1])
            lista_z.append(self.x[2])
            a+=dt
        fig=plt.figure()
        ax=fig.add_subplot(projection='3d')
        xline=lista_x
        yline=lista_y
        zline=lista_z
        ax.plot3D(xline,yline,zline,'blue',label='{}'.format(cestica))
        plt.legend()

p1=particle((1,1,1),1,1)
p2=particle((1,1,1),1,-1)
p1.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1),'Pozitron')
p2.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1),'Elektron')
plt.show()