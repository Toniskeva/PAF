import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class particle:
    def __init__(self,v,m,q,x0):
        self.v=v
        self.m=m
        self.q=q
        self.x=x0
        self.pocetni=v,m,q,x0
    def reset(self):
        self.v,self.m,self.q,self.x=self.pocetni
    def __move(self,E,B,dt):
        self.a=(self.q*(np.array(E)+np.cross(np.array(self.v),np.array(B))))/self.m
        self.v=self.v+self.a*dt
        self.x=self.x+self.v*dt
    def plot_trajectory(self,a,b,dt,E,B):
        lista_x=[]
        lista_y=[]
        lista_z=[]
        while a<b:
            self.__move(E,B,dt)
            lista_x.append(self.x[0])
            lista_y.append(self.x[1])
            lista_z.append(self.x[2])
            a+=dt
        self.reset()
        return lista_x,lista_y,lista_z
    
p1=particle((1,1,1),1,1,(0,0,0))
p2=particle((1,1,1),1,-1,(0,0,0))
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot3D(p1.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[0],p1.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[1],p1.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[2],'blue',label='Pozitron')
ax.plot3D(p2.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[0],p2.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[1],p2.plot_trajectory(1,25,0.001,(0,0,0),(0,0,1))[2],'red',label='Elektron')
ax.set_xlabel('x[m]')
ax.set_ylabel('y[m]')
ax.set_zlabel('z[m]')
plt.legend()
plt.show()