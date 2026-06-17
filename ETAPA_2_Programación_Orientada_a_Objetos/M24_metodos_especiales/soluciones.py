# M24 - Métodos especiales
# Soluciones


def ejercicio_1():

    class Persona:

        def __init__(self):
            self.nombre = "Ana"

        def __str__(self):
            return self.nombre

    persona = Persona()

    return str(persona)


def ejercicio_2():

    class Auto:

        def __init__(self):
            self.marca = "Toyota"

        def __str__(self):
            return self.marca

    auto = Auto()

    return str(auto)


def ejercicio_3():

    class Perro:

        def __init__(self):
            self.nombre = "Firulais"

        def __repr__(self):
            return f"Perro('{self.nombre}')"

    perro = Perro()

    return repr(perro)


def ejercicio_4():

    class Libro:

        def __init__(self):
            self.titulo = "Python desde cero"

        def __str__(self):
            return self.titulo

    libro = Libro()

    return str(libro)


def ejercicio_5():

    class Alumno:

        def __init__(self):
            self.nombre = "Ana"

        def __repr__(self):
            return f"Alumno('{self.nombre}')"

    alumno = Alumno()

    return repr(alumno)


def ejercicio_6():

    class Celular:

        def __init__(self):
            self.marca = "Samsung"

        def __str__(self):
            return self.marca

    celular = Celular()

    return str(celular)


def ejercicio_7():

    class Producto:

        def __init__(self):
            self.nombre = "Mouse"

        def __repr__(self):
            return f"Producto('{self.nombre}')"

    producto = Producto()

    return repr(producto)


def ejercicio_8():

    class Cuenta:

        def __init__(self):
            self.saldo = 1000

        def __str__(self):
            return f"Saldo: {self.saldo}"

    cuenta = Cuenta()

    return str(cuenta)


def ejercicio_9():

    class Pelicula:

        def __init__(self):
            self.titulo = "Matrix"

        def __repr__(self):
            return f"Pelicula('{self.titulo}')"

    pelicula = Pelicula()

    return repr(pelicula)


def ejercicio_10():

    class Usuario:

        def __init__(self):
            self.email = "admin@mail.com"

        def __str__(self):
            return self.email

    usuario = Usuario()

    return str(usuario)