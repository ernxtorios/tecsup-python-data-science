"""
Ejercicio: Generar el archivo "numeros.txt" con el contenido
123456789
12345678
1234567
123456
12345
1234
"""
print("---------------------------------")
los_numeros = "123456789"
with open("Tecsup/modulo1/semana4/numeros.txt","w") as archivo_numeros:
    for x in range(6): 
        archivo_numeros.write(los_numeros[:len(los_numeros) - x] + "\n")
