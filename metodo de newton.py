import math
def f(x):
    #FUNCION ORIGINAL
    y=math.exp( -x )-x
    return (y)
def derf(r):
    #derivada de la funcion original
    h=-math.exp( -r )-1
    return (h)
def xmas1(o):
    g=(o-(f(o)/derf(o)))
    return (g)
#Programa principal
print ("Este programa encuentra una raíz, por el método de newton")
xi=0
error=float((input('Introduce la cota de error')))
iteraciones=float((input('Introduce la cantidad de iteraciones')))
lim=0
cota=0
while abs((xmas1(xi)-xi)/xmas1(xi)) > error and lim<iteraciones:
    lim+=1
    cota=abs((xmas1(xi)-xi)/xmas1(xi))
    xi=xmas1(xi)
    print('la iteracion: '+str(lim)+' nos da una raiz de: '+str(xi)+' con una cota de error de: '+str(cota))
print()
print('la solucion de la funcion dada por el metodo de newton es: '+str(xi))
print('se hicieron '+str(lim)+" iteraciones")
