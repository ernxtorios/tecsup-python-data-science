"""
Práctica de Laboratorio 1
Ernesto Segundo Ríos Sandoval
"""

"""
Ejercicio 1 
Crear una lista con los meses del ano a partir de julio, realizar las siguientes
acciones:
• Eliminar el contenido del mes de Noviembre
• Acceder al mes de Agosto con el indice negativo
• Acceder al mes de Diciembre con el indice positivo
"""
print()
print("-"*50, "Ejercicio 1", "-"*50)
# Lista de los meses del segundo semestre del año
semestre_ii = ["Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]
# Mostrar la lista original
print("La lista de meses del segundo semestre: ", semestre_ii)
# Eliminar el mes "Noviembre": opción 1: remove(), opción 2: del()
print("Hacer: Eliminar el contenido del mes de Noviembre")
semestre_ii.remove("Noviembre")
# También:
# del(semestre_ii[4])
# Mostrar la lista después de la eliminación del mes "Noviembre"
print("La lista de meses del segundo semestre después de la eliminación: ", semestre_ii)
print("Hacer: Acceder al mes de Agosto con el indice negativo")
# Después de la eliminación del mes "Noviembre" el índice del mes "Agosto" es -4
print("semestre_ii[-4]: ", semestre_ii[-4])
print("Hacer: Acceder al mes de Diciembre con el indice positivo")
# Después de la eliminación del mes "Noviembre" el índice del mes "Diciembre" es 4, también el tamaño de la lista menos 1
print("semestre_ii[4]:", semestre_ii[4])
print("semestre_ii[len(semestre_ii) - 1]:", semestre_ii[len(semestre_ii) - 1])
# También se puede obtener el índice positivo del mes "Diciembre" usando index, puesto que conocemos el nombre del elemento
print("semestre_ii[semestre_ii.index(""Diciembre"")]:", semestre_ii[semestre_ii.index("Diciembre")])

"""
Ejercicio 2
Dado el PBI del Peru, desde el 2010 a 2019 : ”148,014 168,772 189,024 197,866
203,021 192,391 195,432 214,128 225,203 232,080” obtener el promedio del PBI
agrupado por cada 2 anos, desde el año 2010
"""
print()
print("-"*50, "Ejercicio 2", "-"*50)
# Diccionario que almacena los valores del PBI por cada año dado
pbi_peru = {"2010": 148014, 
            "2011": 168772, 
            "2012": 189024, 
            "2013": 197866, 
            "2014": 203021, 
            "2015": 192391, 
            "2016": 195432, 
            "2017": 214128, 
            "2018": 225203, 
            "2019": 232080}

"""
Explicación: Convertimos a lista los valores del diccionario, cada dos años, desde el valor inicial.
Obtenemos la suma de los valores de esos dos años y lo dividimos entre 2 para obtener el promedio.
"""
print("Promedio PBI Perú 2010 - 2011 ===> ", sum(list(pbi_peru.values())[:2])/2)
print("Promedio PBI Perú 2012 - 2013 ===> ", sum(list(pbi_peru.values())[2:4])/2)
print("Promedio PBI Perú 2014 - 2015 ===> ", sum(list(pbi_peru.values())[4:6])/2)
print("Promedio PBI Perú 2016 - 2017 ===> ", sum(list(pbi_peru.values())[6:8])/2)
print("Promedio PBI Perú 2018 - 2019 ===> ", sum(list(pbi_peru.values())[8:])/2)

"""
Ejercicio 3
En el siguiente párrafo, contar las cantidades que se repiten las palabras ”de”
y ”la”, almacenarlos en una lista. ”Los mentideros de los científicos de la
computación hierven estos días a fuego vivo en la convicción de que Google
está preparando un anuncio sensacional, uno de esos trabajos que aparecerán
en Navidad en los top ten de la ciencia del año. El Goliat de Silicon Valley cree
haber demostrado la “supremacıa cuantica”, la demostracion empírica de que un
ordenador basado en la enigmática física que impera a escalas atómicas puede
ejecutar operaciones que no están al alcance de los computadores convencionales
más formidables que existen. De confirmarse, sería un avance bien notable”
"""
print()
print("-"*50, "Ejercicio 3", "-"*50)
# Definimos el párrafo
parrafo = """Los mentideros de los científicos de la 
    computación hierven estos días a fuego vivo en la convicción de que Google
    está preparando un anuncio sensacional, uno de esos trabajos que aparecerán
    en Navidad en los top ten de la ciencia del año. El Goliat de Silicon Valley cree
    haber demostrado la “supremacıa cuantica”, la demostracion empírica de que un
    ordenador basado en la enigmática física que impera a escalas atómicas puede
    ejecutar operaciones que no están al alcance de los computadores convencionales
    más formidables que existen. De confirmarse, sería un avance bien notable"""

# Utilizamos count para obtener las ocurrencias de las palabras dadas
print("Ocurrencias de la palabra 'de' en el párrafo: ", parrafo.count(" de "))
print("Ocurrencias de la palabra 'la' en el párrafo: ", parrafo.count(" la "))

# Definimos la lista con los datos solicitados
cantidades = [parrafo.count(" de "), parrafo.count(" la ")]

# Mostramos la lista solicitada
print("Lista de cantidades de las ocurrencias de las palabras 'de' y 'la' en el párrafo:", cantidades)

"""
Ejercicio 4
Dado una lista con los elementos [13,4,22,18,17,2,14,20], crear otro arreglo de
modo que los 4 primeros elementos sean los 4 menores números ordenados
en forma ascendente y los siguientes 4 siguientes números sean los 4 mayores
números ordenados de forma descendente.
"""
print()
print("-"*50, "Ejercicio 4", "-"*50)
# La lista de números dados
los_numeros = [13, 4, 22, 18, 17, 2, 14, 20]
# Mostramos la lista inicial
print("La lista inicial de números:", los_numeros)
# Ordenamos la lista de forma ascendente. Esto modifica la lista inicial
los_numeros.sort()
# Mostramos la lista después del ordenamiento ascendente
print("La lista de números después del ordenamiento ascendente:", los_numeros)
# Definimos una lista que almacene los cuatro primeros elementos de la lista ordenada ascendentemente
los_cuatro_primeros = los_numeros[:4]
# Definimos una lista que almacene los cuatro últimos elementos de la lista ordenada ascendentemente
los_cuatro_ultimos = los_numeros[4:]
# Mostramos la lista de los cuatro primeros elementos de la lista ordenada ascendentemente
print("La lista de los cuatro primeros elementos de la lista ordenada ascendentemente:", los_cuatro_primeros)
# Ordenamos descendentemente la lista de los cuatro últimos elementos de la lista ascendentemente
los_cuatro_ultimos.sort(reverse=True)
# Mostramos la lista de los cuatro últimos elementos de la lista ordenados descendentemente
print("La lista de los cuatro últimos elementos de la lista ordenados descendentemente:", los_cuatro_ultimos)

"""
Ejercicio 5
Dado 2 conjuntos de nombres ”Jose”, ”Maria”, ”Juan” y ”Eduardo”, ”Jose”,
”Pedro”, indicar la cantidad de nombres únicos que existen
"""
print()
print("-"*50, "Ejercicio 5", "-"*50)
# El primer conjunto de nombres
conjunto_A = {"José", "María", "Juan"}
# El segundo conjunto de nombres
conjunto_B = {"Eduardo", "José", "Pedro"}

# Para obtener la cantidad de nombres únicos que existen definimos la intersección de los conjuntos y mostramos su tamaño con len()
print("La cantidad de nombres únicos que existen es:", len(conjunto_A & conjunto_B))

"""
Ejercicio: 
Dada la cadena de entrada
entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
Generar la salida
salida = "Juan:Galvez:Maribel:Alegria"
Se recomienda usar split()
"""
entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
la_lista_de_nombres = entrada.split(":")
print(la_lista_de_nombres)
del(la_lista_de_nombres[la_lista_de_nombres.index("Marin")])
del(la_lista_de_nombres[la_lista_de_nombres.index("Angulo")])
print(la_lista_de_nombres)
salida = ":".join(la_lista_de_nombres)
print(salida)