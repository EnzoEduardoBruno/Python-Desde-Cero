# M28 - Proyecto final POO
# Soluciones


from dataclasses import dataclass


def ejercicio_1():

    @dataclass
    class Libro:

        titulo: str
        autor: str
        disponible: bool = True


    libro = Libro(
        "Python desde cero",
        "Guido"
    )

    return libro.titulo


def ejercicio_2():

    class Biblioteca:

        def __init__(self):

            self.libros = []


    biblioteca = Biblioteca()

    return len(biblioteca.libros)


def ejercicio_3():

    @dataclass
    class Libro:

        titulo: str
        autor: str
        disponible: bool = True


    class Biblioteca:

        def __init__(self):

            self.libros = []

        def agregar_libro(self, libro):

            self.libros.append(libro)


    biblioteca = Biblioteca()

    libro = Libro(
        "Python desde cero",
        "Guido"
    )

    biblioteca.agregar_libro(libro)

    return len(biblioteca.libros)


def ejercicio_4():

    @dataclass
    class Libro:

        titulo: str
        autor: str
        disponible: bool = True


    class Biblioteca:

        def __init__(self):

            self.libros = []

        def agregar_libro(self, libro):

            self.libros.append(libro)

        def buscar_libro(self, titulo):

            for libro in self.libros:

                if libro.titulo == titulo:

                    return libro.titulo


    biblioteca = Biblioteca()

    libro = Libro(
        "Python desde cero",
        "Guido"
    )

    biblioteca.agregar_libro(libro)

    return biblioteca.buscar_libro(
        "Python desde cero"
    )


def ejercicio_5():

    class CuentaBancaria:

        def __init__(
            self,
            titular,
            saldo
        ):

            self.titular = titular

            self.saldo = saldo


    cuenta = CuentaBancaria(
        "Ana",
        1000
    )

    return cuenta.saldo


def ejercicio_6():

    class CuentaBancaria:

        def __init__(
            self,
            titular,
            saldo
        ):

            self.titular = titular

            self.saldo = saldo

        def depositar(
            self,
            monto
        ):

            self.saldo += monto


    cuenta = CuentaBancaria(
        "Ana",
        1000
    )

    cuenta.depositar(500)

    return cuenta.saldo


def ejercicio_7():

    class CuentaBancaria:

        def __init__(
            self,
            titular,
            saldo
        ):

            self.titular = titular

            self.saldo = saldo

        def extraer(
            self,
            monto
        ):

            if monto <= self.saldo:

                self.saldo -= monto

                return "Extracción realizada"

            return "Saldo insuficiente"


    cuenta = CuentaBancaria(
        "Ana",
        1000
    )

    return cuenta.extraer(500)


def ejercicio_8():

    class Alumno:

        def __init__(
            self,
            nombre
        ):

            self.nombre = nombre

            self.notas = []


    alumno = Alumno("Juan")

    return alumno.nombre


def ejercicio_9():

    class Alumno:

        def __init__(
            self,
            nombre
        ):

            self.nombre = nombre

            self.notas = []

        def agregar_nota(
            self,
            nota
        ):

            self.notas.append(nota)


    alumno = Alumno("Juan")

    alumno.agregar_nota(8)

    return alumno.notas


def ejercicio_10():

    class Alumno:

        def __init__(
            self,
            nombre
        ):

            self.nombre = nombre

            self.notas = []

        def agregar_nota(
            self,
            nota
        ):

            self.notas.append(nota)

        def calcular_promedio(self):

            return (
                sum(self.notas)
                / len(self.notas)
            )


    alumno = Alumno("Juan")

    alumno.agregar_nota(8)

    alumno.agregar_nota(9)

    alumno.agregar_nota(10)

    return alumno.calcular_promedio()