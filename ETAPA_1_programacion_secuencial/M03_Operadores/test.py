from ETAPA_1_programacion_secuencial.M03_Operadores.practica import *

puntaje = 0
total = 13

print("\n🧪 Corrigiendo ejercicios...\n")


def correcto(numero):
    global puntaje

    print(f"✅ Ejercicio {numero} correcto")
    puntaje += 1


def incorrecto(numero, detalle=""):
    print(f"❌ Ejercicio {numero} incorrecto")

    if detalle:
        print(f"   {detalle}")


def es_numero(valor):
    return (isinstance(valor, int) or isinstance(valor, float)) and not isinstance(valor, bool)


def validar_numero(numero, resultado):
    if es_numero(resultado):
        correcto(numero)
    else:
        incorrecto(numero, "Debe retornar un resultado numérico.")


def validar_booleano(numero, resultado):
    if isinstance(resultado, bool):
        correcto(numero)
    else:
        incorrecto(numero, "Debe retornar True o False.")


# Ejercicio 1
try:
    validar_numero(1, ejercicio_1())
except Exception as error:
    incorrecto(1, error)


# Ejercicio 2
try:
    validar_numero(2, ejercicio_2())
except Exception as error:
    incorrecto(2, error)


# Ejercicio 3
try:
    validar_numero(3, ejercicio_3())
except Exception as error:
    incorrecto(3, error)


# Ejercicio 4
try:
    validar_numero(4, ejercicio_4())
except Exception as error:
    incorrecto(4, error)


# Ejercicio 5
try:
    resultado = ejercicio_5()

    if isinstance(resultado, int) and not isinstance(resultado, bool):
        correcto(5)
    else:
        incorrecto(5, "Debe retornar un número entero usando división entera.")
except Exception as error:
    incorrecto(5, error)


# Ejercicio 6
try:
    resultado = ejercicio_6()

    if isinstance(resultado, int) and not isinstance(resultado, bool):
        correcto(6)
    else:
        incorrecto(6, "Debe retornar el resto de una división.")
except Exception as error:
    incorrecto(6, error)


# Ejercicio 7
try:
    validar_numero(7, ejercicio_7())
except Exception as error:
    incorrecto(7, error)


# Ejercicio 8
try:
    validar_booleano(8, ejercicio_8())
except Exception as error:
    incorrecto(8, error)


# Ejercicio 9
try:
    validar_booleano(9, ejercicio_9())
except Exception as error:
    incorrecto(9, error)


# Ejercicio 10
try:
    validar_booleano(10, ejercicio_10())
except Exception as error:
    incorrecto(10, error)


# Ejercicio 11
try:
    validar_booleano(11, ejercicio_11())
except Exception as error:
    incorrecto(11, error)


# Ejercicio 12
try:
    validar_booleano(12, ejercicio_12())
except Exception as error:
    incorrecto(12, error)


# Ejercicio 13
try:
    validar_booleano(13, ejercicio_13())
except Exception as error:
    incorrecto(13, error)


print("\n---------------------------")
print(f"🎯 Resultado final: {puntaje}/{total}")

if puntaje == total:
    print("🏆 ¡Excelente trabajo!")
elif puntaje >= 10:
    print("👍 ¡Muy bien!")
elif puntaje >= 6:
    print("🙂 Vas bien, seguí practicando.")
else:
    print("📚 Seguí practicando, es parte del proceso.")