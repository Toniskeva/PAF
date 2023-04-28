import numpy as np
import matplotlib.pyplot as plt

def derivacija2(f,x,h):
    return (f(x+h)-f(x))/h

def derivacija3(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def derivacija(f,a,b,k,e,metoda='3step'):
    lista=np.asarray(np.linspace(a,b,k))
    #print('Lista točaka je {}.'.format(lista))
    derivacije=[]
    if metoda=='3step':
        for i in lista:
            derivacije.append(derivacija3(f,i,e))
    else:
        for i in lista:
            derivacije.append(derivacija2(f,i,e))
    #print('Derivacije u točkama iznose {}.'.format(derivacije))
    return lista,derivacije

def integral(f,a,b,n):
    lista=np.linspace(a,b,n+1)
    delta_x=(b-a)/n
    donja=0
    gornja=0
    for i in range(n):
        donja+=delta_x*f(lista[i])
        gornja+=delta_x*f(lista[i+1])
    return donja,gornja

def integral_trapez(f,a,b,n):
    lista=np.linspace(a,b,n+1)
    delta_x=(b-a)/n
    integral=0
    for i in range(n):
        integral+=delta_x*(f(lista[i])+f(lista[i+1]))/2
    return integral