"""
Ejercicio 4
Del archivo "WEO Data Latinoamerica 2020.csv", realizar un gráfico de cajas
del PBI de los años 2015 al 2019 de los 3 paises con mayor PBI de latinoamérica
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

archivo_csv = "CursoTecsup/modulo2/laboratorio_2/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.set_index("Country", inplace=True)
datos1 = df.sort_values(by="2015", ascending=False, inplace=True)
datos1 = df.head(3)
print(datos1["2015"])
datos2 = df.sort_values(by="2016", ascending=False, inplace=True)
datos2 = df.head(3)
print(datos2["2016"])
datos3 = df.sort_values(by="2017", ascending=False, inplace=True)
datos3 = df.head(3)
print(datos3["2017"])
datos4 = df.sort_values(by="2018", ascending=False, inplace=True)
datos4 = df.head(3)
print(datos4["2018"])
datos5 = df.sort_values(by="2019", ascending=False, inplace=True)
datos5 = df.head(3)
print(datos5["2019"])

data = [datos1["2015"], datos2["2016"], datos3["2017"], datos4["2018"], datos5["2019"]]
etiqueta = ["2015", "2016", "2017", "2018", "2019"]

plt.boxplot(data, labels=etiqueta)
plt.title("Diagrama de Cajas")
plt.ylabel("Top 3 de paises con mayor PBI de los años 2015 al 2019")
plt.legend()

plt.show()