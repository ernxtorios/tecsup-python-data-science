# Ejercicio : 
# graficar la ecuacion  10 + 4x 
# entre x que varie de 0 a 100

import matplotlib.pyplot as plt 
import numpy as np 
LIM_INF = 0
LIM_SUP = 100
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y = 10 + 4*x
titulo_label ="FunciónLineal"
x_label ="x"
y_label ="F(x)"

plt.plot(x, y)
plt.title(titulo_label)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.grid()
plt.show()