def ejercicio_1():
    colores = ["rojo", "verde", "azul"]

    return colores


def ejercicio_2():
    colores = ["rojo", "verde", "azul"]

    return colores[0]


def ejercicio_3():
    colores = ["rojo", "verde", "azul"]

    return colores[-1]


def ejercicio_4():
    colores = ["rojo", "verde"]

    colores.append("azul")

    return colores


def ejercicio_5():
    colores = ["rojo", "verde", "azul"]

    colores.remove("verde")

    return colores


def ejercicio_6():
    colores = ["rojo", "azul"]

    colores.insert(1, "verde")

    return colores


def ejercicio_7():
    colores = ["rojo", "verde", "azul"]

    return len(colores)


def ejercicio_8():
    numeros = []

    for numero in range(5):
        numeros.append(numero)

    return numeros


def ejercicio_9():
    colores = ["rojo", "verde", "azul"]

    return "verde" in colores


def ejercicio_10():
    lenguajes = ["Python", "JavaScript", "Java"]

    lenguajes.append("C#")
    lenguajes.remove("Java")
    lenguajes.insert(1, "TypeScript")

    return lenguajes