import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.integrate as integ
#Punto 1 y 2
def f(x):
	return (35*x**4-30*x**2+3)/8.0

N = int(float(sys.argv[1]))
Np = int(float(sys.argv[2]))

x = np.linspace(-1.0, 1.0, N)
plt.plot(x, f(x))
plt.show()

#Punto 3
def F(x):
	return(7*x**5-10*x**3+3*x)/8.0
int_analitica = F(1)-F(-1)
print "Valor analitico de la integral:", int_analitica

#Punto 4
def r(x):
	return x*(x>=0)

plt.plot(x, r(f(x)))
plt.plot(x, -r(-f(x)))
plt.show()

#Punto 5
random_x_pos = np.random.rand(Np)*2-1
random_x_neg = np.random.rand(Np)*2-1
random_y_pos = np.random.rand(Np)
random_y_neg = np.random.rand(Np)*-1

delta_pos = r(f(random_x_pos)) - random_y_pos
delta_neg = -r(-f(random_x_neg)) - random_y_neg
below = np.where(delta_pos>0.0)
above = np.where(delta_neg<0.0)

x_in = np.append(random_x_pos[below],random_x_neg[above])
y_in = np.append(random_y_pos[below],random_y_neg[above])

integ_pos = 2*np.size(below)/float(Np)
integ_neg = 2*np.size(above)/float(Np)
integral = integ_pos - integ_neg
print "El valor de la integral con MC es", integral

plt.scatter(x_in, y_in)
plt.show()
#Punto 6
print "El error de la integral con MC es", abs(integral-int_analitica)

#Punto 7
integral_2 = integ.quad(f, -1, 1)
print "El valor de la integral con quad es", integral_2[0]
print "El error real de la integral con quad es", integral_2[0]-int_analitica
print "El valor estimado del error de la integral con quad es", integral_2[1]
