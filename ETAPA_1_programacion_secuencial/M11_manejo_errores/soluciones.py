def ejercicio_1():
    texto = "10"

    try:
        numero = int(texto)
        return numero

    except ValueError:
        return "Error"


def ejercicio_2():
    texto = "hola"

    try:
        numero = int(texto)
        return numero

    except ValueError:
        return "Error"


def ejercicio_3():
    try:
        resultado = 10 / 2
        return resultado

    except ZeroDivisionError:
        return "Error"


def ejercicio_4():
    try:
        resultado = 10 / 0
        return resultado

    except ZeroDivisionError:
        return "No se puede dividir por cero"


def ejercicio_5():
    texto = "python"

    try:
        numero = int(texto)
        return numero

    except ValueError:
        return "Valor inválido"


def ejercicio_6():
    try:
        resultado = 20 / 0
        return resultado

    except ZeroDivisionError:
        return "División inválida"


def ejercicio_7():
    try:
        resultado = "En proceso"

    except:
        resultado = "Error"

    finally:
        resultado = "Finalizado"

    return resultado


def ejercicio_8():
    try:
        texto = "abc"
        resultado = int(texto)

    except ValueError:
        resultado = "Error"

    finally:
        resultado = "Finalizado"

    return resultado


def ejercicio_9():
    numeros = [1, 2, 3]

    try:
        return numeros[10]

    except IndexError:
        return "Índice inválido"


def ejercicio_10():
    persona = {
        "nombre": "Ana"
    }

    try:
        return persona["edad"]

    except KeyError:
        return "Clave inexistente"