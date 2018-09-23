import numpy as np
import matplotlib.pyplot as plt
def pol(x):
    return x**5-2*x**4-10*x**3+20*x**2+9*x-18

def polprime(x):
    return 5*x**4-8*x**3-30*x**2+40*x+9

def NewtonRaphson(f, fprime, x0, e=10**(-10)):
    xr = x0
    nsteps = 0
    while abs(f(xr)) > e:
        if fprime(xr) != 0:
            xr = xr - f(xr)/fprime(xr)
        else:
            xr = xr + 0.001
            print "derivada 0:", xr
        nsteps = nsteps + 1
    return xr, nsteps

#xgess = -3
xr = NewtonRaphson(pol, polprime, -3, 0)[0]
print "para xgess = -3, el valor de xr es", xr, "y el valor de f(xr) es", pol(xr)
#xgess = -1
xr = NewtonRaphson(pol, polprime, -1, 0)[0]
print "para xgess = -1, el valor de xr es", xr, "y el valor de f(xr) es", pol(xr)

x0 = np.linspace(-4, 4, 1000)
plt.plot(x0, pol(x0))
plt.title("Polinomio")
plt.savefig("CardenasSergio_NRpoli.pdf")

#numero de iteraciones
x0 = np.random.rand(1000)*8 - 4
a = np.array([NewtonRaphson(pol, polprime, x0i) for x0i in x0])
plt.scatter(x0, a[:,1], alpha=0.5)
plt.title("Numero de iteraciones")
plt.savefig("CardenasSergio_NR_itera.pdf")

#raices encontradas
plt.scatter(x0, a[:,0], alpha=0.5)
plt.title("Raices encontradas")
plt.savefig("CardenasSergio_NRxguess.pdf")

print "Se puede onservar que el numero de iteraciones necesarias para encontrar una raiz es elevado cuando xguess esta cerca de un valor cuya derivada se acerca a 0, esto se debe a que en estos puntos, el siguiente valor para xr se aleja mucho de los ceros de la funcion, por lo que deben pasar mas iteraciones de lo habitual para que xr vuelva a acercarse a una raiz. En estos puntos, se ve que el valor final de xr puede variar mucho con diminutos cambios en xguess; distinto a lo que pasa en otros puntos, donde el valor final de xr es el mismo para todos los puntos de ciertos intervalos (donde los puntos estan alejados de derivada = 0)."
