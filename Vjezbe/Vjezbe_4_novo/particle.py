import numpy as np
import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self,v0,k,x0,y0):
        self.v=v0
        self.k=(k/180)*np.pi
        self.x=x0
        self.y=y0
        self.vx=v0*np.cos(self.k)
        self.vy=v0*np.sin(self.k)
        self.pocetni=(v0,k,x0,y0,v0*np.cos(self.k),v0*np.sin(self.k))
    def reset(self):
        self.v,self.k,self.x,self.y,self.vx,self.vy=self.pocetni
    def __move(self,dt):
        g=9.81
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
        self.vx=self.vx
        self.vy=self.vy-g*dt
    def range(self,dt):
        x0=self.x
        while self.y>=0:
            self.__move(dt)
        domet=self.x-x0
        self.reset()
        return domet
    def plot_trajectory(self,dt):
        x_lista=[self.x]
        y_lista=[self.y]
        while self.y>=0:
            self.__move(dt)
            x_lista.append(self.x)
            y_lista.append(self.y)
        plt.plot(x_lista,y_lista)
        plt.show()