# Series

import pandas as pd
import numpy as np

# Crear una serie desde un listado
nro_list = [1,2,3,4,5,6] 
serie = pd.Series(nro_list) 
print(serie)

mi_listado = [x for x in range(2,101,2)]
serie = pd.Series(mi_listado)
print(serie)

# Series de arreglo numpy
nro_list = [1,2,3,4,5,6]
np_array =  np.array(nro_list)
serie = pd.Series(np_array) 
print(serie)
np_array =  np.arange(2,101,2)
serie = pd.Series(np_array) 
print(serie)

# Crear una serie desde un diccionario
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
serie = pd.Series(d)
print(serie)

serie = pd.Series(d, index = ['f','b','c','a','e','d'])
print(serie)

print(serie[0:4])

# Aplicando funciones numpy a la serie
print(serie)
print(np.sum(serie))
print(np.min(serie))
print(np.max(serie))
print(np.mean(serie))
print(np.median(serie))
print(np.std(serie))
print(np.var(serie))