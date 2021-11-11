'''
pip install pandas
condas install pandas
Mac: PyCharm -> Preferences... -> Project: ... -> Project Interpreter
Windown: File -> Settings... -> Project: ... -> Project Interpreter

'''

'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 04 : Manipulacion de datos - Leer archivos
Fecha : 10/08/2019
Version : 1
Author :
'''

import pandas as pd

# Leer archivo csv
print("---------------------------------")
archivo_csv = "Tecsup/modulo1/semana4/medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_csv)
print(type(df))
print(df.head())
print(df.keys())

# Leer un campo del archivo csv : Series
print("---------------------------------")
col_pais = df['Pais']
print(type(col_pais))
print(col_pais)

# Leer un campo del archivo csv : DataFrame
print("---------------------------------")
medallas = df[['Pais','Oro','Plata','Bronce']]
print(type(medallas))
print(medallas)

############################################
#  iloc
############################################


# Leer una fila
print("---------------------------------")
print(df.head())

x = 0
dato = df.iloc[x]
print(type(dato))
print(dato)

x = 1
dato = df.iloc[x]
print(type(dato))
print(dato)

# Leer una columna
print("---------------------------------")
print(df.head())

x = 0
dato = df.iloc[:,x]
print(type(dato))
print(dato)

x = 1
dato = df.iloc[:,x]
print(type(dato))
print(dato)

# Leer multiples filas y columnas
print("---------------------------------")
print(df.head())

dato = df.iloc[0:2]
print(type(dato))
print(dato)

dato = df.iloc[:,0:3]
print(type(dato))
print(dato)

dato = df.iloc[0:2,0:3]
print(type(dato))
print(dato)

############################################
#  loc
############################################

#
print("---------------------------------")
print(df.head())

df.set_index("Pais", inplace=True)
print(df.head())

dato = df.loc["Brasil"]
print(type(dato))
print(dato)

#
print("---------------------------------")
print(df.head())

#df.set_index("Pais", inplace=True)
#print(df.head())

dato = df.loc[["Brasil","Perú"]]
print(type(dato))
print(dato)

print("---------------------------------")
print(df.head())

#df.set_index("Pais", inplace=True)
#print(df.head())

dato = df.loc[["Brasil","Perú"],
              ["Oro","Plata","Bronce"]]
print(type(dato))
print(dato)


# Retorna un Dataframe
print("---------------------------------")
print(df.head())

#df.set_index("Pais", inplace=True)
#print(df.head())

dato = df.loc[df["Plata"] == 1 ,
              ["Oro","Plata","Bronce"]]
print(type(dato))
print(dato)

# Retorna un Dataframe
print("---------------------------------")
print(df.head())

#df.set_index("Pais", inplace=True)
#print(df.head())

dato = df.loc[df["Oro"] > 10 ,
              ["Oro","Plata","Bronce"]]
print(type(dato))
print(dato)


# Retorna un Dataframe
print("---------------------------------")
print(df.head())

#df.set_index("Pais", inplace=True)
#print(df.head())

dato = df.loc[(df["Oro"]>10) & (df["Oro"]<30)
                ,["Oro","Plata","Bronce"]]
print(type(dato))
print(dato)
