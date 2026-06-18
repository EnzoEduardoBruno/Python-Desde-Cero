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
    "Ana",
    [
        "@dataclass",
        "class Persona",
        "nombre: str",
        "edad: int",
        'Persona("Ana", 20)'
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    1500,
    [
        "@dataclass",
        "class Producto",
        "nombre: str",
        "precio: int",
        'Producto("Mouse", 1500)'
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    8,
    [
        "@dataclass",
        "class Alumno",
        "nombre: str",
        "nota: int",
        'Alumno("Juan", 8)'
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Guido",
    [
        "@dataclass",
        "class Libro",
        "titulo: str",
        "autor: str",
        'Libro("Python", "Guido")'
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    "admin@mail.com",
    [
        "@dataclass",
        "class Usuario",
        "nombre: str",
        "email: str",
        'Usuario("Admin", "admin@mail.com")'
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "Guau",
    [
        "class Perro",
        "class Gato",
        "def hablar",
        "def hacer_hablar",
        "animal.hablar()"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Auto moviéndose",
    [
        "class Auto",
        "class Barco",
        "def mover",
        "def iniciar_movimiento",
        "objeto.mover()"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Imprimiendo",
    [
        "class Impresora",
        "class Pantalla",
        "def mostrar",
        "def ejecutar",
        "objeto.mostrar()"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    1000,
    [
        "@dataclass",
        "class Cuenta",
        "titular: str",
        "saldo: int",
        'Cuenta("Ana", 1000)'
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "Hola mundo",
    [
        "@dataclass",
        "class Mensaje",
        "texto: str",
        "class Notificador",
        "def enviar",
        "mensaje.texto"
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