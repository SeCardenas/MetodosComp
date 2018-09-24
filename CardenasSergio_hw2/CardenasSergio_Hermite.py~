import numpy as np
import matplotlib.pyplot as plt
def exp_interno(x):
    return np.exp(-x**2)

def derivative(arr, h):
	return (arr[1:] - arr[0:-1])/float(h)

def nderivative(arr, h, n):
    if n == 0:
        return arr
    return nderivative(derivative(arr, h), h, n-1)

def Hn(x, n):
    if n == 0:
        return np.ones(len(x)) #H0(x) = 1
    return np.exp(x[:-n]**2)*nderivative(exp_interno(x), x[1]-x[0], n) #La derivada quita un valor al arreglo, por lo que se hace x[:-n] para que las dimensiones coincidan.

N = 7
#para 50 puntos
x = np.linspace(-2.5, 2.5, 50)
plt.plot(x, Hn(x, 0), label="H0") #H0
for i in range(1, N+1):
    plt.plot(x[:-i], Hn(x, i), label="H"+str(i)) #Hi
plt.ylim(-25, 25)
plt.legend()
plt.savefig("CardenasSergio_Hermite.pdf")

#para 500 puntos
x = np.linspace(-2.5, 2.5, 500)
plt.plot(x, Hn(x, 0), label="H0") #H0
for i in range(1, N+1):
    plt.plot(x[:-i], Hn(x, i), label="H"+str(i)) #Hi
plt.ylim(-25, 25)
plt.legend()
plt.savefig("CardenasSergio_Hermite_10.pdf")
