# M19 - Constructores
# Soluciones


def ejercicio_1():

    class Persona:

        def __init__(self, nombre):
            self.nombre = nombre

    persona = Persona("Ana")

    return persona.nombre


def ejercicio_2():

    class Auto:

        def __init__(self, marca):
            self.marca = marca

    auto = Auto("Toyota")

    return auto.marca


def ejercicio_3():

    class Perro:

        def __init__(self, nombre):
            self.nombre = nombre

    perro = Perro("Firulais")

    return perro.nombre


def ejercicio_4():

    class Alumno:

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

    alumno = Alumno("Ana", 20)

    return alumno.edad


def ejercicio_5():

    class Producto:

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

    producto = Producto("Mouse", 1500)

    return producto.precio


def ejercicio_6():

    class Celular:

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

    celular = Celular("Samsung", "A54")

    return celular.modelo


def ejercicio_7():

    class Libro:

        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor

    libro = Libro("Python", "Guido")

    return libro.autor


def ejercicio_8():

    class Pelicula:

        def __init__(self, titulo, genero):
            self.titulo = titulo
            self.genero = genero

    pelicula = Pelicula("Matrix", "Ciencia ficción")

    return pelicula.genero


def ejercicio_9():

    class Cuenta:

        def __init__(self, titular, saldo):
            self.titular = titular
            self.saldo = saldo

    cuenta = Cuenta("Ana", 1000)

    return cuenta.saldo


def ejercicio_10():

    class Usuario:

        def __init__(self, nombre, email, rol):
            self.nombre = nombre
            self.email = email
            self.rol = rol

    usuario = Usuario(
        "Admin",
        "admin@mail.com",
        "administrador"
    )

    return usuario.rol