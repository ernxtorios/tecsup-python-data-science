alumnos = [{"name": "Juan", "apellido": "Garcia", "edad": 18},
    {"name": "Maria", "apellido": "Perez", "edad": 21},
    {"name": "Percy", "apellido": "Rojas", "edad": 20}]

""" 
Crear el siguiente archivo alumnos.txt   
name:apellido:edad
Juan:Garcia:18
Maria:Perez:21
Percy:Rojas:20
"""

with open("Tecsup/modulo1/semana4/alumnos.txt","w") as archivo_alumnos:
    archivo_alumnos.write("nombre:apellido:edad\n")
    for x in alumnos:
        archivo_alumnos.write(x["name"] + ":" + x["apellido"] + ":" + str(x["edad"]) + "\n")

# Solución con funciones
def cabecera(alumno):
    return ":".join(alumno.keys())

def transformar(alumno):
    return ":".join(alumno.values())

with open("Tecsup/modulo1/semana4/alumnos.txt","w") as archivo:
    archivo.write(cabecera(alumnos[0]))
    for alumno in alumnos :        # se le cada alumno
        fmt = transformar(alumno)
        archivo.write(fmt)

# Otra solución definitiva
def cabecera(alumno):
    cab = ":".join(alumno.keys())
    print(cab)
    return cab

def transformar(alumno):
    for (key,value) in alumno.items():
        alumno[key] = str(value)
    # alumno["edad"]=str(alumno["edad"])
    info = ":".join(alumno.values())
    print(info)
    return info

with open("Tecsup/modulo1/semana4/alumnos.txt","w") as archivo:
    archivo.write(cabecera(alumnos[0]) + "\n")
    for alumno in alumnos :        # se le cada alumno
        fmt = transformar(alumno)
        archivo.write(fmt + "\n")