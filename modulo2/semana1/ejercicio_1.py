import numpy as np

arr_np = np.arange(4)
print(arr_np)   # [0 1 2 3]
vista_arr_np = arr_np[0:2]
print(vista_arr_np) 
arr_np[1] = 0
print(vista_arr_np.sum())

"""
Ejercicio:
   
    Sacar una copia de arr_np
    Crear una vista con las posicion impares
    Realizar la suma de la vista anterior
"""
arr_np = np.arange(10)
arr_np_copy = arr_np.copy()
arr_np_copy[5] = -1
vista = arr_np[1::2]
print("arr_np", arr_np)
print("arr_np_copy", arr_np_copy)
print("vista", vista)
print("suma de elementos de la vista", vista.sum())
