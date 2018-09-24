import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

#derivada de adelanto
def derivative(arr, h):
    return (arr[1:]-arr[:-1])/h

data = np.loadtxt('chicamocha.txt')
datax = datos[:,0]
datay = datos[:,1]

x = np.linspace(0,12,500)
ylin = interp.interp1d(datax, datay, kind="linear")(x)
ycuad = interp.interp1d(datax, datay, kind="quadratic")(x)
ycub = interp.interp1d(datax, datay, kind="cubic")(x)
plt.scatter(datax, datay, label="datos")
plt.plot(x, ylin, label="interpolacion lineal")
plt.plot(x, ycuad, label="interpolacion cuadratica")
plt.plot(x, ycub, label="interpolacion cubica")
plt.title("interpolacion con splines")
plt.legend()
plt.savefig("CardenasSergio_Interpola.pdf")

plt.scatter(datax[:-1], derivative(datay, datax[1]-datax[0]), label="datos")
plt.plot(x[:-1], derivative(ylin, x[1]-x[0]), label="interpolacion lineal")
plt.plot(x[:-1], derivative(ycuad, x[1]-x[0]), label="interpolacion cuadratica")
plt.plot(x[:-1], derivative(ycub, x[1]-x[0]), label="interpolacion cubica")
plt.title("Derivadas (de adelanto) de las interpolaciones y de los datos")
plt.legend()
plt.savefig("CardenasSergio_Deriv.pdf")
