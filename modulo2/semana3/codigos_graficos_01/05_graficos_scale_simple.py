'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 15/07/2020
Version : 1
Author : Jaime Gomez
Link : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

'''

import matplotlib.pyplot as plt
import numpy as np


#'''
# Los rangos de las X se definen :
LIM_INF = -10
LIM_SUP = 10
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y = np.exp(x)
titulo_label = "Función Exponencial" 
x_label = "x"
y_label = "Exp(x)"
#'''

# Se imprime el gráfico
plt.plot(x, y)
plt.title(titulo_label)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.yscale("log")
plt.grid()
plt.show()

