import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARCHIVOS_DIR = os.path.join(BASE_DIR, "archivos")

os.makedirs(ARCHIVOS_DIR, exist_ok=True)


def ruta_archivo(nombre):
    return os.path.join(ARCHIVOS_DIR, nombre)


def ejercicio_1():
    with open(ruta_archivo("saludo.txt"), "w", encoding="utf-8") as archivo:
        archivo.write("Hola mundo")

    return "Archivo creado"


def ejercicio_2():
    with open(ruta_archivo("saludo.txt"), "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    return contenido


def ejercicio_3():
    with open(ruta_archivo("datos.txt"), "w", encoding="utf-8") as archivo:
        archivo.write("Python desde cero")

    return "Datos guardados"


def ejercicio_4():
    with open(ruta_archivo("datos.txt"), "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    return contenido


def ejercicio_5():
    with open(ruta_archivo("notas.txt"), "w", encoding="utf-8") as archivo:
        archivo.write("Primera línea")

    with open(ruta_archivo("notas.txt"), "a", encoding="utf-8") as archivo:
        archivo.write("\nSegunda línea")

    with open(ruta_archivo("notas.txt"), "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    return contenido


def ejercicio_6():
    with open(
        ruta_archivo("alumnos.csv"),
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(["nombre", "edad"])
        escritor.writerow(["Ana", "25"])
        escritor.writerow(["Luis", "30"])

    return "CSV creado"


def ejercicio_7():
    filas = []

    with open(ruta_archivo("alumnos.csv"), "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            filas.append(fila)

    return filas


def ejercicio_8():
    with open(
        ruta_archivo("productos.csv"),
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(["producto", "precio"])
        escritor.writerow(["Mouse", "500"])
        escritor.writerow(["Teclado", "1000"])

    return "Productos guardados"


def ejercicio_9():
    filas = []

    with open(ruta_archivo("productos.csv"), "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            filas.append(fila)

    return filas


def ejercicio_10():
    with open(ruta_archivo("resumen.txt"), "w", encoding="utf-8") as archivo:
        archivo.write("Módulo de archivos completado")

    with open(ruta_archivo("resumen.txt"), "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    return contenido