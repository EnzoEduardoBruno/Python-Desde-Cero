# M20 - Encapsulamiento
# Soluciones


def ejercicio_1():

    class Persona:

        def __init__(self):
            self.nombre = "Ana"

    persona = Persona()

    return persona.nombre


def ejercicio_2():

    class Cuenta:

        def __init__(self):
            self._saldo = 1000

    cuenta = Cuenta()

    return cuenta._saldo


def ejercicio_3():

    class Usuario:

        def __init__(self):
            self.__clave = "1234"

    usuario = Usuario()

    return usuario._Usuario__clave


def ejercicio_4():

    class Auto:

        def __init__(self):
            self.marca = "Toyota"
            self._modelo = "Corolla"

    auto = Auto()

    return auto._modelo


def ejercicio_5():

    class Alumno:

        def __init__(self):
            self.__legajo = 100

    alumno = Alumno()

    return alumno._Alumno__legajo


def ejercicio_6():

    class Producto:

        def __init__(self):
            self.nombre = "Mouse"
            self._stock = 50

    producto = Producto()

    return producto._stock


def ejercicio_7():

    class Libro:

        def __init__(self):
            self.__titulo = "Python"

    libro = Libro()

    return libro._Libro__titulo


def ejercicio_8():

    class Pelicula:

        def __init__(self):
            self.genero = "Acción"
            self._duracion = 120

    pelicula = Pelicula()

    return pelicula._duracion


def ejercicio_9():

    class Celular:

        def __init__(self):
            self.__imei = "ABC123"

    celular = Celular()

    return celular._Celular__imei


def ejercicio_10():

    class CuentaBancaria:

        def __init__(self):
            self.titular = "Ana"
            self._saldo = 1000
            self.__clave = "1234"

    cuenta = CuentaBancaria()

    return cuenta._saldo