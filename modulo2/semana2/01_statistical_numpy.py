'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 02 : Fundamentos de Estadistica
Fecha : 10/07/2020
Version : 1
Author : Jaime Gomez
'''

import numpy as np

COL = 0
ROW = 1 

# ---------------------------------
# Methods of Ndarray
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# ---------------------------------

# Generate data
a_matrix = np.arange(0,16).reshape(4,4)
print("Sample data:")
print(a_matrix)

# Information in all data
print("Information in all data")
print("sum =",a_matrix.sum())
print("min =",a_matrix.min())
print("max =",a_matrix.max())
print("mean =",a_matrix.mean())
print("std =",a_matrix.std())
print("var =",a_matrix.var())

# Information by column
print("Information by column")
print("sum =",a_matrix.sum(COL))
print("min =",a_matrix.min(COL))
print("max =",a_matrix.max(COL))
print("mean =",a_matrix.mean(COL))
print("std =",a_matrix.std(COL))
print("var =",a_matrix.var(COL))

# Information by row
print("Information by row")
print("sum =",a_matrix.sum(ROW))
print("min =",a_matrix.min(ROW))
print("max =",a_matrix.max(ROW))
print("mean =",a_matrix.mean(ROW))
print("std =",a_matrix.std(ROW))
print("var =",a_matrix.var(ROW))

# ---------------------------------
# Function of Numpy
# https://numpy.org/doc/stable/reference/routines.statistics.html
# ---------------------------------

# Generate data
a_matrix = np.arange(0,16).reshape(4,4)
print("Sample data:")
print(a_matrix)

# Information in all data
print("Information in all data")
print("sum =",np.sum(a_matrix))
print("min =",np.amin(a_matrix))
print("max =",np.amax(a_matrix))
print("mean =",np.mean(a_matrix))
print("median =",np.median(a_matrix))
print("average =",np.average(a_matrix))
print("variance =",np.var(a_matrix))
print("std =",np.std(a_matrix))


# Information by column
print("Information by column")
print("sum =",np.sum(a_matrix,axis=COL))
print("min =",np.amin(a_matrix,axis=COL))
print("max =",np.amax(a_matrix,axis=COL))
print("mean =",np.mean(a_matrix,axis=COL))
print("median =",np.median(a_matrix,axis=COL))
print("average =",np.average(a_matrix,axis=COL))
print("variance =",np.var(a_matrix,axis=COL))
print("std =",np.std(a_matrix,axis=COL))

# Information by row
print("Information by row")
print("sum =",np.sum(a_matrix,axis=ROW))
print("min =",np.amin(a_matrix,axis=ROW))
print("max =",np.amax(a_matrix,axis=ROW))
print("mean =",np.mean(a_matrix,axis=ROW))
print("median =",np.median(a_matrix,axis=ROW))
print("std =",np.std(a_matrix,axis=ROW))
print("average =",np.average(a_matrix,axis=ROW))
print("variance =",np.var(a_matrix,axis=ROW))

# Information of percentile
print("Information of percentile")
PERCENTAGE = 75  # Percentage, 50 is the mediane
print("percentile all table =",np.percentile(a_matrix,q=PERCENTAGE))
print("percentile by columm =",np.percentile(a_matrix,q=PERCENTAGE,axis=COL))
print("percentile by row =",np.percentile(a_matrix,q=PERCENTAGE,axis=ROW))


# Information of quantiles
print("Information of quantiles")
QUANTILE = 0.50  # 
print("quantile all table =",np.quantile(a_matrix,q=QUANTILE))
print("quantile by columm =",np.quantile(a_matrix,q=QUANTILE,axis=COL))
print("quantile by row =",np.quantile(a_matrix,q=QUANTILE,axis=ROW))


# Calculate the variance
var = (np.sum((a_matrix - np.mean(a_matrix))**2))/a_matrix.size
print("var calculate =",var)