"""
Ejercicio 3
Del archivo WEO Data Latinoamerica 2020.csv, realizar un gráfico de pie
del PBI del 2019 de los paises: Brazil, Mexico, Argentina, Colombia, Chile y
Perú
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

archivo_csv = "CursoTecsup/modulo2/laboratorio_2/WEO_Data_Latinoamerica_2020.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.set_index("Country", inplace=True)
datos = df.loc[["Brazil", "Mexico","Argentina", "Colombia", "Chile", "Peru"]]
print(datos["2019"])

plt.pie(datos["2019"], labels=datos["2019"].index, autopct='%1.1f%%')
plt.title("PBI del 2019 de los paises: Brasil, Mexico, Argentina, Colombia, Chile y Perú")
plt.legend()

plt.show()