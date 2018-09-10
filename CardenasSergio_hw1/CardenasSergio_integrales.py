import numpy as np
import matplotlib.pyplot as plt
def integral_trapezoid(f, a, b, n):
    delta = float(b-a)/(n-1)
    integral = 0
    for i in range(n-1):
        integral = integral + delta*0.5*(f(a+delta*i)+f(a+delta*(i+1)))
    return integral

def integral_trapezoid2(f, a, b, n):
    delta = float(b-a)/(n-1)
    x = np.linspace(a, b, n)
    y = f(x)*delta
    y[0] = y[0]*0.5
    y[n-1] = y[n-1]*0.5
    integral = sum(y)
    if a>b: integral = -integral
    return integral

def integral_simpson(f, a, b, n):
    #Si el numero de puntos es par, se suma uno para que quede impar.
    n = n + 1 - n%2
    delta = float(b-a)/(n-1)
    integral = (f(a)+f(b))*delta
    impar = 1
    for i in range(1, n-1):
        #Coeficiente (2+2*impar) se alterna entre 2 y 4.
        integral = integral + delta*(2+2*impar)*f(a+delta*i)
        impar = 1 - impar
    return integral/3.0

def integral_simpson2(f, a, b, n):
    #Si el numero de puntos es par, se suma uno para que quede impar.
    n = n + 1 - n%2
    delta = float(b-a)/(n-1)
    x = np.linspace(a,b,n)
    indexes = np.linspace(1,n,n)
    y = f(x)*delta*(4-2*(indexes%2))
    y[0] = y[0]/2.0
    y[n-1] = y[n-1]/2.0
    integral = sum(y)/3.0
	if a>b:
		integral = -integral
    return integral

#Funcion rampa unitaria, auxiliar para montecarlo
def r(x):
    return x*(x>=0)

def integral_montecarlo(f, a, b, n, y_min = -1, y_max = 1):
	if y_min > 0:
		y_min = 0
	random_x_pos = np.random.rand(n)*(b-a) + a
	random_x_neg = np.random.rand(n)*(b-a) + a
	random_y_pos = np.random.rand(n)*y_max
	random_y_neg = np.random.rand(n)*y_min
	#Se divide la funcion en parte positiva y negativa.
	delta_pos = r(f(random_x_pos)) - random_y_pos
	delta_neg = -r(-f(random_x_neg)) - random_y_neg
	below = np.where(delta_pos>0.0)
	above = np.where(delta_neg<0.0)
	integ_pos = y_max*abs(b-a)*np.size(below)/float(n)
	integ_neg = y_min*abs(b-a)*np.size(above)/float(n)
	integral = integ_pos + integ_neg
	#si a > b, integral = -integral
	integral = ((b-a)/abs(b-a))*integral
	return integral

def integral_meanvalue(f, a, b, n):
	x = np.random.rand(n) * (b - a) + a
	y = f(x)
	return np.average(y) * (b-a)

def f_c(x):
	return 1.0/np.sqrt(np.sin(x))

def f_c_sin_sing(x):
	if x==0: return 10**6
	return 1.0/np.sqrt(np.sin(x))

def f_c2(x):
	if x==0: return 0 #Este es el valor del limite
	return 1.0/np.sqrt(np.sin(x))-1.0/np.sqrt(x)

analitic_int = 1
a = -np.pi/2.0
b = np.pi
Np = 10001
int_trapezoids = integral_trapezoid(np.cos, a, b, Np)
err_trapezoids = abs(int_trapezoids-analitic_int)/float(analitic_int)
print "metodo: trapezoides, valor de la integral:", int_trapezoids,", error:", err_trapezoids
int_simpson = integral_simpson(np.cos, a, b, Np)
err_simpson = abs(int_simpson-analitic_int)/float(analitic_int)
print "metodo: Simpson, valor de la integral:", int_simpson,", error:", err_simpson
int_mc = integral_montecarlo(np.cos, a, b, Np)
err_mc = abs(int_mc-analitic_int)/float(analitic_int)
print "metodo: Monte-Carlo, valor de la integral:", int_mc,", error:", err_mc
int_mv = integral_meanvalue(np.cos, a, b, Np)
err_mv = abs(int_mv-analitic_int)/float(analitic_int)
print "metodo: Valores medios, valor de la integral:", int_mv,", error:", err_mv

numPoints = np.logspace(2, 7, 6, dtype=np.dtype(np.int32)) + 1
print numPoints
trapezoids_n = np.array([integral_trapezoid2(np.cos, a, b, numPoints_i) for numPoints_i in numPoints])
print trapezoids_n
simpson_n = np.array([integral_simpson2(np.cos, a, b, numPoints_i) for numPoints_i in numPoints])
print simpson_n
mc_n = np.array([integral_montecarlo(np.cos, a, b, numPoints_i) for numPoints_i in numPoints])
print mc_n
mv_n = np.array([integral_meanvalue(np.cos, a, b, numPoints_i) for numPoints_i in numPoints])
print mv_n
plt.loglog(numPoints, abs(trapezoids_n-analitic_int)/float(analitic_int))
plt.loglog(numPoints, abs(simpson_n-analitic_int)/float(analitic_int))
plt.loglog(numPoints, abs(mc_n-analitic_int)/float(analitic_int))
plt.loglog(numPoints, abs(mv_n-analitic_int)/float(analitic_int))
plt.show()

n = 1025
a1 = 0
a2 = 10**(-6)
b = 1
trapezoids_c = integral_trapezoid(f_c, a1, b, n)
simpson_c = integral_simpson(f_c, a1, b, n)
mc_c = integral_montecarlo(f_c, a1, b, n, 0, 100)
mv_c = integral_meanvalue(f_c, a1, b, n)
print "La integral con simgularidad vale", trapezoids_c, "con el metodo del Trapezoide,", simpson_c, "con Simpson,", mc_c, "con Monte Carlo y", mv_c, "con Valores Medios"

trapezoids_c = integral_trapezoid(np.vectorize(f_c_sin_sing), a1, b, n)
simpson_c = integral_simpson(np.vectorize(f_c_sin_sing), a1, b, n)
mc_c = integral_montecarlo(np.vectorize(f_c_sin_sing), a1, b, n, 0, 100)
mv_c = integral_meanvalue(np.vectorize(f_c_sin_sing), a1, b, n)
print "El nuevo valor de la integral usando el metodo del Trapezoide cambiando infinito por 10^6 es", trapezoids_c
print "El nuevo valor de la integral usando el metodo de Simpson cambiando infinito por 10^6 es", simpson_c
print "El nuevo valor de la integral usando el metodo de Monte Carlo cambiando infinito por 10^6 es", mc_c
print "El nuevo valor de la integral usando el metodo de Valores Medios cambiando infinito por 10^6 es", mv_c

trapezoids_c = integral_trapezoid(f_c, a2, b, n)
simpson_c = integral_simpson(f_c, a2, b, n)
mc_c = integral_montecarlo(f_c, a2, b, n, 0, 100)
mv_c = integral_meanvalue(f_c, a2, b, n)
print "El nuevo valor de la integral usando el metodo del Trapezoide evaluando la función en 10^-6 y no en 0 es", trapezoids_c
print "El nuevo valor de la integral usando el metodo de Simpson evaluando la función en 10^-6 y no en 0 es", simpson_c
print "El nuevo valor de la integral usando el metodo de Monte Carlo evaluando la función en 10^-6 y no en 0 es", mc_c
print "El nuevo valor de la integral usando el metodo de Valores Medios evaluando la función en 10^-6 y no en 0 es", mv_c

analitic_int2 = 2
trapezoids_c = integral_trapezoid1(f_c2, a1, b, n) + analitic_int2
simpson_c = integral_simpson2(f_c2, a1, b, n) + analitic_int2
mc_c = integral_montecarlo(np.vectorize(f_c2), a1, b, n, 0, 10) + analitic_int2
mv_c = integral_meanvalue(np.vectorize(f_c2), a1, b, n) + analitic_int2
print "Restando la singularidad el resultado es", trapezoids_c, "con el metodo del Trapezoide,", simpson_c, "con Simpson,", mc_c, "con Monte Carlo y", mv_c, "con Valores Medios"
print "De todos los metodos, el que mas se acerca al valor real es Simpson, siempre y cuando se elimine la singularidad o no se evalue en ella."