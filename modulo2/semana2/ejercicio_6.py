"""  Ejercicio
En la siguiente muestra :
 4,6,7,8,10,14,18,13,29,33,46,70 
Calcular media, mediana, std muestral, varianza muestral, cuartiles
"""
import numpy as np

matrix = np.array([4,6,7,8,10,14,18,13,29,33,46,70])
print("media:",matrix.mean())
print("mediana:",np.median(matrix))
print("std muestral:",matrix.std(ddof=1))
print("varianza muestral:",matrix.var(ddof=1))
print("cuartiles:",np.quantile(matrix,q=[0.25,0.5,0.75]))

lista = [4,6,7,8,10,14,18,13,29,33,46,70]
np_array = np.array(lista)
QUANTILES = [0.25, 0.50, 0.75]
print("Media: ", np.mean(np_array))
print("Mediana: ", np.median(np_array))
print("Desviación Estándar Muestral: ", np.std(np_array, ddof=1))
print("Varianza Muestral: ", np.var(np_array, ddof=1))
print("Cuartiles:", np.quantile(np_array, q=QUANTILES))