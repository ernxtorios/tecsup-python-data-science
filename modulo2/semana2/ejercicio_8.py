'''
Ejercicio 01 :
Calcular la mediana, la media , la varianza y desviacion estandar 
de las medalla de plata usando Pandas
'''
import pandas as pd

df = pd.DataFrame(data_dic)
print("median =",df['Plata'].median())
print("mean =",df['Plata'].mean())
print("var =",df['Plata'].var(ddof=1))
print("std =",df['Plata'].std(ddof=1))