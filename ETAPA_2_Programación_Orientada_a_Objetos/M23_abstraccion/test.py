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

        faltantes = validar_requisitos(codigo, requisitos)

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
    "Guau",
    [
        "ABC",
        "@abstractmethod",
        "class Animal",
        "class Perro(Animal)",
        "def hablar",
        "Perro()",
        "perro.hablar()"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    "Circulando",
    [
        "ABC",
        "@abstractmethod",
        "class Vehiculo",
        "class Auto(Vehiculo)",
        "def mover",
        "Auto()",
        "auto.mover()"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    "Miau",
    [
        "ABC",
        "@abstractmethod",
        "class Animal",
        "class Gato(Animal)",
        "def hablar",
        "Gato()",
        "gato.hablar()"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Área calculada",
    [
        "ABC",
        "@abstractmethod",
        "class Figura",
        "class Cuadrado(Figura)",
        "def area",
        "Cuadrado()",
        "cuadrado.area()"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    "Programando",
    [
        "ABC",
        "@abstractmethod",
        "class Empleado",
        "class Programador(Empleado)",
        "def trabajar",
        "Programador()",
        "programador.trabajar()"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "Consultando saldo",
    [
        "ABC",
        "@abstractmethod",
        "class Cuenta",
        "class CuentaCorriente(Cuenta)",
        "def consultar",
        "CuentaCorriente()",
        "cuenta.consultar()"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Buenos días",
    [
        "ABC",
        "@abstractmethod",
        "class Persona",
        "class Profesor(Persona)",
        "def saludar",
        "Profesor()",
        "profesor.saludar()"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Encendido",
    [
        "ABC",
        "@abstractmethod",
        "class Dispositivo",
        "class Celular(Dispositivo)",
        "def encender",
        "Celular()",
        "celular.encender()"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    "Leyendo",
    [
        "ABC",
        "@abstractmethod",
        "class Libro",
        "class Manual(Libro)",
        "def leer",
        "Manual()",
        "manual.leer()"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "Pío pío",
    [
        "ABC",
        "@abstractmethod",
        "class Animal",
        "class Pajaro(Animal)",
        "def hablar",
        "Pajaro()",
        "pajaro.hablar()"
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