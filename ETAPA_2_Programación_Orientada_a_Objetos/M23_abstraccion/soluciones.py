# M23 - Abstracción
# Soluciones


from abc import ABC
from abc import abstractmethod


def ejercicio_1():

    class Animal(ABC):

        @abstractmethod
        def hablar(self):
            pass

    class Perro(Animal):

        def hablar(self):
            return "Guau"

    perro = Perro()

    return perro.hablar()


def ejercicio_2():

    class Vehiculo(ABC):

        @abstractmethod
        def mover(self):
            pass

    class Auto(Vehiculo):

        def mover(self):
            return "Circulando"

    auto = Auto()

    return auto.mover()


def ejercicio_3():

    class Animal(ABC):

        @abstractmethod
        def hablar(self):
            pass

    class Gato(Animal):

        def hablar(self):
            return "Miau"

    gato = Gato()

    return gato.hablar()


def ejercicio_4():

    class Figura(ABC):

        @abstractmethod
        def area(self):
            pass

    class Cuadrado(Figura):

        def area(self):
            return "Área calculada"

    cuadrado = Cuadrado()

    return cuadrado.area()


def ejercicio_5():

    class Empleado(ABC):

        @abstractmethod
        def trabajar(self):
            pass

    class Programador(Empleado):

        def trabajar(self):
            return "Programando"

    programador = Programador()

    return programador.trabajar()


def ejercicio_6():

    class Cuenta(ABC):

        @abstractmethod
        def consultar(self):
            pass

    class CuentaCorriente(Cuenta):

        def consultar(self):
            return "Consultando saldo"

    cuenta = CuentaCorriente()

    return cuenta.consultar()


def ejercicio_7():

    class Persona(ABC):

        @abstractmethod
        def saludar(self):
            pass

    class Profesor(Persona):

        def saludar(self):
            return "Buenos días"

    profesor = Profesor()

    return profesor.saludar()


def ejercicio_8():

    class Dispositivo(ABC):

        @abstractmethod
        def encender(self):
            pass

    class Celular(Dispositivo):

        def encender(self):
            return "Encendido"

    celular = Celular()

    return celular.encender()


def ejercicio_9():

    class Libro(ABC):

        @abstractmethod
        def leer(self):
            pass

    class Manual(Libro):

        def leer(self):
            return "Leyendo"

    manual = Manual()

    return manual.leer()


def ejercicio_10():

    class Animal(ABC):

        @abstractmethod
        def hablar(self):
            pass

    class Pajaro(Animal):

        def hablar(self):
            return "Pío pío"

    pajaro = Pajaro()

    return pajaro.hablar()