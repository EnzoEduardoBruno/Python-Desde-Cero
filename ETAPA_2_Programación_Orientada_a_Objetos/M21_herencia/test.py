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
    "Respirando",
    [
        "class Animal",
        "class Perro(Animal)",
        "def respirar",
        "Perro()",
        "perro.respirar()"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    "Motor encendido",
    [
        "class Vehiculo",
        "class Auto(Vehiculo)",
        "def arrancar",
        "Auto()",
        "auto.arrancar()"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    "Ana",
    [
        "class Persona",
        "class Alumno(Persona)",
        "self.nombre",
        "Alumno()",
        "alumno.nombre"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Comiendo",
    [
        "class Animal",
        "class Gato(Animal)",
        "def comer",
        "Gato()",
        "gato.comer()"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    "Encendido",
    [
        "class Dispositivo",
        "class Celular(Dispositivo)",
        "def encender",
        "Celular()",
        "celular.encender()"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "Trabajando",
    [
        "class Empleado",
        "class Programador(Empleado)",
        "def trabajar",
        "Programador()",
        "programador.trabajar()"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Saldo disponible",
    [
        "class Cuenta",
        "class CuentaCorriente(Cuenta)",
        "def consultar",
        "CuentaCorriente()",
        "cuenta.consultar()"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Leyendo",
    [
        "class Libro",
        "class Manual(Libro)",
        "def leer",
        "Manual()",
        "manual.leer()"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    "Hola",
    [
        "class Persona",
        "class Profesor(Persona)",
        "def saludar",
        "Profesor()",
        "profesor.saludar()"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "Avanzando",
    [
        "class Vehiculo",
        "class Moto(Vehiculo)",
        "def avanzar",
        "Moto()",
        "moto.avanzar()"
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