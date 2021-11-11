import calendar

year = 2021
month = 9
print(calendar.month(year, month))

real = 1.1 + 2.2
print(f'{real:.2f}')

texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"
print(texto)

texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor"
print(texto)

# 1
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)
texto = texto.lower()
texto = set(texto.split())
print("Numero de palabras en el texto anterior es:", len(texto))

# 2
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)
texto = texto.lower()
text_to_list = texto.split()
list_to_set = set(text_to_list)
print(len(list_to_set))

# 3
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)
print(len((set(texto.lower().split()))))


# Imprimir las palabras únicas en minúsculas por línea
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
texto = texto.lower()
text_to_list = texto.split()
list_to_set = set(text_to_list)
print(len(list_to_set))
for palabras in list_to_set:
    print(palabras)

texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)

texto = texto.lower()
texto = set(texto.split())
for valor in texto:
    print(valor, " --> # de veces")

# Calcular cuántas veces se usan las palabras y cuáles son
# Esto es en una lista
nombres = ["Jaime","Jose","Jaime"]
print(">>>>",nombres.count("Jaime"))

texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)

for palabra in set(texto.split()):
    print(palabra.lower(),"",texto.lower().split().count(palabra.lower()))

texto = texto.lower()
list_txt = texto.split()
set_txt = set(list_txt)
for palabra in set_txt:
    print(palabra, " --> ",list_txt.count(palabra))

#
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)
texto_init = texto
for palabra in set(texto.split()):
    print(palabra.lower(),"",texto.lower().split().count(palabra.lower()))


# 4.- Almacenar la información en un diccionario
#
texto = "En un lugar de la Mancha, de cuyo nombre no quiero"\
        "acordarme, no ha mucho tiempo que vivia un hidalgo "\
        "de los de lanza en astillero, adarga antigua, rocín "\
        "flaco y galgo corredor"
print(texto)
texto = texto.lower()
list_txt = texto.split()
set_txt = set(list_txt)
analisis = dict()  # genera un diccionario vacio
for palabra in set_txt:
    #print(palabra, " --> ",list_txt.count(palabra))
    analisis[palabra] = texto.count(palabra)
print(analisis)

