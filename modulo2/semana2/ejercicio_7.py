'''
Crear la siguiente serie 
     14, 18, 22, 26, 30, 34, 38
     Calcular , el min, max, var poblacional , var muestral
              std poblacional  y std muestral 
'''
import numpy as np
import pandas as pd

la_serie = pd.Series([14, 18, 22, 26, 30, 34, 38])
print(la_serie)
print("Information in all data")
print("min =",la_serie.min())
print("max =",la_serie.max())
print("var p=",la_serie.var(ddof=0))
print("var m=",la_serie.var(ddof=1))
print("std p=",la_serie.std(ddof=0))
print("std m=",la_serie.std(ddof=1))

