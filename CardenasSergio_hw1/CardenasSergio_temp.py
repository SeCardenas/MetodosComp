import numpy as np
import matplotlib.pyplot as plt
file = open("647_Global_Temperature_Data_File.txt", "r")
years = np.array([])
anoms = np.array([])
anoms2 = np.array([])
for line in file:
    a = line.split("\t")
    years = np.append(years, int(a[0]))
    anoms = np.append(anoms, float(a[1]))
    anoms2 = np.append(anoms2, float(a[2]))
plt.plot(years, anoms)
plt.title("Anomalias de temperatura")
plt.savefig("Grafica_temp.pdf")

indexes = np.where(anoms>0.5)
print "anomalias mayores a 0.5:"
print years[indexes]
