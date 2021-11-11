"""
EJERCICIOS:

- Maximo valor de la tercera columna
- Media de la primera fila
- La suma de todos los elementos del centro

        0    1   2   3
0 [ [ 2    4    6  8]
1   [10 12 14 16]
2   [18 20 22 24]]
"""
import numpy

the_array = numpy.arange(2, 25, 2).reshape(3, 4)
print("The array\n", the_array)

# El máximo de la tercera columna
print("El máximo de la tercera columna:", the_array[:, 2].max())

# Media de la primera fila
print("Media de la primera fila:", the_array[0,:].mean())

# La suma de todos los elementos del centro
print("La suma de todos los elementos del centro:", the_array[:, 1:3].sum())
