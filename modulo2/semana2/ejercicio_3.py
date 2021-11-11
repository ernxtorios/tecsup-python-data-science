# Ejercicio : calcular la varianza poblacional
#             usando la definición
import numpy as np

a_matrix = np.arange(0,16).reshape(4,4)
print(a_matrix.var())
a_matrix = a_matrix - a_matrix.mean()
a_matrix = a_matrix**2
var = a_matrix.mean()
print(var)

a_matrix = np.arange(0,16).reshape(4,4)
print(a_matrix.var())
a_matrix_v = a_matrix.copy()
a_matrix_v = a_matrix_v- a_matrix_v.mean()
a_matrix_v = a_matrix_v**2
var = a_matrix_v.mean()
print(var)

