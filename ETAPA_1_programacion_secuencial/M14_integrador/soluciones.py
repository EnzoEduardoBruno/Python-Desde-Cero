# M14 - Ejercicios Integradores
# Soluciones de referencia.


def ejercicio_1(a, b):
    return a + b


def ejercicio_2(a, b):
    return a - b


def ejercicio_3(a, b, operacion):

    if operacion == "suma":
        return a + b

    elif operacion == "resta":
        return a - b

    elif operacion == "multiplicacion":
        return a * b

    elif operacion == "division":
        return a / b

    else:
        return "Operación inválida"


def ejercicio_4(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "No se puede dividir por cero"


def ejercicio_5(nombre, telefono):
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }

    return contacto


def ejercicio_6(agenda, nombre):

    for contacto in agenda:

        if contacto["nombre"] == nombre:
            return contacto

    return "Contacto no encontrado"


def ejercicio_7(agenda, contacto):
    agenda.append(contacto)

    return agenda


def ejercicio_8(notas):
    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)

    return promedio


def ejercicio_9(promedio):

    if promedio >= 6:
        return True

    else:
        return False


def ejercicio_10(alumno):
    suma = 0

    for nota in alumno["notas"]:
        suma += nota

    promedio = suma / len(alumno["notas"])

    aprobado = promedio >= 6

    resultado = {
        "nombre": alumno["nombre"],
        "promedio": promedio,
        "aprobado": aprobado
    }

    return resultado