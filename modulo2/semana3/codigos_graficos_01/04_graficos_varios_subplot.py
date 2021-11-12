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

# Los rangos de las X se definen :
LIM_INF = 0
LIM_SUP = 2 * np.pi
RAZON = 0.05
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = 1/np.tan(x)
#titulo_label = b'Funci\xc3\xb3n Seno'.decode()
x_label = "Grados"
y_label = "Funciones Trigonométricas"

# ------------------------------------------
#            1           2
#      -------------------------
#      |           |           |
#   1  |     1     |     2     |
#      |           |           |
#      |-----------------------|
#      |           |           |
#   2  |     3     |     4     |
#      |           |           |
#      |-----------------------|
#
# ------------------------------------------

# Se imprime el gráfico 

'''
# Forma 1 : subplot()
plt.subplot(2,2,1)
plt.title("Sen.")
plt.plot(x, y1 ) #,'.c')

plt.subplot(2,2,2)
plt.title("Cos.")
plt.plot(x, y2)

plt.subplot(2,2,3)
plt.title("Tan.")
plt.plot(x, y3)
plt.ylim(-10,10)

plt.subplot(2,2,4)
plt.title("Cot.")
plt.plot(x, y4)
plt.ylim(-10,10)

plt.show()

#'''

#'''
# Forma 2 : subplots()
figure, ax = plt.subplots(2,2)
ax[0][0].set_title("Sen.")
ax[0][0].plot(x, y1 ) #,'.c')

ax[0][1].set_title("Cos.")
ax[0][1].plot(x, y2)

ax[1][0].set_title("Tan.")
ax[1][0].plot(x, y3)
ax[1][0].set_ylim(-10,10)

ax[1][1].set_title("Cot.")
ax[1][1].plot(x, y4)
ax[1][1].set_ylim(-10,10)

plt.show()
#'''


