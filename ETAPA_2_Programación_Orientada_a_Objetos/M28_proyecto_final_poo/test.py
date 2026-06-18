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
    "Python desde cero",
    [
        "@dataclass",
        "class Libro",
        "titulo: str",
        "autor: str"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    0,
    [
        "class Biblioteca",
        "self.libros = []"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    1,
    [
        "class Biblioteca",
        "def agregar_libro",
        "self.libros.append"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Python desde cero",
    [
        "def buscar_libro",
        "for libro in self.libros",
        "libro.titulo"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    1000,
    [
        "class CuentaBancaria",
        "self.titular",
        "self.saldo"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    1500,
    [
        "def depositar",
        "self.saldo += monto"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Extracción realizada",
    [
        "def extraer",
        "if monto <= self.saldo",
        'return "Extracción realizada"'
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Juan",
    [
        "class Alumno",
        "self.nombre",
        "self.notas = []"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    [8],
    [
        "def agregar_nota",
        "self.notas.append"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    9.0,
    [
        "def calcular_promedio",
        "sum(self.notas)",
        "len(self.notas)"
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