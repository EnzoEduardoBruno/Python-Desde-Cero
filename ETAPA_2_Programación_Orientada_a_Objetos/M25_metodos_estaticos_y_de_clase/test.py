import inspect
import practica

puntaje = 0
total = 10

print("\n🧪 Corrigiendo ejercicios...\n")


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


def validar(numero, funcion, esperado, requisitos):

    try:

        codigo = obtener_codigo(funcion)

        resultado = funcion()

        errores = []

        if resultado != esperado:

            errores.append(
                f"Esperado: {esperado} | Recibido: {resultado}"
            )

        faltantes = validar_requisitos(
            codigo,
            requisitos
        )

        for faltante in faltantes:

            errores.append(
                f"Falta usar: {faltante}"
            )

        if len(errores) == 0:

            correcto(numero)

        else:

            incorrecto(
                numero,
                " | ".join(errores)
            )

    except Exception as error:

        incorrecto(numero, error)


# =========================
# Ejercicio 1
# =========================

validar(
    1,
    practica.ejercicio_1,
    15,
    [
        "@staticmethod",
        "class Calculadora",
        "def sumar",
        "Calculadora.sumar"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    5,
    [
        "@staticmethod",
        "class Calculadora",
        "def restar",
        "Calculadora.restar"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    200,
    [
        "@staticmethod",
        "class Conversor",
        "def metros_a_centimetros",
        "Conversor.metros_a_centimetros"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    True,
    [
        "@staticmethod",
        "class Validador",
        "def es_mayor_de_edad",
        "Validador.es_mayor_de_edad"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    5,
    [
        "@classmethod",
        "class Usuario",
        "cantidad",
        "cls.cantidad",
        "Usuario.mostrar_cantidad"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    21,
    [
        "@classmethod",
        "class Producto",
        "iva",
        "cls.iva",
        "Producto.mostrar_iva"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Producción",
    [
        "@classmethod",
        "class Configuracion",
        "modo",
        "cls.modo",
        "Configuracion.mostrar_modo"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "PYTHON",
    [
        "@staticmethod",
        "class Texto",
        "def convertir_mayusculas",
        "Texto.convertir_mayusculas"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    "Python Desde Cero",
    [
        "@classmethod",
        "class Sistema",
        "nombre",
        "cls.nombre",
        "Sistema.mostrar_nombre"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "Hola 1.0",
    [
        "@staticmethod",
        "@classmethod",
        "class Herramienta",
        "version",
        "cls.version",
        "Herramienta.saludar",
        "Herramienta.mostrar_version"
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