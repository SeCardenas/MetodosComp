import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
a = np.loadtxt('trm.txt', delimiter=',')
b = sc.fft(a[:,1])/len(a)
dt = 1/365.0
f = np.fft.fftfreq(len(a), dt)
fpos = np.where(f>0)
plt.semilogx(f[fpos], abs(np.real(b[fpos])))
plt.savefig('FFT-trm.pdf')
plt.close()

#b[np.where(abs(f)>1.0/7)]=0
ffiltrado = b*(abs(f)<1.0/7)
datoslimpios = sc.ifft(ffiltrado)
dias = a[:,0]
ultimos = np.where(dias>=len(a)-365*3)
plt.plot(dias[ultimos], datoslimpios[ultimos])
#plt.show()
plt.savefig('trm 3years limpio.pdf')
