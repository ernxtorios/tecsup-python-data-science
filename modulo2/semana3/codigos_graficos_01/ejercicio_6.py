'''
Graficar la función 1/(1+np.exp(-x))
La gráfica debe ser de color rojo y debe tener
rango de 1 a 10 incrementado de 1 en 1 
'''
import matplotlib.pyplot as plt
import numpy as np

# Los rangos de las X se definen :
LIM_INF = 1
LIM_SUP = 11
RAZON = 1
x = np.arange(LIM_INF, LIM_SUP, RAZON)

def grafico(x):
    plt.plot(x, 1/(1 + np.exp(-x)), 'r')
    plt.show()

if __name__ == '__main__':
    grafico(x)
