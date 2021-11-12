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
archivo_csv = "Tecsup/modulo2/semana3/codigos_graficos_02/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
print(df.head())

print("---------------------------------")
df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
print(df.head())

print("---------------------------------")
anhos = list(map(str, range(2001, 2021)))
#anhos = ["2009", "2010", "2011","2012", "2013","2014", "2015",	"2016", "2017",	"2018","2019","2020"]
print(anhos)


def grafico_area_1():
    df.sort_values(by='2018', ascending=False, axis=0, inplace=True)
    df_top5 = df[anhos].head(5)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    df_top5.plot(kind='area', stacked=False, figsize=(20, 9)) # pass a tuple (x, y) size
    plt.title('Top 5 Paises por PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()

def grafico_area_2():
    df.sort_values(by='2018', ascending=False, axis=0, inplace=True)
    df_top5 = df[anhos].head(5)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    df_top5.plot(kind='area', alpha=0.25, stacked=False, figsize=(20, 9)) # pass a tuple (x, y) size
    plt.title('Top 5 Paises por PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()

def grafico_area_3():
    df.sort_values(by='2018', ascending=False, axis=0, inplace=True)
    df_top5 = df[anhos].head(5)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    ax = df_top5.plot(kind='area', alpha=0.35, stacked=False, figsize=(20, 9)) # pass a tuple (x, y) size
    ax.set_title('Top 5 Paises por PBI')
    ax.set_ylabel('Billones $')
    ax.set_xlabel('Años')
    ax.plot()
    plt.show()


if __name__ == '__main__':
    grafico_area_3()