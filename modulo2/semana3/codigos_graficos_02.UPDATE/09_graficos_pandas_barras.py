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
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("---------------------------------")
archivo_csv = "Tecsup/modulo2/semana3/codigos_graficos_02.UPDATE/data/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')

df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
anhos = list(map(str, range(2001, 2022)))

print(df["2020"].head())

def grafico_barras_1():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='bar', figsize=(10, 6))
    plt.title('Perú PBI : 2000 - 2021')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.text(7, 250, '2008 Crisis',horizontalalignment='center')  # see note below
    plt.show()

def grafico_barras_2():
    #df.reset_index(inplace=True)
    df_top = df.sort_values(by = '2021',  ascending=True, inplace=True)
    df_top = df['2021'].tail(10)
    print(df_top)
    df_top.plot(kind='barh', figsize=(10, 10), color='steelblue')
    plt.title('Top Country ')
    plt.xlabel('Billones de $')
    # annotate value labels to each country
    
    for index, value in enumerate(df_top):
        print(value)
        print(np.nan)   
        if not np.isnan(value) : 
            label = format(int(value), ',')  # format int with commas
            #label = value
            # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
            plt.annotate(label, xy=(value, index-0.1), color='black')
    
    plt.savefig("barh-01")
    plt.show()


if __name__ == '__main__':
    grafico_barras_2()