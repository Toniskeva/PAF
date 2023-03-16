import matplotlib.pyplot as plt
import numpy as np

def funkcija(t1,t2):
    x1,y1=t1
    x2,y2=t2
    if not t1==t2:
        k=(y2 - y1)/(x2 - x1)
        n=-k*x1+y1
        if n<0:
            y= str(k)+'x'+str(n)
            print(y)
        if n>0:
            y=str(k)+'x'+'+'+str(n)
            print(y)
        if n==0:
            y=str(k)+'x'
            print(y)
    a=float(input('Unesite minimalnu vrijednost na x osi: '))
    b=float(input('Uneite maksimalnu vrijednot na x osi: '))
    x=np.arange(a,b,1)
    y3=k*x+n
    fig=plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.plot(x1,y1,'b.')
    axes.plot(x2,y2,'b.')
    axes.plot(x,y3)
    z=int(input('Za ispis grafa na ekranu uneisite 0, za spremanje grafa u obliku PDF-a uneite 1: '))
    if z==0:
        plt.show()
    elif z==1:
        ime=input('Uneiste ime slike: ')
        i=ime+'.png'
        fig.savefig(i)
    if t1==t2:
        print('Unijeli ste koordinate istih točaka, unesite ponovno.')
funkcija((0,5),(2,10))