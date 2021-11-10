"""
Función para obtener los datos del trabajador
Almacena los datos ingresados en una lista
Devuelve la lista con los datos del trabajador
"""
def leer_datos_trabajador():
    datos_trabajador = list()

    print("-"*100)
    print("Ingreso de datos del trabajador")
    ocupacion = input("Ocupación (Contador(a), Administrador(a), Programador(a)): ")
    # Valida que la ocupación sea una de las requeridas
    while not validar_ocupacion(str(ocupacion).lower()):
        print("La ocupación no es correcta, vuelva a intentarlo por favor")
        ocupacion = input("Ocupación (Contador(a), Administrador(a), Programador(a)): ")
    horas_trabajadas = int(input("Horas trabajadas: "))
    sueldo_hora = float(input("Sueldo por hora: "))
    numero_hijos = int(input("Número de hijos: "))
    print("-"*100)

    datos_trabajador.append(str(ocupacion).capitalize())
    datos_trabajador.append(horas_trabajadas)
    datos_trabajador.append(sueldo_hora)
    datos_trabajador.append(numero_hijos)

    return datos_trabajador

"""
Función para validar que la ocupación sea 
contador, administrador o programador.
Devuelve True si es una de las ocupaciones requeridas,
de lo contrario devuelve False
"""
def validar_ocupacion(ocupacion):
    if ocupacion in ("contador", "contadora", "administrador", "administradora", "programador", "programadora"):
        return True
    else:
        return False

"""
Función para calcular el pago bruto del trabajador
de acuerdo a las horas trabajadas y el sueldo por hora.
Devuelve el cálculo realizado: horas_trabajadas * sueldo_hora
"""
def calcular_pago_bruto(horas_trabajadas, sueldo_hora):
    return horas_trabajadas * sueldo_hora

"""
Función para calcular el impuesto aplicado al trabajador
de acuerdo al pago bruto.
Todos los trabajadores pagan el 10% de impuesto 
siempre que el pago bruto supere los 2000 soles.
Devuelve el cálculo realizado: pago_bruto * 0.10, si corresponde,
de lo contrario devuelve cero.
"""
def calcular_impuesto(pago_bruto):
    impuesto = 0
    if pago_bruto > 2000:
        impuesto = pago_bruto * 0.10
    
    return impuesto

"""
Función para calcular el descuento aplicado al trabajador
de acuerdo a su ocupación y al pago bruto.
Únicamente a los contadores se les descuenta el 5% del pago bruto,
mientras que a los demás es el 8% del pago bruto.
Devuelve el cálculo realizado: pago_bruto * 0.05 o pago_bruto * 0.08, 
según corresponde.
"""
def calcular_descuento(ocupacion, pago_bruto):
    if str(ocupacion).lower() == "contador" or str(ocupacion).lower() == "contadora":
        descuento = pago_bruto * 0.05
    else:
        descuento = pago_bruto * 0.08
    
    return descuento

"""
Función para calcular la bonificación aplicada al trabajador
de acuerdo al número de hijos y al pago bruto.
La bonificación es el 1% del pago bruto por hijo. 
Devuelve el cálculo realizado: numero_hijos * pago_bruto * 0.01.
"""
def calcular_bonificacion(numero_hijos, pago_bruto):
    return numero_hijos * pago_bruto * 0.01

"""
Función para calcular del pago neto del trabajador,
de acuerdo a su pago bruto, el impuesto, el descuento y la bonficación,
que le corresponde. 
Devuelve el cálculo realizado: pago_bruto - impuesto - descuento + bonificacion.
"""
def calcular_pago_neto(pago_bruto, impuesto, descuento, bonificacion):
    return pago_bruto - impuesto - descuento + bonificacion

"""
Función para mostrar la inforfmación del trabajador, de acuerdo a
los datos almacenados en la lista que contiene los datos del trabajador.
Muestra en pantalla los datos del trabajador, además de 
el pago bruto, el impuesto, el descuento, la bonificación y el pago neto del trabajador.
"""
def imprimir_pago(datos_trabajador):
    pago_bruto = calcular_pago_bruto(datos_trabajador[1], datos_trabajador[2])
    impuesto = calcular_impuesto(pago_bruto)
    descuento = calcular_descuento(datos_trabajador[0], pago_bruto)
    bonificacion = calcular_bonificacion(datos_trabajador[3], pago_bruto)

    print("Ocupación:", datos_trabajador[0])
    print("Horas trabajadas:", datos_trabajador[1])
    print("Sueldo por hora:", f"{datos_trabajador[2]:.2f}")
    print("Número de hijos:", datos_trabajador[3])
    print("-"*100)
    print("Pago bruto:", f"{pago_bruto:.2f}", "soles")
    print("Impuesto:", f"{impuesto:.2f}", "soles")
    print("Descuento:", f"{descuento:.2f}", "soles")
    print("Bonificación:", f"{bonificacion:.2f}", "soles")
    print("Pago neto:", f"{calcular_pago_neto(pago_bruto, impuesto, descuento, bonificacion):.2f}", "soles")
