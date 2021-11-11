import numpy as np
import pandas as pd

# Versión de Numpy
print(np.__version__)

# Versión de Pandas
print(pd.__version__)

# Crear un ndarray con los elementos
# de 1 al 99
array = np.array(range(1, 100))
print(array)

# Otra solución
nro_list = [i for i in range(1,100)]
np_arr = np.array(nro_list) 

# Crear un ndarray
# 9, 13, 17 , 21, 25
array_2 = np.arange(9, 26, 4)
print(array_2)

# Ejemplo
ceros_array = np.zeros((3,3))
print("np.zeros((3,3)) --> \n",ceros_array)
ceros_array_2 = np.zeros(9).reshape(3,3)
print("np.zeros(9) --> \n",ceros_array_2)

"""Generar la siguiente matriz
22  24  26
28  30  32
34  36  38
"""
array_3 = np.arange(22, 39, 2).reshape(3, 3)
print(array_3)

'''
Generar una matriz de
4 x 5 con numeros aleatorios
de 0 a 1
'''
array_4 = np.random.random((4, 5))
print(array_4)

"""
Generar una matriz 3x5 , que tengan 
numeros aleatorios de 0 a 100
"""
array_5 = np.random.random((3, 5))*100
print(array_5)

matriz_aleat =  np.random.random((3,5))
print(matriz_aleat * 100)

matriz_aleat =  np.random.random((3,5))
print(matriz_aleat * 100//1)

# Ejemplo
# Funcion numpy raiz cuadrada
a_array = np.arange(4)
b_array = np.arange(4,8)

print("------------------------------------")
c_array = a_array * np.sqrt(b_array)
print("a_array : \n",a_array)
print("b_array : \n",b_array)
print("np.sqrt(b_array) : \n",np.sqrt(b_array))
print("a_array * np.sqrt(b_array) : \n", c_array)

# Ejemplo
print("------------------------------------")
a_matriz = np.arange(0,16).reshape(4,4)
b_matriz = np.ones((4,4))
c_matriz = a_matriz*b_matriz
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("a_matriz * b_matriz : \n", c_matriz)
# The Matriz Product
print("------------------------------------")
c_matriz = np.dot(a_matriz,b_matriz)

#                    3 x 5    5 x 4  =  3 x 4 
print("a_matriz : \n",a_matriz)
print("b_matriz : \n",b_matriz)
print("np.dot(a_matriz,b_matriz) : \n", c_matriz )

'''
Multiplicar matricialmente estas 2 matrices
1 2 3     
4 5 6       
          
10  11 
12  13  
14  15
'''
array_x = np.arange(1, 7).reshape(2, 3)
array_y = np.arange(10, 16).reshape(3, 2)
print(array_x)
print(array_y)
array_z = np.dot(array_x, array_y)
print(array_z)

'''
Generar esta matriz
   2  4  6
   8 10 12
Elevar al cuadrado la matriz
y obtener lo siguiente:
El mayor valor
EL menor valor
'''
array_t = np.power(np.arange(2, 13, 2).reshape(2, 3), 2)
print(np.max(array_t))
print(np.min(array_t))

'''
Ejericio :
# idx   ->   0  1  2  3  4  5  6  7  8  9
# value -> [10 11 12 13 14 15 16 17 18 19]
Obtener todos los numeros que estan en posiciones
pares en el arreglo y sumarlos
'''
print(np.arange(10, 20)[::2])
print(np.arange(10, 20)[::2].sum())

'''
          [10 11 12 13 ]
          [14 15 16 17 ]
          [18 19 20 21 ]
          [22 23 24 25 ]
    
Obtener una matriz con las filas pares
y columnas impares
'''
array_dado = [[10, 11, 12, 13],
          [14, 15, 16, 17],
          [18, 19, 20, 21],
          [22, 23, 24, 25]]

array_nd = np.array(array_dado)
array_pedido = array_nd[::2, 1::2]
print(array_pedido)

# Ejemplo
a_m = np.apply_along_axis(np.round,
            axis=0, arr=a_matriz, decimals=2)
print(a_m)
a_m_1 =  np.round(a_matriz, decimals=2)
print(a_m_1)

# Ejemplo
def dummy(z):
    print("data =>",z)
    return z
a_matriz = np.arange(0,15).reshape(3,5)
a_matriz_resultado = np.apply_along_axis(dummy,
            axis=1, arr=a_matriz)
print(a_matriz)
print(a_matriz_resultado)
arr = np.arange(4)
print("==>>>",arr)
print("==>>>",np.mean(arr))
print("==>>>",np.round(arr))

""""
Ejercicio : Genera 20 numero aleatorios entre 0 y 100
y filtra los que son mayores o iguales a 80
"""
numeros = np.random.random((4,5))*100
print(numeros)
# numeros_2 = np.apply_along_axis(np.round, axis=1, arr=numeros, decimals=0)
numeros_2 = np.round(numeros)
print(numeros_2)
print(numeros_2[numeros_2 >= 80])

# Genera numeros enteros entre 0  y 100 en una matriz de 4x5
a_matriz = np.random.randint(100, size=(4, 5))

"""
  Crear una matriz de 2x8 con numeros aleatorios
  enteros y convertirlo en una matriz de 4x4
  Recomendacion : usar la funcion ravel()
"""
random_array = np.random.randint(100,size=(2,8))
random_array.ravel().reshape(4,4)

a_matriz = np.random.randint(100, size=(2, 8))
print (a_matriz)
a_matriz = a_matriz.ravel().reshape(4,4)
print (a_matriz)

# Generate inverse matrix
matriz_x = np.random.random(16).reshape(4,4)
inversa_matriz_x = np.linalg.inv(matriz_x)

print(inversa_matriz_x)
print(np.dot(matriz_x,inversa_matriz_x))
print(np.round(np.dot(matriz_x,inversa_matriz_x),10))

matrix_ide = np.identity(3)
print(matrix_ide)

'''
Genear la siguiente matriz
1 1 1 1 0 0
1 1 1 0 1 0
1 1 1 0 0 1
0 0 0 1 1 1
0 0 0 1 1 1
'''
c = np.identity(3)

# Solución
one = np.ones((3,3))
cero = np.zeros((3,3))
iden = np.identity(3)
ones = np.ones((2,3))
ceros = np.zeros((2,3))
union = [np.hstack((one,iden)),np.hstack((ceros,ones))]
union = np.vstack((union[0],union[1]))
print(union)

"""
Ejercicio Propuesto : generar una matriz donde se reemplaza
los pares por la letra P y los impares por la letra I
 2  3  4  5  6  7
 8  9 10 11 12 13
14 15 16 17 18 19
20 21 22 23 24 25
"""
# Pendiente de solución

# Otro tema
# Cortes personalizado a nivel de columna
print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("-"*40)
[b,c,d] = np.split(a,[2,3],axis=1)
print(b)
print("-"*40)
print(c)
print("-"*40)
print(d)
# Cortes personalizado a nivel de filas
print("------------------------------------")
a = np.arange(16).reshape((4, 4))
print(a)
print("-"*40)
[b,c,d] = np.split(a,[2,3],axis=0)
print(b)
print("-"*40)
print(c)
print("-"*40)
print(d)
