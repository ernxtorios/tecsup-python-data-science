"""
Ejercicio 1 (6 puntos)
Generar la siguiente matriz usando Numpy
1 3 5
7 9 11
13 15 17
Elevar al cuadrado la matriz y obtener el mayor y menor valor
"""
import numpy

# Generar la matriz
the_array = numpy.arange(1, 18, 2).reshape(3, 3)
print(the_array)

# Elevar al cuadrado la matriz
the_array_square = numpy.power(the_array, 2)
print(the_array_square)

# Obtener el mayor y menor valor
print("El mayor valor", numpy.max(the_array_square))
print("El menor valor", numpy.min(the_array_square))