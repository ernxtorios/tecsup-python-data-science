"""
Ejercicio 1
Realizar un gráfico de linea de la función trigonométrica del seno y coseno
en 2 gráficos distintos de 0 a 2pi, use el método subplot()
"""

import matplotlib.pyplot as plt
import numpy as np

LIM_INF = 0
LIM_SUP = 2*np.pi + 1
RAZON = 0.1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y1 = np.sin(x)
y2 = np.cos(x)
x_label = "Grados"
y_label = "Funciones Trigonométricas"

def graficos_1(x):
    plt.subplot(2,2,1)
    plt.plot(x, y1, 'r', label="sin")
    plt.grid()
    plt.legend()
    plt.xlabel("Valores de X")
    plt.ylabel("Valores de Y")
    plt.title("Función Seno")
    plt.subplot(2,2,4)
    plt.plot(x, y2, 'b', label="cos")
    plt.grid()
    plt.legend()
    plt.xlabel("Valores de X")
    plt.ylabel("Valores de Y")
    plt.title("Función Coseno")

    plt.show()

if __name__ == '__main__':
    graficos_1(x)