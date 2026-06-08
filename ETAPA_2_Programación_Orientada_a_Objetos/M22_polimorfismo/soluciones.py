# M22 - Polimorfismo
# Soluciones


def ejercicio_1():

    class Animal:

        def hablar(self):
            return "Sonido"

    class Perro(Animal):

        def hablar(self):
            return "Guau"

    perro = Perro()

    return perro.hablar()


def ejercicio_2():

    class Animal:

        def hablar(self):
            return "Sonido"

    class Gato(Animal):

        def hablar(self):
            return "Miau"

    gato = Gato()

    return gato.hablar()


def ejercicio_3():

    class Vehiculo:

        def mover(self):
            return "Moviéndose"

    class Auto(Vehiculo):

        def mover(self):
            return "Circulando"

    auto = Auto()

    return auto.mover()


def ejercicio_4():

    class Vehiculo:

        def mover(self):
            return "Moviéndose"

    class Avion(Vehiculo):

        def mover(self):
            return "Volando"

    avion = Avion()

    return avion.mover()


def ejercicio_5():

    class Animal:

        def hablar(self):
            return "Sonido"

    class Vaca(Animal):

        def hablar(self):
            return "Muuu"

    vaca = Vaca()

    return vaca.hablar()


def ejercicio_6():

    class Vehiculo:

        def mover(self):
            return "Moviéndose"

    class Moto(Vehiculo):

        def mover(self):
            return "Acelerando"

    moto = Moto()

    return moto.mover()


def ejercicio_7():

    class Persona:

        def saludar(self):
            return "Hola"

    class Profesor(Persona):

        def saludar(self):
            return "Buenos días"

    profesor = Profesor()

    return profesor.saludar()


def ejercicio_8():

    class Persona:

        def saludar(self):
            return "Hola"

    class Alumno(Persona):

        def saludar(self):
            return "Hola profe"

    alumno = Alumno()

    return alumno.saludar()


def ejercicio_9():

    class Vehiculo:

        def mover(self):
            return "Moviéndose"

    class Camion(Vehiculo):

        def mover(self):
            return "Transportando carga"

    camion = Camion()

    return camion.mover()


def ejercicio_10():

    class Animal:

        def hablar(self):
            return "Sonido"

    class Pajaro(Animal):

        def hablar(self):
            return "Pío pío"

    pajaro = Pajaro()

    return pajaro.hablar()