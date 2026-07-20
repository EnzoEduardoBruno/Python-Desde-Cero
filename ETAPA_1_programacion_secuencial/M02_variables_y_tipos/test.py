from practica import *

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


def validar_string(numero, resultado):
    if isinstance(resultado, str) and len(resultado.strip()) > 0:
        correcto(numero)
    else:
        incorrecto(numero, "Debe retornar un texto no vacío.")


# =========================
# Ejercicio 1
# =========================

try:
    validar_string(1, ejercicio_1())

except Exception as error:
    incorrecto(1, error)


# =========================
# Ejercicio 2
# =========================

try:
    resultado = ejercicio_2()

    if isinstance(resultado, int) and not isinstance(resultado, bool):
        correcto(2)
    else:
        incorrecto(2, "Debe retornar un número entero.")

except Exception as error:
    incorrecto(2, error)


# =========================
# Ejercicio 3
# =========================

try:
    resultado = ejercicio_3()

    if isinstance(resultado, float):
        correcto(3)
    else:
        incorrecto(3, "Debe retornar un número decimal.")

except Exception as error:
    incorrecto(3, error)


# =========================
# Ejercicio 4
# =========================

try:
    resultado = ejercicio_4()

    if isinstance(resultado, bool):
        correcto(4)
    else:
        incorrecto(4, "Debe retornar True o False.")

except Exception as error:
    incorrecto(4, error)


# =========================
# Ejercicio 5
# =========================

try:
    validar_string(5, ejercicio_5())

except Exception as error:
    incorrecto(5, error)


# =========================
# Ejercicio 6
# =========================

try:
    validar_string(6, ejercicio_6())

except Exception as error:
    incorrecto(6, error)


# =========================
# Ejercicio 7
# =========================

try:
    validar_string(7, ejercicio_7())

except Exception as error:
    incorrecto(7, error)


# =========================
# Ejercicio 8
# =========================

try:
    validar_string(8, ejercicio_8())

except Exception as error:
    incorrecto(8, error)


# =========================
# Ejercicio 9
# =========================

try:
    resultado = ejercicio_9()

    if (
        isinstance(resultado, str)
        or isinstance(resultado, int)
        or isinstance(resultado, float)
        or isinstance(resultado, bool)
    ):
        correcto(9)
    else:
        incorrecto(9)

except Exception as error:
    incorrecto(9, error)


# =========================
# Ejercicio 10
# =========================

try:
    resultado = ejercicio_10()

    if (
        isinstance(resultado, str)
        or isinstance(resultado, int)
        or isinstance(resultado, float)
        or isinstance(resultado, bool)
    ):
        correcto(10)
    else:
        incorrecto(10)

except Exception as error:
    incorrecto(10, error)


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
