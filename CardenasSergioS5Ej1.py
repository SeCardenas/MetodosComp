import numpy as np
def gauss_jordan(a):
	numRows = len(a)
	for i in range(numRows):
		#Cambiar columnas
		for j in range(i+1, numRows):
			if a[i,i] != 0:
				break
			a[[i,j]] = a[[j,i]]
		#Dejar un 1 en la diagonal
		if a[i,i] != 0.0:
			a[i] = a[i]/float(a[i,i])
		#Restar en las demas filas
		for j in range(numRows):
			if j != i:
				a[j] = a[j]-a[i]*a[j,i]
	return a

a = np.array([[1,-2,3,11],[4,1,-1,4], [2,-1,3,10]], dtype=np.float64)
print gauss_jordan(a)
