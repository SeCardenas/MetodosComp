import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('data_mean_sq.txt')
x = data[:,0]
y = data[:,1]
#Se construye la matriz A de la ecuacion A*x=y, donde x = [m, b], B = datosy
A = np.ones((len(x), 2))
A[:,0] = x
#Se multiplica por la transpuesta a ambos lados de la ecuacion
A2 = np.matmul(np.transpose(A), A)
B = np.matmul(np.transpose(A), y)
#Se calculan m y b
m, b = np.matmul(np.linalg.inv(A2), B)
print "valor calculado para m:", m
print "valor calculado para b:", b
#grafica
datosx = np.linspace(0, 35, 36)
plt.scatter(x, y)
plt.plot(datosx, m*datosx+b)
plt.show()

#literal b
def generateData(x):
    return np.maximum(10*np.exp(-x/0.5) + np.random.normal(0, 0.03, x.shape), np.exp(-15)) #Se hace para que los datos no den negativos
#generacion de datos
x = np.linspace(0, 6, 30, endpoint=False)
y = np.zeros((10, 30))
lny = np.zeros((10,30))
for i in range(10):
    y[i] = generateData(x)
#linealizacion: lny = -x/tau + lnA => lny = M*b
lny = np.log(y)
oneovertau = np.zeros(10)
lnA = np.zeros(10)
M = np.ones((len(x), 2))
M[:,0] = -x
#minimos cuadrados
MT = np.transpose(M)
M2 = np.matmul(MT, M)
for i in range(10):
    B = np.matmul(MT, lny[i])
    oneovertau[i] , lnA[i] = np.matmul(np.linalg.inv(M2), B)
tau = 1/oneovertau
A = np.exp(lnA)
print "la varianza de los valores calculados para tau es", np.var(tau)
print "la varianza de los valores calculados para A es", np.var(A)


