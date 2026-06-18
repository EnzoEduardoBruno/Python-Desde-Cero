# M28 - Proyecto final POO
# Completar cada ejercicio.
#
# Importante:
# - No cambiar el nombre de las funciones.
# - No cambiar las clases solicitadas.
# - Borrar pass y escribir la solución.
# - Usar return.
#
# En este módulo vas a integrar:
# - dataclasses
# - constructores
# - atributos
# - métodos
# - listas dentro de objetos
# - composición
# - sistemas reales


from dataclasses import dataclass


# =========================
# Ejercicio 1
# =========================
# Crear:
#
# @dataclass
# class Libro:
#
#     titulo: str
#     autor: str
#     disponible: bool = True
#
# Crear:
#
# libro = Libro("Python desde cero", "Guido")
#
# Retornar:
#
# libro.titulo
#
# Resultado esperado:
#
# "Python desde cero"

def ejercicio_1():
    pass


# =========================
# Ejercicio 2
# =========================
# Crear:
#
# class Biblioteca:
#
#     def __init__(self):
#
#         self.libros = []
#
# Crear:
#
# biblioteca = Biblioteca()
#
# Retornar:
#
# len(biblioteca.libros)
#
# Resultado esperado:
#
# 0

def ejercicio_2():
    pass


# =========================
# Ejercicio 3
# =========================
# Crear:
#
# class Biblioteca:
#
#     def __init__(self):
#
#         self.libros = []
#
#     def agregar_libro(self, libro):
#
#         self.libros.append(libro)
#
# Crear:
#
# biblioteca = Biblioteca()
#
# libro = Libro("Python desde cero", "Guido")
#
# biblioteca.agregar_libro(libro)
#
# Retornar:
#
# len(biblioteca.libros)
#
# Resultado esperado:
#
# 1

def ejercicio_3():
    pass


# =========================
# Ejercicio 4
# =========================
# Agregar a Biblioteca:
#
# def buscar_libro(self, titulo):
#
#     recorrer self.libros
#
#     si encuentra el título:
#
#         return libro.titulo
#
# Crear:
#
# biblioteca = Biblioteca()
#
# libro = Libro("Python desde cero", "Guido")
#
# biblioteca.agregar_libro(libro)
#
# Retornar:
#
# biblioteca.buscar_libro("Python desde cero")
#
# Resultado esperado:
#
# "Python desde cero"

def ejercicio_4():
    pass


# =========================
# Ejercicio 5
# =========================
# Crear:
#
# class CuentaBancaria:
#
#     def __init__(self, titular, saldo):
#
#         self.titular = titular
#
#         self.saldo = saldo
#
# Crear:
#
# cuenta = CuentaBancaria("Ana", 1000)
#
# Retornar:
#
# cuenta.saldo
#
# Resultado esperado:
#
# 1000

def ejercicio_5():
    pass


# =========================
# Ejercicio 6
# =========================
# Agregar:
#
# def depositar(self, monto):
#
#     self.saldo += monto
#
# Crear:
#
# cuenta = CuentaBancaria("Ana", 1000)
#
# cuenta.depositar(500)
#
# Retornar:
#
# cuenta.saldo
#
# Resultado esperado:
#
# 1500

def ejercicio_6():
    pass


# =========================
# Ejercicio 7
# =========================
# Agregar:
#
# def extraer(self, monto):
#
#     if monto <= self.saldo:
#
#         self.saldo -= monto
#
#         return "Extracción realizada"
#
#     return "Saldo insuficiente"
#
# Crear:
#
# cuenta = CuentaBancaria("Ana", 1000)
#
# Retornar:
#
# cuenta.extraer(500)
#
# Resultado esperado:
#
# "Extracción realizada"

def ejercicio_7():
    pass


# =========================
# Ejercicio 8
# =========================
# Crear:
#
# class Alumno:
#
#     def __init__(self, nombre):
#
#         self.nombre = nombre
#
#         self.notas = []
#
# Crear:
#
# alumno = Alumno("Juan")
#
# Retornar:
#
# alumno.nombre
#
# Resultado esperado:
#
# "Juan"

def ejercicio_8():
    pass


# =========================
# Ejercicio 9
# =========================
# Agregar:
#
# def agregar_nota(self, nota):
#
#     self.notas.append(nota)
#
# Crear:
#
# alumno = Alumno("Juan")
#
# alumno.agregar_nota(8)
#
# Retornar:
#
# alumno.notas
#
# Resultado esperado:
#
# [8]

def ejercicio_9():
    pass


# =========================
# Ejercicio 10
# =========================
# Agregar:
#
# def calcular_promedio(self):
#
#     return sum(self.notas) / len(self.notas)
#
# Crear:
#
# alumno = Alumno("Juan")
#
# alumno.agregar_nota(8)
#
# alumno.agregar_nota(9)
#
# alumno.agregar_nota(10)
#
# Retornar:
#
# alumno.calcular_promedio()
#
# Resultado esperado:
#
# 9.0

def ejercicio_10():
    pass