import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

class Gravitacija:
    def __init__(self,m,v,x):
        self.m=m
        self.v=v
        self.x=x
        self.pocetni=self.m,self.v,self.x
    def reset(self):
        self.m,self.v,self.x=self.pocetni
    def __move(self,M,v2,x2,dt,G=6.67408*10**(-11)):
        self.a=-G*M/((LA.norm(np.array(self.x)-np.array(x2)))**3)*(np.array(self.x)-np.array(x2))
        self.v+=self.a*dt
        self.x+=self.v*dt
        a2=-G*self.m/((LA.norm(np.array(x2)-np.array(self.x)))**3)*(np.array(x2)-np.array(self.x))
        v2+=a2*dt
        x2+=v2*dt
        return x2
    def plot_trajectory(self,dt,T,M,v2,x2,G=6.67408*10**(-11)):
        lista_x=[self.x[0]]
        lista_y=[self.x[1]]
        lista_xs=[]
        lista_ys=[]
        t=0
        while t<T:
            self.__move(M,v2,x2,dt,G=6.67408*10**(-11))
            lista_x.append(self.x[0])
            lista_y.append(self.x[1])
            lista_xs.append(self.__move(M,v2,x2,dt,G=6.67408*10**(-11))[0])
            lista_ys.append(self.__move(M,v2,x2,dt,G=6.67408*10**(-11))[1])
            t+=dt
        plt.scatter(0,0,c='yellow',label='Sun')
        plt.plot(lista_x,lista_y,'b',label='Earth')
        plt.plot(lista_xs,lista_ys,'r',label='Sun trajectory')
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.title('Sun-Earth system')
        plt.legend()
        plt.show()

zemlja=Gravitacija(5.9742*10**24,(0,29783),(1.486*10**11,0))
zemlja.plot_trajectory(3600*24,365.242*24*3600,1.989*10**30,(0,0),(0,0))