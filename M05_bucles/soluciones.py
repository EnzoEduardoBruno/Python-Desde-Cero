def ejercicio_1():
    numeros = []
    contador = 1

    while contador <= 5:
        numeros.append(contador)
        contador += 1

    return numeros


def ejercicio_2():
    numeros = []

    for numero in range(5):
        numeros.append(numero)

    return numeros


def ejercicio_3():
    numeros = []

    for numero in range(1, 11):
        numeros.append(numero)

    return numeros


def ejercicio_4():
    numeros = []

    for numero in range(10):
        if numero == 5:
            break

        numeros.append(numero)

    return numeros


def ejercicio_5():
    numeros = []

    for numero in range(5):
        if numero == 2:
            continue

        numeros.append(numero)

    return numeros


def ejercicio_6():
    contador = 1
    suma = 0

    while contador <= 5:
        suma += contador
        contador += 1

    return suma


def ejercicio_7():
    textos = []

    for _ in range(3):
        textos.append("Python")

    return textos


def ejercicio_8():
    numeros = []

    for numero in range(5, 11):
        numeros.append(numero)

    return numeros


def ejercicio_9():
    contador = 0

    while True:
        if contador == 3:
            break

        contador += 1

    return contador


def ejercicio_10():
    numeros = []

    for numero in range(3):
        numeros.append(numero)

    return numeros