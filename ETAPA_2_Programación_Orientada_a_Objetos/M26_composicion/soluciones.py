# M26 - Composición y agregación
# Soluciones


def ejercicio_1():

    class Motor:

        def arrancar(self):
            return "Motor encendido"

    class Auto:

        def __init__(self):
            self.motor = Motor()

    auto = Auto()

    return auto.motor.arrancar()


def ejercicio_2():

    class Procesador:

        def informacion(self):
            return "Ryzen 7"

    class Computadora:

        def __init__(self):
            self.procesador = Procesador()

    pc = Computadora()

    return pc.procesador.informacion()


def ejercicio_3():

    class Profesor:

        def __init__(self, nombre):
            self.nombre = nombre

    class Curso:

        def __init__(self, profesor):
            self.profesor = profesor

    profesor = Profesor("Ana")

    curso = Curso(profesor)

    return curso.profesor.nombre


def ejercicio_4():

    class Alumno:

        def __init__(self, nombre):
            self.nombre = nombre

    class Curso:

        def __init__(self, alumno):
            self.alumno = alumno

    alumno = Alumno("Juan")

    curso = Curso(alumno)

    return curso.alumno.nombre


def ejercicio_5():

    class Bateria:

        def estado(self):
            return "Batería cargada"

    class Celular:

        def __init__(self):
            self.bateria = Bateria()

    celular = Celular()

    return celular.bateria.estado()


def ejercicio_6():

    class Direccion:

        def __init__(self, ciudad):
            self.ciudad = ciudad

    class Persona:

        def __init__(self, direccion):
            self.direccion = direccion

    direccion = Direccion("Córdoba")

    persona = Persona(direccion)

    return persona.direccion.ciudad


def ejercicio_7():

    class Pantalla:

        def mostrar(self):
            return "Mostrando imagen"

    class Televisor:

        def __init__(self):
            self.pantalla = Pantalla()

    televisor = Televisor()

    return televisor.pantalla.mostrar()


def ejercicio_8():

    class Autor:

        def __init__(self, nombre):
            self.nombre = nombre

    class Libro:

        def __init__(self, autor):
            self.autor = autor

    autor = Autor("Guido")

    libro = Libro(autor)

    return libro.autor.nombre


def ejercicio_9():

    class Teclado:

        def escribir(self):
            return "Escribiendo"

    class Notebook:

        def __init__(self):
            self.teclado = Teclado()

    notebook = Notebook()

    return notebook.teclado.escribir()


def ejercicio_10():

    class Empresa:

        def __init__(self, nombre):
            self.nombre = nombre

    class Empleado:

        def __init__(self, empresa):
            self.empresa = empresa

    empresa = Empresa("BeeSoftware")

    empleado = Empleado(empresa)

    return empleado.empresa.nombre