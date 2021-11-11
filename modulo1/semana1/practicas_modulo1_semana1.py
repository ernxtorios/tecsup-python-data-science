t = type(10)
print(t)

a, b = 2, 3
print(a, b)

print("Ernesto Segundo")

msg = "Mi nuevo mensaje"
print(msg[::3])

nombres = ["maria","ROCIO","Marta" , "veronica"]

print(nombres[:3:2])

print(nombres[::2])

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Neptuno", "Urano"]

print("¿La tierra es un planeta?", "Tierra" in planetas)
print("¿La luna es un planeta?", "Luna" in planetas)
print("¿Titán no es un planeta?", "Titan" not in planetas)

print("#"*50)
print("Hola Mundo")
print("#"*50)

nombre = "Ernesto"
apellido = "Ríos"
print(f"El nombre es {nombre} y el apellido es {apellido}")

var_a = 4
var_b = "hola"
print("la var_a es " + str(var_a) + " la var_b es " + var_b)
print("la var_a es", var_a, "la var_b es", var_b)
print("la var_a es {} la var_b es {}".format(var_a, var_b))
print(f"la var_a es {var_a} la var_b es {var_b}")

vocales = list("aeiou")
print(vocales)

caballeros = ["Juan", "Pedro", "Marcos"]
print(caballeros)
caballeros[0] = "Juana"
caballeros[1] = "Patricia"
print(caballeros)
# Elimina el último
caballeros.pop()
#del(caballeros[2])
print(caballeros)

msg = "Panam Sports - Lima Peru"
list_palabras =  msg.split()
print(list_palabras)

# convertir la primera palabra a minusculas
list_palabras[0] = list_palabras[0].lower()
print(list_palabras)

print(msg[0].lower()+msg[1:])

# Unir los elementos de una lista y volverlo a una cadena
rec_msg = " ".join(list_palabras)
print(rec_msg)

# convertir todas las palabras a minusculas

# Encontrar cuantas veces se repite la palabra
# "en" 
frase = "Es un dia largo En un parque EN verano"
print("En la frase:", frase)
frase = frase.lower()
print("La palabra en se repite:",frase.count("en"),"veces")

frase = "Es un dia largo En un parque EN verano"
nueva_frase = frase.lower()
print(nueva_frase.count("en"))

"""
Ejercicio: 
entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
salida = "Juan:Galvez:Maribel:Alegria"
"""
entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
lista = entrada.split(":")
lista.pop(-1)
lista.pop(-4)
print(lista)
print(":".join(lista))

entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
lista_nombres = entrada.split(":")
print(lista_nombres)
del lista_nombres[::-3]
print(lista_nombres)
salida = ":".join(lista_nombres)
print(salida)

entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
salida= entrada.split(":")
del(salida[5])
del(salida[2])
print(salida)
rec_salida = ":".join(salida)
print(rec_salida)

entrada = "Juan:Galvez:Marin:Maribel:Alegria:Angulo"
print(entrada)
entrada = entrada.split(":")
del(entrada[2])
del(entrada[-1])
salida = ":".join(entrada)
print(salida)

print("-"*50)
ratings = (10,12,14,20,11,9,15,22,33,17)
orden_rating = sorted(ratings)
print(type(orden_rating))

print("--------------------------------------")
dato_ingresado = "soccer"
sports = ["Soccer","Tennis","Baseball","Squash"]
#¿ Como hacer para encontrar la posicion del soccer
# independiente de si esta en mayuscula o minuscula

for s in sports:
    print(f"¿{dato_ingresado} en lista de deportes?", dato_ingresado in s.lower())


print("-"*50)
ratings = [10,12,14,20,11,9,15,22,33,17]
for valor in ratings:
    print(valor)
# Ejercicio 
#  Imprimir de mayor a menor y viceversa
ratings.sort()
print("Menor a mayor")
for valor in ratings:
    print(valor)
print("Mayor a menor")
ratings.sort(reverse=True)
for valor in ratings:
    print(valor)

print("-"*50)
ratings = [10,12,14,20,11,9,15,22,33,17]
menor_mayor=sorted(ratings)
for valor in menor_mayor:
    print(valor)

# Referencia una lista a traves de otra variable
print("-"*50)
datos = [10,12,14,20,11,9,15,22,33,17]
dato_ref = datos
print(datos)
dato_ref[-1] = 1
print(datos)

# copy
print("-"*50)
datos = [10,12,14,20,11,9,15,22,33,17]
datos_clone = datos.copy()
print("Antes :",datos)
datos_clone[-1] = 1
print("Desp  :",datos)
print("Desp  :",datos_clone)

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



"""
Dada las expresiones
es_lunes =
es_de_noche =
Deseo saber esta condición : ¿Es lunes en la noches?
"""
print("")
es_lunes = True
es_de_noche = True
print("¿Es lunes en la noche?", es_lunes & es_de_noche)

x = int(input("Evaluamos f(x) y g(x) para x = "))

f_x = 4*x**2 + 5*x - 1 + x**(1/2)
g_x = 2*x**2 + 10*x - 1 + x**(1/3)

print("¿f(x) > g(x)?", f_x > g_x)

""" Ejercicio
str_historia = "En un lugar de la mancha"
Obtener el primer caracter
Obtener el último caracter
Obtener la longitud de la cadena """

str_historia = "En un lugar de la mancha"
print(f"El primer caracter: {str_historia[0]}")
print(f"El último caracter: {str_historia[len(str_historia) - 1]}")
print(f"La longitud de la cadena: {len(str_historia)}")