'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Fundamentos de Estadistica
Fecha : 10/07/2020
Version : 1
Author : Jaime Gomez
'''

# ---------------------------------
# Using scipy.stats
# https://docs.scipy.org/doc/scipy/reference/stats.html
# ---------------------------------

import numpy as np
import scipy.stats as st

a_matrix = np.arange(0,16) #.reshape(4,4)
#b_matrix = np.array([1,1,1,1])
#a_matrix = np.append(a_matrix, b_matrix)

print("Sample data:")
print(a_matrix)

# Information in all data
print("Information in all data")
print("min =",st.tmin(a_matrix))
print("max =",st.tmax(a_matrix))
print("mode =",st.mode(a_matrix))
print("mean =",st.tmean(a_matrix))
print("var =",st.tvar(a_matrix, ddof=0))
print("std =",st.tstd(a_matrix, ddof=0))

