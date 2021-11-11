
'''
Dado los siguientes listas, 
A = [1,  2, 3, 4, 5, 6]
B = [1 , 1, 0, 0, 0, 1]

Realizar:
- Convertir A y B a un array numpy
- Hallar la transpuesta de B, que se llamara BT
- Multiplicar vectorial A X BT
'''
import numpy

A = [1,  2, 3, 4, 5, 6]
B = [1 , 1, 0, 0, 0, 1]

print("Lista A\n", A)
print("Lista B\n", B)


# Convertir A y B a un array numpy
A = numpy.array(A)
B = numpy.array(B)

print("Array A\n", A)
print("Array B\n", B)

# Hallar la transpuesta de B, que se llamara BT

BT = B.transpose()

print("Array Transpose B\n", BT) 

# Multiplicar vectorial A X BT
print("Multiplicar vectorial A X BT", numpy.dot(A, BT))