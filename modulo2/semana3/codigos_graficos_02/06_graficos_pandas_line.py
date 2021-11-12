'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 15/07/2020
Version : 1
Author : Jaime Gomez
Link : 

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


""" # Country	
ppp_2020 = {
"Anhos"  :[    2009, 2010, 2011,	2012,	2013,	2014,	2015,	2016,	2017,	2018,	2019],
"Argentina":[  678.224,  755.600,  817.698,	 824.828,  859.487,	 853.398,  885.833,  876.387,  916.719,  915.749,  911.562],	
"Bolivia"  :[   49.872,   52.535,	56.424,	  60.452,   65.693,	  70.562,   74.760,	  78.754,   83.604,	  89.258,	93.357],
"Brazil"   :[ 2575.700,	2802.320, 2974.902,	3090.412, 3239.228,	3315.854, 3231.412,	3157.627, 3259.359,	3382.591, 3480.546],	
"Chile"    :[  302.042,	 323.393,  350.368,	 376.074,  398.163,	 412.747,  426.718,	 438.525,  452.030,	 481.282,  495.176],	
"Colombia" :[  461.592,	 487.959,  532.763,	 564.226,  603.602,	 642.432,  668.307,	 689.322,  711.851,	 747.536,  785.836],	
"Ecuador"  :[  130.635,	 136.816,  150.664,	 162.217,  173.228,	 183.119,  185.209,	 184.832,  192.772,	 200.015,  203.611],	
"Mexico"   :[ 1698.329,	1806.054, 1911.319,	2018.932, 2082.170,	2180.178, 2275.306,	2365.776, 2461.382,	2575.206, 2616.289],	
"Panama"   :[   52.095,	  55.773,	63.380,	  70.913,   77.138,	  82.546,   88.187,	  93.514,  100.609,	 106.866,  111.998],	
"Peru"     :[  259.632,	 284.854,  309.567,	 334.280,  360.000,  375.440,  391.767,  411.855,  429.997,  457.956,  476.014],	
"Uruguay"  :[	51.773,	  56.464,   60.619,	  63.967,	68.108,	  71.615,	72.629,	  74.621,	77.997,	  81.191,	82.791],	
"Venezuela":[  472.050,	 470.441,  500.326,	 538.611,  555.422,	 543.671,  515.155,	 431.796,  370.985,  305.457,  202.009]	
}

df = pd.DataFrame(ppp_2020)

plt.plot(anhos, df)
plt.show()

print(df.head())
 """


print("---------------------------------")
archivo_csv = "Tecsup/modulo2/semana3/codigos_graficos_02/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
print(df.head())

print("---------------------------------")
df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
print(df.head())

print("---------------------------------")
anhos = list(map(str, range(2001, 2021))) # [str(year) for year in range(2001,2021)]
#anhos = ["2009", "2010", "2011","2012", "2013","2014", "2015",	"2016", "2017",	"2018","2019","2020"]
print(anhos)

def grafico_linea_0():
    '''
    Graficar la información de Argentina
    del año 2010-2021
    '''
    anhos2 = list(map(str, range(2010, 2022)))
    arg = df.loc["Argentina", anhos2]
    print(type(arg))
    arg.plot()
    plt.show()

def grafico_linea_1():
    print(df.head())
    peru = df.loc["Peru", anhos]
    print(type(peru))
    print(peru.head())
    peru.plot()
    plt.grid()
    plt.show()
    #plt.show(block=True)
    plt.interactive(False)

def grafico_linea_2():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='line')
    plt.title('Perú PBI')
    plt.ylabel('Miles de millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_3():
    peru = df.loc['Peru', anhos]
    peru.plot(kind='line')
    plt.title('Perú PBI')
    plt.ylabel('Miles de millones de $')
    plt.xlabel('Años')
    plt.text(7, 250, '2008 Crisis') # see note below
    plt.text(19, 476, 'Estamos aca') # see note below
    plt.show()

def grafico_linea_4():
    paises = df.loc[['Peru','Chile','Colombia'], anhos]
    print(paises.head())
    paises.plot(kind='line')
    plt.show()

def grafico_linea_5():
    paises = df.loc[['Peru','Chile','Colombia'], anhos]
    paises = paises.transpose()
    print(paises.head())
    paises.plot(kind='line')
    plt.title('Perú - Chle - Colombia ')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_6():
    df.sort_values(by='2018', ascending=False, axis=0, inplace=True)
    df_top5 = df[anhos].head(5)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
    plt.title('Top 5 Paises por PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_7():
    '''
    Graficar la información de Brasil
    del año 2000-2021
    '''
    anhos2 = list(map(str, range(2000, 2022)))
    arg = df.loc["Brazil", anhos2]
    print(type(arg))
    arg.plot()
    plt.show()

def grafico_linea_8():
    '''
    Graficar el PBI PPA  de Brazil, Mexico y Argentina
    entre los años 2014 al 2021
    '''    
    paises = df.loc[['Brazil','Mexico','Argentina'], list(map(str, range(2014, 2022)))]
    paises = paises.transpose()
    print(paises.head())
    paises.plot(kind='line')
    plt.title('Brasil - México - Argentina')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico_linea_9():
    '''
    Graficar el PBI PPA de los 3 paises con menores valores
    entre los años 2014 al 2021, tomar de referencia el año 2019
    '''
    df.sort_values(by='2019', ascending=True, axis=0, inplace=True)
    df_top5 = df[anhos].head(3)
    df_top5 = df_top5.transpose()
    print(df_top5.head())
    df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
    plt.title('3 paises con menor PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()


if __name__ == '__main__':
    grafico_linea_9()


