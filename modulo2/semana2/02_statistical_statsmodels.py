'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Fundamentos de Estadistica
Fecha : 10/07/2020
Version : 1
Author : Jaime Gomez
'''

# ---------------------------------
# Using DescrStatsW
#https://www.statsmodels.org/dev/generated/statsmodels.stats.weightstats.DescrStatsW.html#statsmodels.stats.weightstats.DescrStatsW
# ---------------------------------


import numpy as np
import statsmodels.api as statmod

print(statmod.__version__)

a_matrix = np.arange(0,16) #.reshape(4,4)
print("Sample data:")
print(a_matrix)

# Construct a DescrStatsW instance

descriptive = statmod.stats.DescrStatsW(a_matrix, ddof=0) # degrees of freedom correction

# Print the mean of each column
print("Mean:")
print(descriptive.mean)

print("Var:")
print(descriptive.var)

print("Std:")
print(descriptive.std)

