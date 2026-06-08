import math
import random

from math import sqrt
from math import pi

from utilidades.matematicas import sumar
from utilidades.matematicas import multiplicar

from utilidades.textos import saludar


def ejercicio_1():
    import math

    return math.sqrt(25)


def ejercicio_2():
    from math import sqrt

    return sqrt(36)


def ejercicio_3():
    import math as m

    return m.pow(2, 3)


def ejercicio_4():
    from utilidades.matematicas import sumar

    return sumar(10, 5)


def ejercicio_5():
    from utilidades.textos import saludar

    return saludar()


def ejercicio_6():
    from utilidades.matematicas import sumar
    from utilidades.matematicas import multiplicar

    return multiplicar(sumar(2, 3), 5)


def ejercicio_7():
    from math import pi

    return round(pi, 2)


def ejercicio_8():
    import random

    return hasattr(random, "randint")


def ejercicio_9():
    from utilidades.matematicas import multiplicar

    return multiplicar(4, 5)


def ejercicio_10():
    import math as m
    from math import sqrt

    valor = sqrt(25)

    if valor == 5:
        return "Módulo completado"

    return "Error"