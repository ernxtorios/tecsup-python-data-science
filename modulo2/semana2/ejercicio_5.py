# Ejercicio 3 : crear la funcion
#     nombre : obtener_var_muestral
#     argumento : una matriz
#     retornar : la varianza muestral de la matriz
#  Usar la funcion. 
import numpy as np

def obtener_var_muestral(a_matrix):
    tmp_matrix = a_matrix.copy()
    tmp_matrix = tmp_matrix - tmp_matrix.mean()
    tmp_matrix = np.power(tmp_matrix,2)
    var = tmp_matrix.sum()/(tmp_matrix.size-1)
    return var

a_matrix = np.arange(0,16).reshape(4,4)
print(obtener_var_muestral(a_matrix))

print("variance poblacional =",np.var(a_matrix))
print("variance muestral    =",np.var(a_matrix,ddof=1))