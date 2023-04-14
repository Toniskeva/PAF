import numpy as np
import matplotlib.pyplot as plt

class Particle():
    def __init__(self, v0, kut, koordinate):
        self.v0=v0
        self.kut=(kut/180)*np.pi
        self.koordinate=koordinate
        x,y=koordinate
        self.pocetna=v0
        self.pkut=kut
        self.pkoordinate=koordinate
    def reset(self):
        self.v0=self.pocetna
        self.kut=self.pocetna
        self.koordinate=self.pkoordinate   
    def __move(self,dt):
        self.dt=dt
        g=10
        x=self.v0*np.cos(self.kut)*dt
        y=self.v0*np.sin(self.kut)*dt-(g*dt**2)/2
        self.koordinate=(x,y)
        return y
    def range(self):
        x,y=self.koordinate
        g=10
        t=0
        while y>=0:
            y+=self.__move(0.01)
        #print('Domet iznosi {} metara.'.format(self.v0*np.cos(self.kut)*t))
        return self.v0*np.cos(self.kut)*t
    def plot_trajectory(self):
            x,y=self.koordinate
            x_koordinate=[]
            y_koordinate=[]
            g=10
            t=0
            dt=0.01
            while y>=0:
                y=self.v0*np.sin(self.kut)*t-(g*t**2)/2
                y_koordinate.append(y)
                t+=dt
                x_koordinate.append(self.v0*np.cos(self.kut)*t)
            x_polje=np.asarray(y_koordinate)
            y_polje=np.asarray(x_koordinate)
            plt.plot(y_polje,x_polje)
            plt.show()

p1=Particle(10,45,(1,2))
print(p1.v0)