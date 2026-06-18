# M27 - Dataclasses y Duck Typing
# Completar cada ejercicio.
#
# Importante:
# - No cambiar el nombre de las funciones.
# - No cambiar las clases solicitadas.
# - Borrar pass y escribir la solución.
# - Usar return.
#
# En este módulo vas a practicar:
# - @dataclass
# - constructor automático
# - Duck Typing
# - comportamiento por interfaz


from dataclasses import dataclass


# =========================
# Ejercicio 1
# =========================
# Crear:
#
# @dataclass
# class Persona:
#
#     nombre: str
#     edad: int
#
# Crear:
#
# persona = Persona("Ana", 20)
#
# Retornar:
#
# persona.nombre
#
# Resultado esperado:
#
# "Ana"

def ejercicio_1():
    pass


# =========================
# Ejercicio 2
# =========================
# Crear:
#
# @dataclass
# class Producto:
#
#     nombre: str
#     precio: int
#
# Crear:
#
# producto = Producto("Mouse", 1500)
#
# Retornar:
#
# producto.precio
#
# Resultado esperado:
#
# 1500

def ejercicio_2():
    pass


# =========================
# Ejercicio 3
# =========================
# Crear:
#
# @dataclass
# class Alumno:
#
#     nombre: str
#     nota: int
#
# Crear:
#
# alumno = Alumno("Juan", 8)
#
# Retornar:
#
# alumno.nota
#
# Resultado esperado:
#
# 8

def ejercicio_3():
    pass


# =========================
# Ejercicio 4
# =========================
# Crear:
#
# @dataclass
# class Libro:
#
#     titulo: str
#     autor: str
#
# Crear:
#
# libro = Libro("Python", "Guido")
#
# Retornar:
#
# libro.autor
#
# Resultado esperado:
#
# "Guido"

def ejercicio_4():
    pass


# =========================
# Ejercicio 5
# =========================
# Crear:
#
# @dataclass
# class Usuario:
#
#     nombre: str
#     email: str
#
# Crear:
#
# usuario = Usuario("Admin", "admin@mail.com")
#
# Retornar:
#
# usuario.email
#
# Resultado esperado:
#
# "admin@mail.com"

def ejercicio_5():
    pass


# =========================
# Ejercicio 6
# =========================
# Crear:
#
# class Perro:
#
#     def hablar(self):
#         return "Guau"
#
#
# class Gato:
#
#     def hablar(self):
#         return "Miau"
#
#
# def hacer_hablar(animal):
#
#     return animal.hablar()
#
# Crear:
#
# perro = Perro()
#
# Retornar:
#
# hacer_hablar(perro)
#
# Resultado esperado:
#
# "Guau"

def ejercicio_6():
    pass


# =========================
# Ejercicio 7
# =========================
# Crear:
#
# class Auto:
#
#     def mover(self):
#         return "Auto moviéndose"
#
#
# class Barco:
#
#     def mover(self):
#         return "Barco navegando"
#
#
# def iniciar_movimiento(objeto):
#
#     return objeto.mover()
#
# Crear:
#
# auto = Auto()
#
# Retornar:
#
# iniciar_movimiento(auto)
#
# Resultado esperado:
#
# "Auto moviéndose"

def ejercicio_7():
    pass


# =========================
# Ejercicio 8
# =========================
# Crear:
#
# class Impresora:
#
#     def mostrar(self):
#         return "Imprimiendo"
#
#
# class Pantalla:
#
#     def mostrar(self):
#         return "Mostrando"
#
#
# def ejecutar(objeto):
#
#     return objeto.mostrar()
#
# Crear:
#
# impresora = Impresora()
#
# Retornar:
#
# ejecutar(impresora)
#
# Resultado esperado:
#
# "Imprimiendo"

def ejercicio_8():
    pass


# =========================
# Ejercicio 9
# =========================
# Crear:
#
# @dataclass
# class Cuenta:
#
#     titular: str
#     saldo: int
#
# Crear:
#
# cuenta = Cuenta("Ana", 1000)
#
# Retornar:
#
# cuenta.saldo
#
# Resultado esperado:
#
# 1000

def ejercicio_9():
    pass


# =========================
# Ejercicio 10
# =========================
# Crear:
#
# @dataclass
# class Mensaje:
#
#     texto: str
#
#
# class Notificador:
#
#     def enviar(self, mensaje):
#         return mensaje.texto
#
# Crear:
#
# mensaje = Mensaje("Hola mundo")
#
# notificador = Notificador()
#
# Retornar:
#
# notificador.enviar(mensaje)
#
# Resultado esperado:
#
# "Hola mundo"

def ejercicio_10():
    pass