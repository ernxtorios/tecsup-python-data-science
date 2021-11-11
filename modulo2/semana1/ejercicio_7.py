'''
Usando la función np.apply_along_axis realizar el cálculo en cada celda
[10 11 12 13 ]
[14 15 16 17 ]
[18 19 20 21 ]
[22 23 24 25 ]
 2
x + x + 1

   2
10 + 10 + 1 = 111
'''
import numpy

the_array = numpy.arange(10, 26).reshape(4, 4)
print(the_array)

def the_equation(x):
    return numpy.power(x, 2) + x + 1

print(numpy.apply_along_axis(the_equation, axis=1, arr=the_array))
