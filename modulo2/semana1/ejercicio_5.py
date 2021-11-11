'''
Se quiere aplicar un modelo de una regresión lineal
de la forma y = bo + b1*x
a la matriz
[[ 2 4 6 8]
[10 12 14 16]
[18 20 22 24]]
Donde b1, es la media de los datos y bo es 10

2 --> 10 + 23*2 = 56
'''
import numpy

the_array = numpy.arange(2, 25, 2).reshape(3, 4)
print("The array\n", the_array)

bo = 10
b1 = the_array.mean()

print(f"Modelo de regresión lineal y = bo + b1*x con bo = {bo} y b1 = {b1} para y = 2 resulta {bo + b1*2}")