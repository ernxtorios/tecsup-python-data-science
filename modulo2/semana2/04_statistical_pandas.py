'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Fundamentos de Estadistica
Fecha : 10/07/2020
Version : 1
Author : Jaime Gomez
'''

import numpy as np
import pandas as pd

# -------------------------------------------
#   Pandas : Series
# -------------------------------------------

ds = pd.Series(np.arange(0,16))
#add = pd.Series((1,1,1,1))
#ds = ds.append(add)
print("Sample data:")
print(ds)

# Information in all data
print("Information in all data")
print("min =",ds.min())
print("max =",ds.max())
print("mode =",ds.mode())
print("mean =",ds.mean())
print("var =",ds.var(ddof=0))
print("std =",ds.std(ddof=0))


ds = pd.Series(np.arange(0,4), 
    index={"alumno 1","alumno 2","alumno 3","alumno 4"})

print(ds)


# -------------------------------------------
#   Pandas : Dataframe
# -------------------------------------------

data_dic ={
"Pais":["Estados Unidos","Brasil","México","Canadá","Cuba","Argentina","Colombia","Chile",
"Perú","República Dominicana","Ecuador","Venezuela","Jamaica","Puerto Rico",
"El Salvador","Guatemala","Trinidad y Tobago","Uruguay","Paraguay","Bolivia",
"Granada","Costa Rica","Santa Lucia","Barbados","Islas Vírgenes B",
"Antigua y Barbuda","Honduras","Panamá","Nicaragua","Aruba","Bahamas"],
"Oro":[ 120,55,37,35,33,32,28,13,11,10,10,9,6,5,3,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
"Plata":[88,45,36,64,27,35,23,19,7,13,7,15,6,5,0,9,8,4,3,2,1,0,0,0,0,1,1,0,0,0,0]}

print(len(data_dic["Pais"]))
print(len(data_dic["Oro"]))
print(len(data_dic["Plata"]))

df = pd.DataFrame(data_dic)


print("About sum :")
print("sum =",df['Oro'].sum())
print("sum =",df.Oro.sum())
print("sum =",np.sum(df['Oro']))
print("sum =",np.sum(df.Oro))



print("About min :")
print("min =",df['Oro'].min())
print("min =",df.Oro.min())
print("min =",np.min(df['Oro']))
print("min =",np.min(df.Oro))

print("About max :")
print("max =",df['Oro'].max())
print("max =",df.Oro.max())
print("max =",np.max(df['Oro']))
print("max =",np.max(df.Oro))

print("About median :")
print("median =",df['Oro'].median())
print("median =",df.Oro.median())
print("median =",np.median(df['Oro']))
print("median =",np.median(df.Oro))

print("About mode :")
print("mode =",df['Oro'].mode())
print("mode =",df.Oro.mode())

print("About percentiles :")
tramos = 75 # [25,50,75]
print("percentile =",np.percentile(df['Oro'], q=tramos))
print("percentile =",np.percentile(df.Oro, q=tramos))

print("About quantiles :")
tramos = 0.75 # [0.25,0.50,0.75]
print("quantile =",df['Oro'].quantile(tramos))
print("quantile =",df.Oro.quantile(tramos))
print("quantile =",np.quantile(df['Oro'], q=tramos))
print("quantile =",np.quantile(df.Oro, q=tramos))


print("About variance :")
print("var =",df['Oro'].var())   # Using correction  Bessel  ddof=0
print("var =",df.Oro.var())      # Using correction  Bessel ddof=0
print("var =",np.var(df['Oro'])) # Using correction  Bessel ddof=0
print("var =",np.var(df.Oro))    # Using correction  Bessel ddof=0

print("About std :")
print("std =",df['Oro'].std())   # Using correction  Bessel  ddof=0
print("std =",df.Oro.std())      # Using correction  Bessel ddof=0
print("std =",np.std(df['Oro'])) # Using correction  Bessel ddof=0
print("std =",np.std(df.Oro))    # Using correction  Bessel ddof=0


# Read file
FILENAME = "Tecsup/modulo2/semana2/medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(FILENAME)

# Print the 5 first element
print(df.head())
