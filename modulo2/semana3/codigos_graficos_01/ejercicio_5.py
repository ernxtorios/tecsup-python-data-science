# Ejercicio 
# graficar cuatros graficos simultaneamente
#                           2 
#  - 1er cuadrante : ec : 4x    , color azul , el trazado 
#    se debe hacer con circulos
#                           
#  - 2do cuadrante : ec : log(x)    , color verde
#  
#  - 3er cuadrante : ec : sin(x)    , color amarillo
#
#  - 4to cuadrante : ec : 7 + 4x    , color rojo, el trazado con puntos

import matplotlib.pyplot as plt
import numpy as np

# Los rangos de las X se definen :
LIM_INF = -10
LIM_SUP = 10
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)

def graficos(x):
    plt.subplot(2,2,1)
    plt.plot(x, 4*x**2,'.b')
    plt.subplot(2,2,2)
    plt.plot(x, np.log(x), 'g')
    plt.subplot(2,2,3)
    plt.plot(x, np.sin(x), 'y')
    plt.subplot(2,2,4)
    plt.plot(x, 7 + 4*x, '.r')
    plt.show()

if __name__ == '__main__':
    graficos(x)
