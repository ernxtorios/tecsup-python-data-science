'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 15/07/2020
Version : 1
Author : Jaime Gomez
Link : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

Link 2 : https://matplotlib.org/3.1.1/api/pyplot_summary.html

'''

import matplotlib.pyplot as plt
import numpy as np

#'''
# Los rangos de las X se definen :
LIM_INF = -10
LIM_SUP = 10
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y = x
titulo_label = "Función Lineal" 
x_label = "x"
y_label = "F(x)"
#'''

'''
# Los rangos de las X se definen :
LIM_INF = 0
LIM_SUP = 2 * np.pi
RAZON = 0.05
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y = np.sin(x)
titulo_label = "Función Seno" 
#titulo_label = b'Funci\xc3\xb3n Seno'.decode()
x_label = "Grados"
y_label = "Seno"
#'''

# Se imprime el gráfico
plt.plot(x, y)
plt.title(titulo_label)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()

# encode() y decode()

'''
print("------------------------------------")
s = "Perú"
print(s.encode())
b = b'Per\xc3\xba'
print(b.decode())

s = "Función Seno"
print(s.encode())
b = b'Funci\xc3\xb3n Seno'
print(b.decode())
#'''