# Ejercicio 
# crear la funcion imprimir_nros
# que reciba de parametro un entero
# e imprima en consola los numeros de 0 
# al valor del parametro
# imprimir_nros(5)

def imprimir_nros(n):
    [print(x, end=" ") for x in range(n + 1)]

imprimir_nros(5)

# Ejercicio 2
# crear la funcion imprimir_nros_ord
# que reciba dos parametro
#  - 1er parametro : Un entero
#  - 2do parametro : Un boolean
# e imprima en consola de la siguiente 
# manera 
# 
#  Si el 2do. parametro es verdadero 
#     Imprimir de 0 al primer parametro  (inc)
# 
#  Si el 2do. parametro es falso 
#     Imprimir desde primer parametro al 0  (dec)

print()
def imprimir_nros_ord(nro, flag):
    if flag:
        [print(x, end=" ") for x in range(nro + 1)]
    else:
        [print(x - 1, end=" ") for x in range(nro + 1, 0, -1)]

imprimir_nros_ord(5,True)
print()
imprimir_nros_ord(5,False)

# Parámetro opcional
def imprimir_nros_ord_1(nro, flag=True):
    if flag:
        [print(x, end=" ") for x in range(nro + 1)]
    else:
        [print(x - 1, end=" ") for x in range(nro + 1, 0, -1)]

imprimir_nros_ord_1(5)
print()
imprimir_nros_ord_1(5,False)


# Ejercicio 3
#  Crear la funcion saludo() que reciba como parametro
#  el nombre de un perosona e imprima
#             "Welcome to Tecsup , Jaime"
# saludo("Jaime") ==>  "Welcome to Tecsup , Jaime"
# saludo()        ==>  "Welcome to Tecsup , Estudiante"
def saludo(nombre="Estudiante"):
    print("Welcome to Tecsup, {}".format(nombre))

saludo("Jaime")
saludo()

#######################################################
# 3.- Funcion sin entrada de datos y que retornen datos
#######################################################
def acerca():
    msg = "Curso de Ciencia de datos"
    print(msg)
    return msg  # retorna un valor 
 #######################################################
# 2.- Funcion con entrada de datos y que retornen datos
#######################################################
def ope_suma(a, b):
    sum = a + b
    print(sum) 
    return sum

acerca()

print("-"*60)
acerca()  # no recibe el valor de la funcion
msg_acerca = acerca()  # Recibe el valor en una variable
print(msg_acerca)

print("-"*60)
res_suma = ope_suma(12,24)
print(res_suma)

# Ejercicio 4
#      Crear la funcion media, que obtenga la 
#      media de un listado de datos que se ingresan
#      como parametros y me devuvela la media
def media(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)

listado = [1,2,3] 
print(media(listado))

print(round(12.456, 2))

# Ejercicio 5
#
#      Crear la funcion var, que obtenga la 
#      varianza de un listado de datos que se ingresa
#      como parametros y me devuvela la varianza
#                              2
#      nro   media            r
#       1   -  2   =  -1   => (-1)(-1) = 1 
#       2   -  2   =   0   => (0)(0)   = 0
#       3   -  2   =   1   => (1)(1)   = 1 
#                                       ----
#                                        2  
#      El 2 se divide entre el numero de datos 
#      y el resultado es la varianza   2/3
#
def var(lista_numeros, numero_decimales=2):
    suma = 0
    for n in lista_numeros:
        suma += (n - media(lista_numeros))**2
    
    return round(suma/len(lista_numeros), numero_decimales)

listado = [1,2,3] 
varianza = var(listado, 4)
print(varianza)

import tecsup.estadistica as est

listado = [1, 2, 3, 4] 
md = est.media(listado)
print("La media es", md)
print("La suma del listado de números es", est.sumar_lista(listado))