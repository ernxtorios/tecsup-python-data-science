"""
Dada las edades de los participantes: 22, 18, 35, 23, 90, 110, 42
Calcular la desviación estándar a tráves de una función
nombre : calc_std()
arg : listado de las edades de los perticipantes
salida : imprimir la desviación estándar
"""
import numpy

lista_edades = [22, 18, 35, 23, 90, 110, 42]

def calc_std(lista):
    array_edades = numpy.array(lista)

    return array_edades.std()

print("La desviación estándar de las edades de los participantes es:", round(calc_std(lista_edades), 2))