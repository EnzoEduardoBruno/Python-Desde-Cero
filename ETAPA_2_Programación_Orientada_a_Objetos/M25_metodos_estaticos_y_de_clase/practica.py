# M25 - Métodos estáticos y de clase
# Completar cada ejercicio.
#
# Importante:
# - No cambiar el nombre de las funciones.
# - No cambiar las clases solicitadas.
# - Borrar pass y escribir la solución.
# - Usar return.
#
# En este módulo vas a practicar:
# - @staticmethod
# - @classmethod
# - métodos estáticos
# - métodos de clase


# =========================
# Ejercicio 1
# =========================
# Crear:
#
# class Calculadora:
#
#     @staticmethod
#     def sumar(a, b):
#         return a + b
#
# Retornar:
#
# Calculadora.sumar(10, 5)
#
# Resultado esperado:
#
# 15

def ejercicio_1():
    pass


# =========================
# Ejercicio 2
# =========================
# Crear:
#
# class Calculadora:
#
#     @staticmethod
#     def restar(a, b):
#         return a - b
#
# Retornar:
#
# Calculadora.restar(10, 5)
#
# Resultado esperado:
#
# 5

def ejercicio_2():
    pass


# =========================
# Ejercicio 3
# =========================
# Crear:
#
# class Conversor:
#
#     @staticmethod
#     def metros_a_centimetros(metros):
#         return metros * 100
#
# Retornar:
#
# Conversor.metros_a_centimetros(2)
#
# Resultado esperado:
#
# 200

def ejercicio_3():
    pass


# =========================
# Ejercicio 4
# =========================
# Crear:
#
# class Validador:
#
#     @staticmethod
#     def es_mayor_de_edad(edad):
#         return edad >= 18
#
# Retornar:
#
# Validador.es_mayor_de_edad(20)
#
# Resultado esperado:
#
# True

def ejercicio_4():
    pass


# =========================
# Ejercicio 5
# =========================
# Crear:
#
# class Usuario:
#
#     cantidad = 5
#
#     @classmethod
#     def mostrar_cantidad(cls):
#         return cls.cantidad
#
# Retornar:
#
# Usuario.mostrar_cantidad()
#
# Resultado esperado:
#
# 5

def ejercicio_5():
    pass


# =========================
# Ejercicio 6
# =========================
# Crear:
#
# class Producto:
#
#     iva = 21
#
#     @classmethod
#     def mostrar_iva(cls):
#         return cls.iva
#
# Retornar:
#
# Producto.mostrar_iva()
#
# Resultado esperado:
#
# 21

def ejercicio_6():
    pass


# =========================
# Ejercicio 7
# =========================
# Crear:
#
# class Configuracion:
#
#     modo = "Producción"
#
#     @classmethod
#     def mostrar_modo(cls):
#         return cls.modo
#
# Retornar:
#
# Configuracion.mostrar_modo()
#
# Resultado esperado:
#
# "Producción"

def ejercicio_7():
    pass


# =========================
# Ejercicio 8
# =========================
# Crear:
#
# class Texto:
#
#     @staticmethod
#     def convertir_mayusculas(texto):
#         return texto.upper()
#
# Retornar:
#
# Texto.convertir_mayusculas("python")
#
# Resultado esperado:
#
# "PYTHON"

def ejercicio_8():
    pass


# =========================
# Ejercicio 9
# =========================
# Crear:
#
# class Sistema:
#
#     nombre = "Python Desde Cero"
#
#     @classmethod
#     def mostrar_nombre(cls):
#         return cls.nombre
#
# Retornar:
#
# Sistema.mostrar_nombre()
#
# Resultado esperado:
#
# "Python Desde Cero"

def ejercicio_9():
    pass


# =========================
# Ejercicio 10
# =========================
# Crear:
#
# class Herramienta:
#
#     version = "1.0"
#
#     @staticmethod
#     def saludar():
#         return "Hola"
#
#     @classmethod
#     def mostrar_version(cls):
#         return cls.version
#
# Retornar:
#
# Herramienta.saludar() + " " + Herramienta.mostrar_version()
#
# Resultado esperado:
#
# "Hola 1.0"

def ejercicio_10():
    pass