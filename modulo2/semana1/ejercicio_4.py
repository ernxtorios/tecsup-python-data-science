""" 
Desarrollar la siguiente matriz con Numpy
2    4    6    8
10  12   14   16 
18  20   22   24
Calcular la suma de todos los elementos, el mayor valor, el menor valor y la media
"""
import numpy

the_array = numpy.arange(2, 25, 2).reshape(3, 4)
print("The array\n", the_array)

# La suma de todos los elementos
print("La suma de todos los elementos:", the_array.sum())

# El mayor valor
print("El mayor valor:", the_array.max())

# El menor valor
print("El menor valor:", the_array.min())

# La media
print("La media:", the_array.mean())