def ejercicio_1():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return persona


def ejercicio_2():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return persona["nombre"]


def ejercicio_3():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return persona["edad"]


def ejercicio_4():
    persona = {
        "nombre": "Ana"
    }

    persona["edad"] = 25

    return persona


def ejercicio_5():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    persona["edad"] = 30

    return persona


def ejercicio_6():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    persona.pop("edad")

    return persona


def ejercicio_7():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return persona.keys()


def ejercicio_8():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return persona.values()


def ejercicio_9():
    persona = {
        "nombre": "Ana",
        "edad": 25
    }

    return "nombre" in persona


def ejercicio_10():
    producto = {
        "nombre": "Notebook",
        "precio": 1000
    }

    producto["stock"] = 5

    return producto