'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 07/09/2019
Version : 1
Author : Jaime Gomez
'''
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("---------------------------------")
archivo_csv = "Tecsup/modulo2/semana3/codigos_graficos_02.UPDATE/data/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')

def grafico_histograma_1():
    #
    count, bin_edges = np.histogram(df['2018'])
    print(bin_edges)

    # sturges
    df['2018'].plot(kind='hist', figsize=(8, 5)) # pass a tuple (x, y) size
    plt.title('Paises por PBI')
    plt.ylabel('Número de Paises')
    plt.xlabel('Billones de $')
    plt.savefig("hist-01")
    plt.show()


if __name__ == '__main__':
    grafico_histograma_1()