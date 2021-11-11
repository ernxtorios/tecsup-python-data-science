'''
Crear en numpy los siguiente arreglos
   2, 4, 6, 8
   10,12,14,16

   1,3,5
   7,9,11
   13,15,17 
'''
import numpy

array_1 = numpy.arange(2, 17, 2).reshape(2, 4)
print(array_1)

array_2 = numpy.arange(1, 18, 2).reshape(3, 3)
print(array_2)