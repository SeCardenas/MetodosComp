import numpy as np
def integration_trapezoid(f, a, b, n):
    delta = (b-a)/float(n)
    integral = 0
    for i in range(n-1):
        integral = integral + delta*0.5*(f(a+delta*i)+f(a+delta*(i+1)))
    return integral

def integral_simpson(f, a, b, n):
    #Si el número de puntos es par, se resta uno para que quede impar.
    n = n + n%2 -1
    delta = (b-a)/float(n)
    integral = (f(a)+f(b))*delta
    impar = 1
    for i in range(1, n):
        #Coeficiente (2+2*impar) se alterna entre 2 y 4.
        integral = delta*(2+2*impar)*f(a+delta*i)
        impar = 1 - impar
    return integral/3.0

#Funcion rampa unitaria, auxiliar para montecarlo
def r(x):
    return x*(x>=0)

def integral_montecarlo(f, a, b, y_min, y_max, n):
    if y_min > 0:
        y_min = 0
    random_x_pos = np.random.rand(n)*(b-a) + a
    random_x_neg = np.random.rand(n)*(b-a) + a
    random_y_pos = np.random.rand(n)*y_max
    random_y_neg = np.random.rand(n)*y_min
    #Se divide la función en parte positiva y negativa.
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