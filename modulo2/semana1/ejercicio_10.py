"""
Generar la siguiente matriz usando numpy

A A A B B B B

A A A B B B B

A A A B B B B

C C C C C C C

C C C C C C C

C C C C C C C

C C C C C C C 

Considerar que:
A = 4
B = 5
C = 10
"""
import numpy

matriz_a = numpy.ones((3, 3))*4
matriz_b = numpy.ones((3, 4))*5
matriz_c = numpy.ones((4, 7))*10

print("A\n", matriz_a)
print("B\n", matriz_b)
print("C\n", matriz_c)

matriz_t = numpy.hstack((matriz_a, matriz_b))

matriz_x = numpy.vstack((matriz_t, matriz_c))

print("Matriz pedida\n", matriz_x)