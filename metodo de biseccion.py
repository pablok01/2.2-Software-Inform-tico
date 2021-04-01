def f(xi):
    x=xi**3+4*xi**2-10
    return(x)
def f2(xs):
    y=xs**3+4*xs**2-10
    return(y)
def xr(xi,xs):
    z=(xi+xs)/2
    return(z)
def fxr(a,b):
    w=xr(a,b)**3+4*xr(a,b)**2-10
    return(w)
#Programa principal
print ("Este programa encuentra una raíz, por el metodo de biseccion")
xi=float((input('Introduce xi')))
xs=float((input('Introduce xs')))
error=float((input('Introduce la cota de error')))
iteraciones=float((input('Introduce la cantidad de iteraciones')))
lim=0
cota=0
raiz=0
if(f(xi)*f2(xs)<0):
    while abs((xr(xi,xs)-xi)/xr(xi,xs))> error and lim<iteraciones:
        raiz=xr(xi,xs)
        cota=abs((xr(xi,xs)-xi)/xr(xi,xs))
        lim+=1
        print('la iteracion: '+str(lim)+' nos da una raiz de: '+str(raiz)+' con una cota de error de: '+str(cota))
        if(fxr(xi,xs)*f(xi)==0):
            raiz=xr(xi,xs)
            lim>iteraciones
        elif(fxr(xi,xs)*f(xi)<0):
            xs=xr(xi,xs)
            xi=xi
        else:
            xi=xr(xi,xs)
            xs=xs
       
        
else:
    print('los dos intervalos dados son mayores a 0 introduzca otros')
print()
print('la solucion de la funcion dada por el metodo biseccion es: '+str(xi))
print('se hicieron '+str(lim)+" iteraciones")
