# M12 - Archivos
# Completar cada ejercicio.
#
# Importante:
# - No cambiar el nombre de las funciones.
# - Borrar pass y escribir la solución.
# - Usar return para devolver resultados.
# - Todos los archivos deben guardarse dentro de la carpeta "archivos".

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARCHIVOS_DIR = os.path.join(BASE_DIR, "archivos")

os.makedirs(ARCHIVOS_DIR, exist_ok=True)


def ruta_archivo(nombre):
    return os.path.join(ARCHIVOS_DIR, nombre)


# =========================
# Ejercicio 1
# =========================
# Crear el archivo:
#
# archivos/saludo.txt
#
# Escribir:
#
# Hola mundo
#
# Retornar:
# "Archivo creado"

def ejercicio_1():
    pass


# =========================
# Ejercicio 2
# =========================
# Leer el archivo:
#
# archivos/saludo.txt
#
# Retornar su contenido.

def ejercicio_2():
    pass


# =========================
# Ejercicio 3
# =========================
# Crear el archivo:
#
# archivos/datos.txt
#
# Escribir:
#
# Python desde cero
#
# Retornar:
# "Datos guardados"

def ejercicio_3():
    pass


# =========================
# Ejercicio 4
# =========================
# Leer el archivo:
#
# archivos/datos.txt
#
# Retornar su contenido.

def ejercicio_4():
    pass


# =========================
# Ejercicio 5
# =========================
# Crear el archivo:
#
# archivos/notas.txt
#
# Escribir:
# Primera línea
#
# Luego agregar:
# Segunda línea
#
# usando modo append "a".
#
# Retornar el contenido completo del archivo.

def ejercicio_5():
    pass


# =========================
# Ejercicio 6
# =========================
# Crear el archivo:
#
# archivos/alumnos.csv
#
# Con estas filas:
#
# nombre,edad
# Ana,25
# Luis,30
#
# Retornar:
# "CSV creado"

def ejercicio_6():
    pass


# =========================
# Ejercicio 7
# =========================
# Leer el archivo:
#
# archivos/alumnos.csv
#
# Retornar una lista con sus filas.

def ejercicio_7():
    pass


# =========================
# Ejercicio 8
# =========================
# Crear el archivo:
#
# archivos/productos.csv
#
# Con estas filas:
#
# producto,precio
# Mouse,500
# Teclado,1000
#
# Retornar:
# "Productos guardados"

def ejercicio_8():
    pass


# =========================
# Ejercicio 9
# =========================
# Leer el archivo:
#
# archivos/productos.csv
#
# Retornar una lista con sus filas.

def ejercicio_9():
    pass


# =========================
# Ejercicio 10
# =========================
# Crear el archivo:
#
# archivos/resumen.txt
#
# Escribir:
# Módulo de archivos completado
#
# Leer el archivo y retornar su contenido.

def ejercicio_10():
    pass