# M21 - Herencia
# Soluciones


def ejercicio_1():

    class Animal:

        def respirar(self):
            return "Respirando"

    class Perro(Animal):
        pass

    perro = Perro()

    return perro.respirar()


def ejercicio_2():

    class Vehiculo:

        def arrancar(self):
            return "Motor encendido"

    class Auto(Vehiculo):
        pass

    auto = Auto()

    return auto.arrancar()


def ejercicio_3():

    class Persona:

        def __init__(self):
            self.nombre = "Ana"

    class Alumno(Persona):
        pass

    alumno = Alumno()

    return alumno.nombre


def ejercicio_4():

    class Animal:

        def comer(self):
            return "Comiendo"

    class Gato(Animal):
        pass

    gato = Gato()

    return gato.comer()


def ejercicio_5():

    class Dispositivo:

        def encender(self):
            return "Encendido"

    class Celular(Dispositivo):
        pass

    celular = Celular()

    return celular.encender()


def ejercicio_6():

    class Empleado:

        def trabajar(self):
            return "Trabajando"

    class Programador(Empleado):
        pass

    programador = Programador()

    return programador.trabajar()


def ejercicio_7():

    class Cuenta:

        def consultar(self):
            return "Saldo disponible"

    class CuentaCorriente(Cuenta):
        pass

    cuenta = CuentaCorriente()

    return cuenta.consultar()


def ejercicio_8():

    class Libro:

        def leer(self):
            return "Leyendo"

    class Manual(Libro):
        pass

    manual = Manual()

    return manual.leer()


def ejercicio_9():

    class Persona:

        def saludar(self):
            return "Hola"

    class Profesor(Persona):
        pass

    profesor = Profesor()

    return profesor.saludar()


def ejercicio_10():

    class Vehiculo:

        def avanzar(self):
            return "Avanzando"

    class Moto(Vehiculo):
        pass

    moto = Moto()

    return moto.avanzar()