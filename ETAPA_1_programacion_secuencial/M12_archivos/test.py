import csv
import inspect
import os
import practica

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARCHIVOS_DIR = os.path.join(BASE_DIR, "archivos")

os.makedirs(ARCHIVOS_DIR, exist_ok=True)

puntaje = 0
total = 10

print("\n🧪 Corrigiendo ejercicios...\n")


def ruta_archivo(nombre):
    return os.path.join(ARCHIVOS_DIR, nombre)


def correcto(numero):
    global puntaje
    print(f"✅ Ejercicio {numero} correcto")
    puntaje += 1


def incorrecto(numero, detalle=""):
    print(f"❌ Ejercicio {numero} incorrecto")

    if detalle:
        print(f"   {detalle}")


def obtener_codigo(funcion):
    return inspect.getsource(funcion)


def validar_requisitos(codigo, requisitos):
    faltantes = []

    for requisito in requisitos:
        if requisito not in codigo:
            faltantes.append(requisito)

    return faltantes


def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)


def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


def validar(numero, funcion, esperado, requisitos):
    try:
        codigo = obtener_codigo(funcion)
        resultado = funcion()

        errores = []

        if resultado != esperado:
            errores.append(f"Esperado: {esperado} | Recibido: {resultado}")

        faltantes = validar_requisitos(codigo, requisitos)

        for faltante in faltantes:
            errores.append(f"Falta usar: {faltante}")

        if len(errores) == 0:
            correcto(numero)
        else:
            incorrecto(numero, " | ".join(errores))

    except Exception as error:
        incorrecto(numero, error)


# =========================
# Ejercicio 1
# =========================

eliminar_archivo(ruta_archivo("saludo.txt"))

validar(
    1,
    practica.ejercicio_1,
    "Archivo creado",
    ['with open', 'ruta_archivo("saludo.txt")', '"w"', "write"]
)

try:
    contenido = leer_archivo(ruta_archivo("saludo.txt"))

    if contenido != "Hola mundo":
        incorrecto(
            1,
            "El archivo archivos/saludo.txt no contiene el texto esperado."
        )

except Exception as error:
    incorrecto(1, error)


# =========================
# Ejercicio 2
# =========================

with open(ruta_archivo("saludo.txt"), "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo")

validar(
    2,
    practica.ejercicio_2,
    "Hola mundo",
    ['with open', 'ruta_archivo("saludo.txt")', '"r"', "read"]
)


# =========================
# Ejercicio 3
# =========================

eliminar_archivo(ruta_archivo("datos.txt"))

validar(
    3,
    practica.ejercicio_3,
    "Datos guardados",
    ['with open', 'ruta_archivo("datos.txt")', '"w"', "write"]
)

try:
    contenido = leer_archivo(ruta_archivo("datos.txt"))

    if contenido != "Python desde cero":
        incorrecto(
            3,
            "El archivo archivos/datos.txt no contiene el texto esperado."
        )

except Exception as error:
    incorrecto(3, error)


# =========================
# Ejercicio 4
# =========================

with open(ruta_archivo("datos.txt"), "w", encoding="utf-8") as archivo:
    archivo.write("Python desde cero")

validar(
    4,
    practica.ejercicio_4,
    "Python desde cero",
    ['with open', 'ruta_archivo("datos.txt")', '"r"', "read"]
)


# =========================
# Ejercicio 5
# =========================

eliminar_archivo(ruta_archivo("notas.txt"))

validar(
    5,
    practica.ejercicio_5,
    "Primera línea\nSegunda línea",
    [
        "with open",
        'ruta_archivo("notas.txt")',
        '"w"',
        '"a"',
        '"r"',
        "write",
        "read"
    ]
)


# =========================
# Ejercicio 6
# =========================

eliminar_archivo(ruta_archivo("alumnos.csv"))

validar(
    6,
    practica.ejercicio_6,
    "CSV creado",
    [
        "with open",
        'ruta_archivo("alumnos.csv")',
        '"w"',
        "csv.writer",
        "writerow"
    ]
)


# =========================
# Ejercicio 7
# =========================

with open(
    ruta_archivo("alumnos.csv"),
    "w",
    encoding="utf-8",
    newline=""
) as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", "25"])
    escritor.writerow(["Luis", "30"])

validar(
    7,
    practica.ejercicio_7,
    [["nombre", "edad"], ["Ana", "25"], ["Luis", "30"]],
    [
        "with open",
        'ruta_archivo("alumnos.csv")',
        '"r"',
        "csv.reader"
    ]
)


# =========================
# Ejercicio 8
# =========================

eliminar_archivo(ruta_archivo("productos.csv"))

validar(
    8,
    practica.ejercicio_8,
    "Productos guardados",
    [
        "with open",
        'ruta_archivo("productos.csv")',
        '"w"',
        "csv.writer",
        "writerow"
    ]
)


# =========================
# Ejercicio 9
# =========================

with open(
    ruta_archivo("productos.csv"),
    "w",
    encoding="utf-8",
    newline=""
) as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["producto", "precio"])
    escritor.writerow(["Mouse", "500"])
    escritor.writerow(["Teclado", "1000"])

validar(
    9,
    practica.ejercicio_9,
    [["producto", "precio"], ["Mouse", "500"], ["Teclado", "1000"]],
    [
        "with open",
        'ruta_archivo("productos.csv")',
        '"r"',
        "csv.reader"
    ]
)


# =========================
# Ejercicio 10
# =========================

eliminar_archivo(ruta_archivo("resumen.txt"))

validar(
    10,
    practica.ejercicio_10,
    "Módulo de archivos completado",
    [
        "with open",
        'ruta_archivo("resumen.txt")',
        '"w"',
        '"r"',
        "write",
        "read"
    ]
)


print("\n---------------------------")
print(f"🎯 Resultado final: {puntaje}/{total}")

if puntaje == total:
    print("🏆 ¡Excelente trabajo!")

elif puntaje >= 7:
    print("👍 ¡Muy bien!")

elif puntaje >= 4:
    print("🙂 Vas bien, seguí practicando.")

else:
    print("📚 Seguí practicando, es parte del proceso.")