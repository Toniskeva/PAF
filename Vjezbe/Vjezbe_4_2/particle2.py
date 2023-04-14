import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,kut,koordinate):
        self.v0=v0
        self.kut=(kut/180)*np.pi
        self.x0,self.y0=koordinate
    def reset(self):
        self.v0=0
        self.kut=0
        self.koordinate=(0,0)
    def __move(self,dt):
        g=10
        x=self.x0+self.v0*np.cos(self.kut)*dt
        y=self.y0+self.v0*np.sin(self.kut)*dt-g*dt**2
        self.y0=y
        return y
    def range(self):
        t=0
        y=self.y0
        while y>=0:
            y=self.__move(0.5)
            print(y)
p1=Particle(10,45,(10,10))
p1.range()