import math
def fximenosuno(x):
    y=x**2-3*x-4
    return (y)
def fxi(x):
    y=x**2-3*x-4
    return (y)
def ximasuno(x,y):
    u=y-((fxi(y)*(x-y))/(fximenosuno(x)-fxi(y)))
    return (u)
#Programa principal
print ("Este programa encuentra una raíz, por el método de la secante")
ximenos1=float((input('Introduce xi-1')))
xi=float((input('Introduce xi')))
error=float((input('Introduce la cota de error')))
iteraciones=float((input('Introduce la cantidad de iteraciones')))
lim=0
cota=0
xi2=0
while abs((ximasuno(ximenos1,xi)-xi)/ximasuno(ximenos1,xi)) > error and lim<iteraciones:
    lim+=1
    cota=abs((ximasuno(ximenos1,xi)-xi)/ximasuno(ximenos1,xi))
    xi2=ximasuno(ximenos1,xi)
    ximenos1=xi
    xi=xi2
    print('la iteracion: '+str(lim)+' nos da una raiz de: '+str(xi)+' con una cota de error de: '+str(cota))
print()
print('la solucion de la funcion dada por el metodo de la secante es: '+str(xi))
print('se hicieron '+str(lim)+" iteraciones")
