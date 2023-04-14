import particle as particle
import numpy as np
import matplotlib.pyplot as plt
import math

cestica=particle.Particle(10,60,0,0)
g=9.81
Domet_a=2*cestica.v*np.cos(cestica.k)*math.sqrt((cestica.v*np.sin(cestica.k))**2/(g**2))
Domet_n=cestica.range(0.01)
print('Analitički domet iznosi: {}.'.format(Domet_a))
print('Numerički domet iznosi: {}.'.format(Domet_n))
print('Pogeška iznosi: {}, {}%.'.format(Domet_a-Domet_n,-(Domet_a-Domet_n)/Domet_a*100))