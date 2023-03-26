import numpy as np
import math

def funkcija(a):
    print('A) koristeći formule za aritmetičku sredinu i devijaciju: ')
    srednja=sum(a)/len(a)
    print(srednja)
    s=0
    for i in a:
        s=s+(i-srednja)**2
    dev=math.sqrt(s/(len(a)*(len(a)-1)))
    print(dev)
    print('B) koristeći gotove module: ')
    print(np.mean(a))
    print(np.std(a))
funkcija([1,2,3,4,5,6,7,8,9,10])
