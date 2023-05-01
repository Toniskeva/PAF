import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,m,k,v0,x0):
        self.m=m
        self.k=k
        self.v=v0
        self.x=x0
        self.a=-self.x*self.k/self.m
        self.pocetni=(m,k,v0,x0)
    def reset(self):
        self.m,self.k,self.v,self.x=self.pocetni
    def __move(self,dt):
        self.v=self.v+self.a*dt
        self.x=self.x+self.v*dt
        self.a=-self.x*self.k/self.m
    def plot_trajectory(self,a,b,dt):
        a_lista=[]
        v_lista=[]
        x_lista=[]
        t_lista=[]
        while a<=b:
            x_lista.append(self.x)
            v_lista.append(self.v)
            a_lista.append(self.a)
            t_lista.append(a)
            self.__move(dt)
            a+=dt
        self.reset()
        fig,ax=plt.subplots(3,1)
        ax[0].plot(t_lista,x_lista)
        ax[0].set(xlabel='t[s]',ylabel='x[m]',title='x-t graf')
        ax[1].plot(t_lista,v_lista)
        ax[1].set(xlabel='t[s]',ylabel='v[m/s]',title='v-t graf')
        ax[2].plot(t_lista,a_lista)
        ax[2].set(xlabel='t[s]',ylabel='a[m/s^2]',title='a-t graf')
        plt.show()
    def period(self,dt):
        loop=True
        brojac=0
        polozaj=[self.x]
        T=[]
        I=[]
        vrijeme=[0]
        t=0
        i=0
        indeks=[0]
        while loop:
            self.__move(dt)
            t+=dt
            i+=1
            vrijeme.append(t)
            polozaj.append(self.x)
            indeks.append(i)
            if polozaj[i-1]<0 and polozaj[i]>0:
                brojac+=1
                I.append(i)
                T.append(t)
            elif polozaj[i-1]>0 and polozaj[i]<0:
                brojac+=1
                I.append(i)
                T.append(t)
            if brojac==2:
                #print(T[0],T[1])
                s=2*(T[1]-T[0])
                #print(I[1]-I[0])
                z=I[1]-I[0]
                #print(2*(T[1]-T[0]))
                break
        #print(vrijeme[:2*z+1]) - Da se obuhvati početni i krajnji trenutak promjene predznaka, 2*z+1
        self.reset()
        return vrijeme[:2*z+1],polozaj[:2*z+1],s
    def graf_period(self,dt):
        plt.plot(self.period(dt)[0],self.period(dt)[1], label='dt={}, T={}'.format(dt,self.period(dt)[2]))
        self.reset()