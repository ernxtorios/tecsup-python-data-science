'''
Generar el gráfico 
del seno , coseno
-Desde 0 a 2*pi con incremento
de 0.1
- Colocar leyenda
- Seno --> color rojo
- Coseno --> color azul
- Poner grilla
- Grabar "func_trig" # png
'''
import matplotlib.pyplot as plt
import numpy as np

# Los rangos de las X se definen :
LIM_INF = 0
LIM_SUP = 2*np.pi + 1
RAZON = 0.1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
y1 = np.sin(x)
y2 = np.cos(x)
x_label = "Grados"
y_label = "Funciones Trigonométricas"

def graficos(x):
    plt.plot(x, y1, 'r', label="sin")
    plt.plot(x, y2, 'b', label="cos")
    plt.grid()
    plt.legend()

    plt.savefig("func_trig")

    plt.show()

if __name__ == '__main__':
    graficos(x)
