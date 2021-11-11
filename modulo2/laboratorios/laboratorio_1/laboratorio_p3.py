"""
Ejercicio 3 (7 puntos)
Dado el archivo medallero_Panamericanos_Lima2019.csv, calcular para
la variable independiente Oro los siguientes valores
- La cantidad de registros
- El mayor y menor valor
- Los cuartiles Q1, Q2 y Q3
- La media
- La mediana
- La varianza muestral y poblacional
- La desviación estándar muestral y poblacional
"""
import numpy

# Reading files CSV
NOMBRE_ARCHIVO = 'Tecsup/modulo2/laboratorios/laboratorio_1/medallero_Panamericanos_Lima2019.csv'
datos = numpy.genfromtxt(NOMBRE_ARCHIVO, delimiter=',', names=True, dtype=None, encoding="utf-8")

print(datos)

# La cantidad de registros
print("La cantidad de registros", numpy.size(datos["Oro"]))
# El mayor y menor valor
print("El mayor valor", numpy.max(datos["Oro"]), "el menor valor", numpy.min(datos["Oro"]))
# Los cuartiles Q1, Q2 y Q3
print("Q1 =", numpy.quantile(datos['Oro'], q=0.25))
print("Q2 =", numpy.quantile(datos['Oro'], q=0.50))
print("Q3 =", numpy.quantile(datos['Oro'], q=0.75))
# La media
print("La media", numpy.mean(datos["Oro"]))
# La mediana
print("La mediana", numpy.median(datos["Oro"]))
# La varianza muestral y poblacional
print("La varianza muestral", numpy.var(datos["Oro"], ddof=1), "la varianza poblacional", numpy.var(datos["Oro"]))
# La desviación estándar muestral y poblacional
print("La desviación estándar muestral", numpy.std(datos["Oro"], ddof=1), 
    "la desviación estándar poblacional", numpy.std(datos["Oro"]))