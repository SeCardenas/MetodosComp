import numpy as np
def integral_trapezoid(f, a, b, n):
    delta = float(b-a)/(n-1)
    integral = 0
    for i in range(n-1):
        integral = integral + delta*0.5*(f(a+delta*i)+f(a+delta*(i+1)))
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
	integ_neg = -y_min*abs(b-a)*np.size(above)/float(n)
	integral = integ_pos - integ_neg
	#si a > b, integral = -integral
	integral = ((b-a)/abs(b-a))*integral
	return integral

def integral_meanvalue(f, a, b, n):
	x = np.random.rand(n) * (b - a) + a
	y = f(x)
	return np.average(y) * (b-a)

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

numPoints = np.logspace(2, 7, 6) + 1
print numPoints
print integral_trapezoid(np.cos, a, b, numPoints)
#plt.loglog(numPuntos, abs(-analitic_int)/float(analitic_int))
