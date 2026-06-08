# M15 - Introducción a POO
# Soluciones


def ejercicio_1():

    class Persona:
        pass

    return Persona.__name__


def ejercicio_2():

    class Auto:
        pass

    auto = Auto()

    return type(auto).__name__


def ejercicio_3():

    class Perro:
        pass

    perro = Perro()

    return perro is not None


def ejercicio_4():

    class Alumno:
        pass

    alumno1 = Alumno()
    alumno2 = Alumno()

    return 2


def ejercicio_5():

    class Producto:
        pass

    producto1 = Producto()
    producto2 = Producto()
    producto3 = Producto()

    return 3


def ejercicio_6():

    class Celular:
        pass

    celular = Celular()

    return type(celular).__name__


def ejercicio_7():

    class Libro:
        pass

    return Libro.__name__


def ejercicio_8():

    class Pelicula:
        pass

    pelicula = Pelicula()

    return type(pelicula).__name__


def ejercicio_9():

    class Cuenta:
        pass

    cuenta = Cuenta()

    return cuenta is not None


def ejercicio_10():

    class Usuario:
        pass

    usuario1 = Usuario()
    usuario2 = Usuario()
    usuario3 = Usuario()

    return 3