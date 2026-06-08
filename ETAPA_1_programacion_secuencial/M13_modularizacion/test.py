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


def validar(numero, funcion, esperado, requisitos):
    try:
        codigo = obtener_codigo(funcion)
        resultado = funcion()

        errores = []

        if resultado != esperado:
            errores.append(
                f"Esperado: {esperado} | Recibido: {resultado}"
            )

        for requisito in requisitos:
            if requisito not in codigo:
                errores.append(
                    f"Falta usar: {requisito}"
                )

        if len(errores) == 0:
            correcto(numero)
        else:
            incorrecto(numero, " | ".join(errores))

    except Exception as error:
        incorrecto(numero, error)


validar(
    1,
    practica.ejercicio_1,
    5.0,
    ["import math", "math.sqrt"]
)

validar(
    2,
    practica.ejercicio_2,
    6.0,
    ["from math import sqrt", "sqrt("]
)

validar(
    3,
    practica.ejercicio_3,
    8.0,
    ["import math as m", "m.pow"]
)

validar(
    4,
    practica.ejercicio_4,
    15,
    [
        "from utilidades.matematicas import sumar",
        "sumar("
    ]
)

validar(
    5,
    practica.ejercicio_5,
    "Hola",
    [
        "from utilidades.textos import saludar",
        "saludar("
    ]
)

validar(
    6,
    practica.ejercicio_6,
    25,
    [
        "from utilidades.matematicas import sumar",
        "from utilidades.matematicas import multiplicar"
    ]
)

validar(
    7,
    practica.ejercicio_7,
    3.14,
    [
        "from math import pi",
        "round("
    ]
)

validar(
    8,
    practica.ejercicio_8,
    True,
    [
        "import random",
        "randint"
    ]
)

validar(
    9,
    practica.ejercicio_9,
    20,
    [
        "from utilidades.matematicas import multiplicar",
        "multiplicar("
    ]
)

validar(
    10,
    practica.ejercicio_10,
    "Módulo completado",
    [
        "import",
        "from",
        "as"
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