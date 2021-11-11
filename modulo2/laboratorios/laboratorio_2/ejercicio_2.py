"""
Ejercicio 2
Del archivo "WEO Data Latinoamerica 2020.csv", realizar un histograma
del PBI del año 2018 de los paises cuyo PBI es mayor a los 150,000 millones de dolares
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

archivo_csv = "CursoTecsup/modulo2/laboratorio_2/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df_1 = df.loc[(df['2018'] > 150)]
df.set_index("Country", inplace=True)
print(df['2018'])
df_1.set_index("Country", inplace=True)
print(df_1['2018'])

def grafico_histograma_1():
    count, bin_edges = np.histogram(df_1['2018'])
    print(bin_edges)
    df_1['2018'].plot(kind='hist', figsize=(8, 5))
    plt.title('Paises por PBI')
    plt.ylabel('Número de Paises')
    plt.xlabel('Billones de $')
    plt.show()


if __name__ == '__main__':
    grafico_histograma_1()
