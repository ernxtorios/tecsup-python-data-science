# Dataframes

import pandas as pd
import numpy as np

listado_docentes = \
           {
            "0001":
                    {"nombre":"Jaime",
                     "apellido":"Gomez"} ,
            "0002":
                    {"nombre":"Eduardo",
                     "apellido":"Velasquez"}}

#print(listado_docentes) 
#listado_docentes["0003"] = "Carmen Pariona" 
print(listado_docentes["0001"])

# Creamos el dataframe desde el diccionario
df = pd.DataFrame(listado_docentes) 
print(df.head())

# Columna del dataframe que se presenta como una seria
print(df[["0001"]])

# Crear columnas
print(df.head())
df['0003']  = df['0002']
print(df.head())
df['0004']  = df['0002'] + df['0003'] 
print(df.head())

# Borrar e insertar columnas
del df['0004']
print("-"*50)
print(df.head())
df.insert(1,"1111",df["0003"])
print("-"*50)
print(df.head())

"""
# EJERCICIO
  Generar un dataframe de
   nombre edad
  Jose    14
  Maria   18
  Pedro   17
1.- Crear la dentro de 10 años
columan "edad_10" , y almacenar la edad de las personas
2.- Insertar entre el nombre y la edad la columna "codigo" e inicializarlo con el numero -1
"""
data = {"nombre":["Jose","Maria","Pedro"],"edad":[14,18,17]}
data_df = pd.DataFrame(data)
data_df["edad_10"] = data_df["edad"]+10
data_df = data_df.assign(tmp = -1)
data_df.insert(1,"codigo",data_df["tmp"])
del data_df["tmp"]
print(data_df.head())
