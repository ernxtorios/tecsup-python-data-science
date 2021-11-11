"""
Generar una matriz de 3 x 5 con números aleatorios
de los cuales:
- Cuantos números generados son mayores a 0.80
- Cuál es la suma de todos los números menores o iguales a 0.80
"""
import numpy

the_array = numpy.random.random(15).round(2).reshape(3, 5)
print("The array\n", the_array)

# ¿Cuantos números generados son mayores a 0.80?
print(f"¿Cuantos números generados son mayores a 0.80? {the_array[the_array > 0.80].size}")

# ¿Cuál es la suma de todos los números menores o iguales a 0.80?
print(f"¿Cuál es la suma de todos los números menores o iguales a 0.80? {the_array[the_array <= 0.80].sum().round(2)}")