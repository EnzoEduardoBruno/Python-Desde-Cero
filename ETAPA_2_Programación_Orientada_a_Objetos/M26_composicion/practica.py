# M26 - Composición y agregación
# Completar cada ejercicio.
#
# Importante:
# - No cambiar el nombre de las funciones.
# - No cambiar las clases solicitadas.
# - Borrar pass y escribir la solución.
# - Usar return.
#
# En este módulo vas a practicar:
# - ES UN
# - Tiene un
# - Usa un
# - composición
# - agregación
# - objetos dentro de objetos


# =========================
# Ejercicio 1
# =========================
# Crear:
#
# class Motor:
#
#     def arrancar(self):
#         return "Motor encendido"
#
#
# class Auto:
#
#     def __init__(self):
#         self.motor = Motor()
#
# Crear:
#
# auto = Auto()
#
# Retornar:
#
# auto.motor.arrancar()
#
# Resultado esperado:
#
# "Motor encendido"

def ejercicio_1():
    pass


# =========================
# Ejercicio 2
# =========================
# Crear:
#
# class Procesador:
#
#     def informacion(self):
#         return "Ryzen 7"
#
#
# class Computadora:
#
#     def __init__(self):
#         self.procesador = Procesador()
#
# Crear:
#
# pc = Computadora()
#
# Retornar:
#
# pc.procesador.informacion()
#
# Resultado esperado:
#
# "Ryzen 7"

def ejercicio_2():
    pass


# =========================
# Ejercicio 3
# =========================
# Crear:
#
# class Profesor:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#
# class Curso:
#
#     def __init__(self, profesor):
#         self.profesor = profesor
#
# Crear:
#
# profesor = Profesor("Ana")
# curso = Curso(profesor)
#
# Retornar:
#
# curso.profesor.nombre
#
# Resultado esperado:
#
# "Ana"

def ejercicio_3():
    pass


# =========================
# Ejercicio 4
# =========================
# Crear:
#
# class Alumno:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#
# class Curso:
#
#     def __init__(self, alumno):
#         self.alumno = alumno
#
# Crear:
#
# alumno = Alumno("Juan")
# curso = Curso(alumno)
#
# Retornar:
#
# curso.alumno.nombre
#
# Resultado esperado:
#
# "Juan"

def ejercicio_4():
    pass


# =========================
# Ejercicio 5
# =========================
# Crear:
#
# class Bateria:
#
#     def estado(self):
#         return "Batería cargada"
#
#
# class Celular:
#
#     def __init__(self):
#         self.bateria = Bateria()
#
# Crear:
#
# celular = Celular()
#
# Retornar:
#
# celular.bateria.estado()
#
# Resultado esperado:
#
# "Batería cargada"

def ejercicio_5():
    pass


# =========================
# Ejercicio 6
# =========================
# Crear:
#
# class Direccion:
#
#     def __init__(self, ciudad):
#         self.ciudad = ciudad
#
#
# class Persona:
#
#     def __init__(self, direccion):
#         self.direccion = direccion
#
# Crear:
#
# direccion = Direccion("Córdoba")
# persona = Persona(direccion)
#
# Retornar:
#
# persona.direccion.ciudad
#
# Resultado esperado:
#
# "Córdoba"

def ejercicio_6():
    pass


# =========================
# Ejercicio 7
# =========================
# Crear:
#
# class Pantalla:
#
#     def mostrar(self):
#         return "Mostrando imagen"
#
#
# class Televisor:
#
#     def __init__(self):
#         self.pantalla = Pantalla()
#
# Crear:
#
# televisor = Televisor()
#
# Retornar:
#
# televisor.pantalla.mostrar()
#
# Resultado esperado:
#
# "Mostrando imagen"

def ejercicio_7():
    pass


# =========================
# Ejercicio 8
# =========================
# Crear:
#
# class Autor:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#
# class Libro:
#
#     def __init__(self, autor):
#         self.autor = autor
#
# Crear:
#
# autor = Autor("Guido")
# libro = Libro(autor)
#
# Retornar:
#
# libro.autor.nombre
#
# Resultado esperado:
#
# "Guido"

def ejercicio_8():
    pass


# =========================
# Ejercicio 9
# =========================
# Crear:
#
# class Teclado:
#
#     def escribir(self):
#         return "Escribiendo"
#
#
# class Notebook:
#
#     def __init__(self):
#         self.teclado = Teclado()
#
# Crear:
#
# notebook = Notebook()
#
# Retornar:
#
# notebook.teclado.escribir()
#
# Resultado esperado:
#
# "Escribiendo"

def ejercicio_9():
    pass


# =========================
# Ejercicio 10
# =========================
# Crear:
#
# class Empresa:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#
# class Empleado:
#
#     def __init__(self, empresa):
#         self.empresa = empresa
#
# Crear:
#
# empresa = Empresa("BeeSoftware")
# empleado = Empleado(empresa)
#
# Retornar:
#
# empleado.empresa.nombre
#
# Resultado esperado:
#
# "BeeSoftware"

def ejercicio_10():
    pass