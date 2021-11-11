# 0 1 2
nombres = ["Jose","Juan","Pedro"]

print(nombres[2].lower()) # pedro

# "Jose" --> "JOSE"
indice = nombres.index("Jose")
print(nombres[indice], "-->", nombres[indice].upper())

# "Juan" --> "jUAN"
indice = nombres.index("Juan")
print(nombres[indice], "-->", nombres[indice].swapcase())

# "Pedro" --> "Pdo"
indice = nombres.index("Pedro")
print(nombres[indice], "-->", nombres[indice][0::2])

# Ejercicio
# Crear una tupla de planetas : Mercurio Venus Tierra Marte Jupyter
# e imprimir los primeros 4 caracteres del nombre de
# cada planeta
planetas = ("Mercurio", "Venus", "Tierra", "Marte", "Jupiter")

for p in planetas:
    print(p[:4])

# Ecuación cuadrática
import math

a, b, c = 4, -16, 2

x_1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
x_2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a

# Muestra las soluciones con dos decimales
print(f"Las raices de la ecuación 4*x^2 - 16*x + 2 son {x_1:.2f} y {x_2:.2f}")

"""
Ejercicio con operador "in" y "not in"
Los planetas: Mercurio Venus Tierra Marte Jupyter
La Tierra es un planeta
La Luna es un planeta
Titan no es un planeta
"""
planetas = ("Mercurio", "Venus", "Tierra", "Marte", "Jupiter")

print("La tierra es un planeta", "Tierra" in planetas)
print("La luna es un planeta", "Luna" in planetas)
print("Titan no es un planeta", "Titan" not in planetas)

# Ejercicio :
# Definir una lista con : "Juan" , "Pedro" ,"Marcos"
# Reemplazar "Juan" por "Juana"
# Reemplazar "Pedro" por "Patricia"
# Eliminar a "Marcos" del listado
los_nombres = ["Juan", "Pedro" ,"Marcos"]
print(los_nombres)
el_indice = los_nombres.index("Juan")
los_nombres[el_indice] = "Juana"
el_indice = los_nombres.index("Pedro")
los_nombres[el_indice] = "Patricia"
el_indice = los_nombres.index("Marcos")
del(los_nombres[el_indice])
print(los_nombres)

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

print("--------------------------------------")
dato_ingresado = "soccer"
sports = ["Soccer","Tennis","Baseball","Squash"]
#¿ Como hacer para encontrar la posicion del soccer
# independiente de si esta en mayuscula o minuscula
sports_lower = list()
for s in sports:
    sports_lower.append(s.lower())
print(sports)
print(sports_lower)
print(f"El índice de {dato_ingresado.lower()} en la lista de deportes es: ", sports_lower.index(dato_ingresado.lower()))

# Datos de una empresa de Software
mujeres = {"Marisol","Ana","Maria","Carmen"}
hombres = {"Pedro","Jaime","Alberto","Juan"}
desarrolladores = {"Marisol","Jaime","Maria","Juan"}
practicantes = {"Pedro","Alberto","Ana"}
# Que desarrolladores son mujeres?
print("Mujeres desarrolladoras: ", end="")
for d in mujeres:
    print(d, end=" ")
print("")
# Quienes son los practicantes que son varones?
print("Practicantes varones: ", end="")
for v in hombres & practicantes:
    print(v, end=" ")
print("")
# Cuantos trabajadores hay en total en la empresa?
print("Total de trabajadores: ", len(hombres | mujeres))

# Forma de mostrar los elementos de una lista
letras = ['á', 'é', 'í', 'ó', 'ú', 'ñ']
[print(x, end=" ") for x in letras]

