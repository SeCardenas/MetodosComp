import numpy as np
import matplotlib.pyplot as plt
file = open("647_Global_Temperature_Data_File.txt", "r")
years = np.array([])
anoms = np.array([])
anoms2 = np.array([])
for line in file:
    a = line.split("\t")
    years = np.append(years, [a[0]])
    anoms = np.append(anoms, [a[1]])
    anoms2 = np.append(anoms2, [a[2]])
