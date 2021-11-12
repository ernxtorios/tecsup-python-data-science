import matplotlib.pyplot as plt 
import numpy as np 
LIM_INF = -104
LIM_SUP = 105
RAZON = 16
x = np.arange(LIM_INF, LIM_SUP, RAZON)

def graficar(x):
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


if __name__ == '__main__':
    
    graficar(x)