# M27 - Dataclasses y Duck Typing
# Soluciones


from dataclasses import dataclass


def ejercicio_1():

    @dataclass
    class Persona:

        nombre: str
        edad: int

    persona = Persona("Ana", 20)

    return persona.nombre


def ejercicio_2():

    @dataclass
    class Producto:

        nombre: str
        precio: int

    producto = Producto("Mouse", 1500)

    return producto.precio


def ejercicio_3():

    @dataclass
    class Alumno:

        nombre: str
        nota: int

    alumno = Alumno("Juan", 8)

    return alumno.nota


def ejercicio_4():

    @dataclass
    class Libro:

        titulo: str
        autor: str

    libro = Libro("Python", "Guido")

    return libro.autor


def ejercicio_5():

    @dataclass
    class Usuario:

        nombre: str
        email: str

    usuario = Usuario("Admin", "admin@mail.com")

    return usuario.email


def ejercicio_6():

    class Perro:

        def hablar(self):
            return "Guau"


    class Gato:

        def hablar(self):
            return "Miau"


    def hacer_hablar(animal):

        return animal.hablar()


    perro = Perro()

    return hacer_hablar(perro)


def ejercicio_7():

    class Auto:

        def mover(self):
            return "Auto moviéndose"


    class Barco:

        def mover(self):
            return "Barco navegando"


    def iniciar_movimiento(objeto):

        return objeto.mover()


    auto = Auto()

    return iniciar_movimiento(auto)


def ejercicio_8():

    class Impresora:

        def mostrar(self):
            return "Imprimiendo"


    class Pantalla:

        def mostrar(self):
            return "Mostrando"


    def ejecutar(objeto):

        return objeto.mostrar()


    impresora = Impresora()

    return ejecutar(impresora)


def ejercicio_9():

    @dataclass
    class Cuenta:

        titular: str
        saldo: int

    cuenta = Cuenta("Ana", 1000)

    return cuenta.saldo


def ejercicio_10():

    @dataclass
    class Mensaje:

        texto: str


    class Notificador:

        def enviar(self, mensaje):

            return mensaje.texto


    mensaje = Mensaje("Hola mundo")

    notificador = Notificador()

    return notificador.enviar(mensaje)