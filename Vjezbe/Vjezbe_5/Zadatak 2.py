import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def kubna(x):
    return x**3
f=kubna

def trigonometrijska(x):
    return np.cos(x)
h=trigonometrijska

def d_kubna(x):
    return 3*x**2
def d_trigonometrijska(x):
    return -1*np.sin(x)

xlista=np.linspace(-5,5,100)
f_lista=[]
h_lista=[]
for i in xlista:
    f_lista.append(d_kubna(i))
    h_lista.append(d_trigonometrijska(i))

plt.plot(xlista,f_lista,label='Analitičko rješenje')
for i in list(np.arange(0.1,10,1)):
    plt.plot(cal.derivacija(f,-5,5,100,i)[0],cal.derivacija(f,-5,5,100,i)[1], label='3step, e={}'.format(i))
plt.plot(cal.derivacija(f,-5,5,100,0.1,'2step')[0],cal.derivacija(f,-5,5,100,0.1,'2step')[1],'r-.',label='2step, e=0.1')
plt.xlabel('x')
plt.ylabel('d(x^3)/dx')
plt.title('Numeričko deriviranje')
plt.legend()
plt.show()

plt.plot(xlista,h_lista,label='Analitičko rješenje')
for i in list(np.arange(0.1,10,1)):
    plt.plot(cal.derivacija(h,-5,5,100,i)[0],cal.derivacija(h,-5,5,100,i)[1], label='3step, e={}'.format(i))
plt.plot(cal.derivacija(h,-5,5,100,0.1,'2step')[0],cal.derivacija(h,-5,5,100,0.1,'2step')[1],'r-.',label='2step, e=0.1')
plt.xlabel('x')
plt.ylabel('d(cos(x))/dx')
plt.title('Numeričko deriviranje')
plt.legend()
plt.show()

def pravac(x):
    return 2*x
g=pravac

broj_podjela=list(range(100,1001,50))
donja_meda=[]
gornja_meda=[]
trapezni_integral=[]

for i in broj_podjela:
    donja_meda.append(cal.integral(g,0,1,i)[0])
    gornja_meda.append(cal.integral(g,0,1,i)[1])
    trapezni_integral.append(cal.integral_trapez(g,0,1,i))

analiticko=[1]*len(broj_podjela)
plt.plot(broj_podjela,analiticko,label='Analitičko rješenje')
plt.plot(broj_podjela,donja_meda,'r.',label='Donja međa')
plt.plot(broj_podjela,gornja_meda,'b.',label='Gornja međa')
plt.plot(broj_podjela,trapezni_integral,'y.',label='Trapezna integracija')
plt.xlabel('Broj podjela')
plt.ylabel('Integral')
plt.title('Numeričko integriranje')
plt.legend()
plt.show()
