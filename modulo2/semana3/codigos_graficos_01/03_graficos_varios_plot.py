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
y1 = x
y2 = 4 * x
y3 = 8 * x
titulo_label = "Gráfico de lineas" 
x_label = "x"
y_label = "F(x)"
#'''

# Se imprime el gráfico
plt.plot(x, y1, label="linea 1")
plt.plot(x, y2, label="linea 2")
plt.plot(x, y3, label="linea 3")
plt.title(titulo_label)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
plt.show()


'''
# Se imprime el gráfico
plt.plot(x, y1, label="linea 1")
plt.plot(x, y2, label="linea 2")
plt.plot(x, y3, label="linea 3")
plt.title(titulo_label)
# Setear limites
#plt.xlim(1,8)
#plt.ylim(40,60)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend()
#plt.grid()
#plt.grid(color='b', ls = '-.', lw = 0.25)
#plt.savefig("mi_grafico")
plt.show()
#'''