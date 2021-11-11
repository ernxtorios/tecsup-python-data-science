# Ejercicio 2 : crear la funcion
#     nombre : obtener_var_pob
#     argumento : una matriz
#     retornar : la varianza poblacion de la matriz
#  Usar la funcion.  
import numpy as np

def obtener_var_pob(matrix):
    matrix_copy = matrix.copy()
    matrix_copy = matrix_copy - np.mean(matrix_copy)
    matrix_copy = np.power(matrix_copy, 2)
    
    return np.mean(matrix_copy)

a_matrix = np.arange(0,16).reshape(4,4)
print(obtener_var_pob(a_matrix))
print(np.var(a_matrix))  
