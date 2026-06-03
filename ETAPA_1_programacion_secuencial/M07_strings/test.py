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


def validar(numero, resultado, esperado):
    if resultado == esperado:
        correcto(numero)
    else:
        incorrecto(
            numero,
            f"Esperado: {esperado} | Recibido: {resultado}"
        )


def validar_string(numero, resultado):
    if isinstance(resultado, str) and len(resultado.strip()) > 0:
        correcto(numero)
    else:
        incorrecto(numero, "Debe retornar un string no vacío.")


def validar_string_con_espacio(numero, resultado):
    if isinstance(resultado, str) and " " in resultado.strip():
        correcto(numero)
    else:
        incorrecto(numero, "Debe retornar un string con un espacio entre nombre y apellido.")


# Ejercicio 1
try:
    validar_string(1, ejercicio_1())
except Exception as error:
    incorrecto(1, error)


# Ejercicio 2
try:
    resultado = ejercicio_2()

    if isinstance(resultado, str) and resultado == resultado.upper():
        correcto(2)
    else:
        incorrecto(2, "Debe retornar un string en mayúsculas usando upper().")

except Exception as error:
    incorrecto(2, error)


# Ejercicio 3
try:
    resultado = ejercicio_3()

    if isinstance(resultado, str) and resultado == resultado.lower():
        correcto(3)
    else:
        incorrecto(3, "Debe retornar un string en minúsculas usando lower().")

except Exception as error:
    incorrecto(3, error)


# Ejercicio 4
try:
    validar(4, ejercicio_4(), "Pyt")
except Exception as error:
    incorrecto(4, error)


# Ejercicio 5
try:
    resultado = ejercicio_5()

    if isinstance(resultado, str) and len(resultado.strip()) > 0:
        correcto(5)
    else:
        incorrecto(5, "Debe retornar un saludo usando concatenación.")

except Exception as error:
    incorrecto(5, error)


# Ejercicio 6
try:
    resultado = ejercicio_6()

    if isinstance(resultado, str) and len(resultado.strip()) > 0:
        correcto(6)
    else:
        incorrecto(6, "Debe retornar un saludo usando f-string.")

except Exception as error:
    incorrecto(6, error)


# Ejercicio 7
try:
    validar(7, ejercicio_7(), "P")
except Exception as error:
    incorrecto(7, error)


# Ejercicio 8
try:
    validar(8, ejercicio_8(), "thon")
except Exception as error:
    incorrecto(8, error)


# Ejercicio 9
try:
    validar_string_con_espacio(9, ejercicio_9())
except Exception as error:
    incorrecto(9, error)


# Ejercicio 10
try:
    validar_string(10, ejercicio_10())
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