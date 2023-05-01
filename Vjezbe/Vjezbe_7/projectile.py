import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,k,x0,y0,m,A):
        self.A=A
        self.m=m
        self.v=v0
        self.k=(k/180)*np.pi
        self.x=x0
        self.y=y0
        self.vx=self.v*np.cos(self.k)
        self.vy=self.v*np.sin(self.k)
        self.pocetni=(v0,k,x0,y0,v0*np.cos(self.k),v0*np.sin(self.k))
    def reset(self):
        self.v,self.k,self.x,self.y,self.vx,self.vy=self.pocetni
    def __move(self,dt,P,C):
        if self.vy>0:
            ay=-9.81-(P*C*self.A*(self.vy)**2/(2*self.m))
        if self.vy<0:
            ay=-9.81+(P*C*self.A*(self.vy)**2/(2*self.m))
        ax=-P*C*self.A*(self.vx)**2/(2*self.m)
        self.vx=self.vx+ax*dt
        self.vy=self.vy+ay*dt
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
    def plot_trajectory(self,dt,P,C):
        x_lista=[self.x]
        y_lista=[self.y]
        while self.y>=0:
            self.__move(dt,P,C)
            x_lista.append(self.x)
            y_lista.append(self.y)
        plt.plot(x_lista,y_lista, label='dt={}'.format(dt))
        self.reset()
    def __runge_kutta(self,dt,P,C):
        if self.vx>0:
            k1vx=-P*C*self.A/(2*self.m)*(self.vx)**2*dt
        elif self.vx<0:
            k1vx=P*C*self.A/(2*self.m)*(self.vx)**2*dt
        k1x=self.vx*dt
        if (self.vx+k1vx/2)>0:
            k2vx=-P*C*self.A/(2*self.m)*(self.vx+k1vx/2)**2*dt
        elif (self.vx+k1vx/2)<0:
            k2vx=P*C*self.A/(2*self.m)*(self.vx+k1vx/2)**2*dt
        k2x=(self.vx+k1vx/2)*dt
        if (self.vx+k2vx/2)>0:
            k3vx=-P*C*self.A/(2*self.m)*(self.vx+k2vx/2)**2*dt
        elif (self.vx+k2vx/2)<0:
            k3vx=P*C*self.A/(2*self.m)*(self.vx+k2vx/2)**2*dt
        k3x=(self.vx+k2vx/2)*dt
        if (self.vx+k3vx/2)>0:
            k4vx=-P*C*self.A/(2*self.m)*(self.vx+k3vx/2)**2*dt
        elif (self.vx+k3vx/2)<0:
            k4vx=P*C*self.A/(2*self.m)*(self.vx+k3vx/2)**2*dt
        k4x=(self.vx+k3vx/2)*dt
        self.vx=self.vx+(k1vx+2*k2vx+2*k3vx+k4vx)/6
        self.x=self.x+(k1x+2*k2x+2*k3x+k4x)/6

        if self.vy>0:
            k1vy=(-9.81-P*C*self.A/(2*self.m)*(self.vy)**2)*dt
        elif self.vy<0:
            k1vy=(-9.81+P*C*self.A/(2*self.m)*(self.vy)**2)*dt
        k1y=self.vy*dt
        if (self.vy+k1vy/2)>0:
            k2vy=(-9.81-P*C*self.A/(2*self.m)*(self.vy+k1vy/2)**2)*dt
        elif (self.vy+k1vy/2)<0:
            k2vy=(-9.81+P*C*self.A/(2*self.m)*(self.vy+k1vy/2)**2)*dt
        k2y=(self.vy+k1vy/2)*dt
        if (self.vy+k2vy/2)>0:
            k3vy=(-9.81-P*C*self.A/(2*self.m)*(self.vy+k2vy/2)**2)*dt
        elif (self.vy+k2vy/2)<0:
            k3vy=(-9.81+P*C*self.A/(2*self.m)*(self.vy+k2vy/2)**2)*dt
        k3y=(self.vy+k2vy/2)*dt
        if (self.vy+k3vy/2)>0:
            k4vy=(-9.81-P*C*self.A/(2*self.m)*(self.vy+k3vy/2)**2)*dt
        elif (self.vy+k3vy/2)<0:
            k4vy=(-9.81+P*C*self.A/(2*self.m)*(self.vy+k3vy/2)**2)*dt
        k4y=(self.vy+k3vy/2)*dt
        self.vy=self.vy+(k1vy+2*k2vy+2*k3vy+k4vy)/6
        self.y=self.y+(k1y+2*k2y+2*k3y+k4y)/6
    def runge_kutta_plot_trajectory(self,dt,P,C):
        lista_x=[self.x]
        lista_y=[self.y]
        while self.y>=0:
            self.__runge_kutta(dt,P,C)
            lista_x.append(self.x)
            lista_y.append(self.y)
        plt.plot(lista_x,lista_y,'r',label='Runge-Kutta metoda, dt={}'.format(dt))
        self.reset()