import math
def g(x):
    y=math.exp( -x )
    return (y)
#Programa principal
print ("Este programa encuentra una raíz, por el método de aproximaciones sucesivas")
xi=0
error=float((input('Introduce la cota de error')))
iteraciones=float((input('Introduce la cantidad de iteraciones')))
lim=0
cota=0
while abs((g(xi)-xi)/g(xi)) > error and lim<iteraciones:
    lim+=1
    cota=abs((g(xi)-xi)/g(xi))
    xi=g(xi)
    print('la iteracion: '+str(lim)+' nos da una raiz de: '+str(xi)+' con una cota de error de: '+str(cota))
print()
print('la solucion de la funcion dada por el metodo de aproximaciones sucesivas es: '+str(xi))
print('se hicieron '+str(lim)+" iteraciones")
