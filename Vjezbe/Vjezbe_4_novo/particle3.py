import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,kut,koordinate,g=9.81):
        self.v=v0
        self.kut=(kut/180)*np.pi
        self.x,self.y=koordinate
        self.pocetni=(v0,kut,koordinate)
        self.g=g
    def reset(self):
        self.v,self.kut,self.koordinate=self.pocetni
    def __move(self,dt):
        vy=self.v*np.sin(self.kut)-self.g*dt
        vx=self.v*np.cos(self.kut)
        self.v=np.sqrt(vx**2+vy**2)
        self.k=np.arctan(vy/vx)/np.pi*180.
        self.x=self.x+self.v*np.cos(self.kut)
        self.y=self.y+self.v*np.sin(self.kut)
    def range(self,dt):
        x0=self.x
        while self.y>0:
            self.__move(dt)
            print(self.x,self.y)
        domet=self.x-x0
        return domet
p2=Particle(2,30,(1,1))
print(p2.range(10))