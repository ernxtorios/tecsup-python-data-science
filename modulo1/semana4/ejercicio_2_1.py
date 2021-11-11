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

def cabecera(alumno):
    cab = ":".join(alumno.keys())
    return cab

def transformar(alumno):
    for (key, value) in alumno.items():
        alumno[key] = str(value)
    info = ":".join(alumno.values())
    return info

with open("Tecsup/modulo1/semana4/los_alumnos.txt","w") as archivo:
    archivo.write(cabecera(alumnos[0]) + "\n")
    for alumno in alumnos :        
        fmt = transformar(alumno)
        archivo.write(fmt + "\n")