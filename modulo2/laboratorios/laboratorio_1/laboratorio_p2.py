"""
Ejercicio 2 (7 puntos)
Generar la siguiente matriz usando Numpy
100 110 120
130 140 150
170 190 210
Generar una nueva matriz aplicando la ecuación a cada elemento de la matriz:
3x3 + x2 − 10x + 4
"""
import numpy
from numpy.lib import type_check

# Generar la matriz
the_part_1 = numpy.arange(100, 151, 10).reshape(2, 3)
the_part_2 = numpy.arange(170, 211, 20)
the_array = numpy.row_stack((the_part_1, the_part_2))
print(the_array)

def the_function(x):
    return 3*x**3 + x**2 - 10*x + 4

# Generar la nueva matriz
the_new_array = numpy.apply_along_axis(the_function, axis=0, arr=the_array)
print(the_new_array)