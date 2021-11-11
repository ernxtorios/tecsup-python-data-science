'''
Ejercicio: Validar si un numero par
o impar y mostrar un mensaje en ambos
casos
'''
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

"""
Ejercicio: Del año 1990 al año 2019,
imprimir la decada del año
- "Decada de los 90"
- "Decada de los 2000"
- "Decada de los 2010"
Para un año que no esta comprendido en el rango
anterior imprimir:
- "Decada desconocida"
1990 al año 2019
"""
anio = 1992
if 1990 <= anio <= 1999:
    print(f"{anio} es de la década de los 90")
elif 2000 <= anio <= 2009:
    print(f"{anio} es de la década de los 2000")
elif 2010 <= anio <= 2019:
    print(f"{anio} es de la década de los 2010")
else:
    print(f"{anio} es de la década desconocida")

"""
Ejercicio
Dado una diccionario de puntajes de jugadores
jugadores_puntos = {"Juan":50 , "Maria":30,
"Feliz":10 ,"Jaime":20}
Ingresar un nuevo jugador por teclado
Si el jugador existe, incrementar en 10 %
su puntaje, caso contrario agregarlo al diccionario
y asignarlo 10 puntos
"""
jugadores_puntos = {"Juan": 50, "Maria": 30, "Feliz": 10, "Jaime": 20}
nuevo_jugador = input("Ingrese el nombre del nuevo jugador: ")
if nuevo_jugador in jugadores_puntos.keys():
    jugadores_puntos[nuevo_jugador] *= 1.1
else:
    jugadores_puntos[nuevo_jugador]  = 10
print(jugadores_puntos)

print("------------------------------------------")
numeros = [10, 20, 30, 40, 50]
for valor in numeros :
    print(valor)

# ¿Podrías imprimir solo los numero múltiplos de 4?
print("Múltiplos de 4:", end=" ")
for valor in numeros:
    if valor % 4 == 0:
        print(f"{valor}", end=", ")