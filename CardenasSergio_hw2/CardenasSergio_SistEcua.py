import numpy as np
N=np.random.randint(3 , 8)
print (N)
Arreglo=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-5.0
solnp = np.linalg.solve(Arreglo, B)
print (Arreglo)
print (B)
def gauss_jordan(a, b):
  numRows = len(a)
  #Se construye la matriz aumentada porque si trabajo directamente con B, este no cambia (no se la razon de eso)
  m = np.append(a, b, axis=1)
  for i in range(numRows):
    #Cambiar filas en caso de que haya ceros en la diagonal
    for j in range(i+1, numRows):
      if m[i,i] != 0:
        break
      m[[i,j]] = m[[j,i]]
    #Dejar un 1 en la diagonal (si no es singular)
    if m[i,i] != 0.0:
      m[i] = m[i]/(m[i,i])
    #Restar en las demas filas
    for j in range(i+1, numRows):
      m[j] = m[j]-m[i]*m[j,i]
  #Se retorna A reducida y b'
  return m[:,:-1], m[:,-1:]

Arreglo, B = gauss_jordan(Arreglo, B)

print (Arreglo)
print (B)

#Obtener x a partir de b'
Solucion = np.zeros((N,1))
for i in range(N):
  index = N-i-1
  Solucion[index] = B[index]
  for j in range(N-i, N):
    Solucion[index] = Solucion[index] - Solucion[j]*Arreglo[index,j]
print "solucion:"
print Solucion
print "solucion de numpy:"
print solnp
print "Comparacion:"
print np.allclose(Solucion, solnp)
