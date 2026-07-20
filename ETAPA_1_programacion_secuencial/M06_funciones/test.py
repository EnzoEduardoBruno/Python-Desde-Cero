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


try:
    validar(1, ejercicio_1(), "Hola")
except Exception as error:
    incorrecto(1, error)


try:
    validar(2, ejercicio_2("Enzo"), "Enzo")
except Exception as error:
    incorrecto(2, error)


try:
    validar(3, ejercicio_3(10, 5), 15)
except Exception as error:
    incorrecto(3, error)


try:
    validar(4, ejercicio_4(10, 5), 50)
except Exception as error:
    incorrecto(4, error)


try:
    validar(5, ejercicio_5(), True)
except Exception as error:
    incorrecto(5, error)


try:
    validar(6, ejercicio_6(), False)
except Exception as error:
    incorrecto(6, error)


try:
    validar(7, ejercicio_7(20), "Mayor")
except Exception as error:
    incorrecto(7, error)


try:
    validar(8, ejercicio_8("Hola ", "Python"), "Hola Python")
except Exception as error:
    incorrecto(8, error)


try:
    validar(9, ejercicio_9("Enzo"), "Hola Enzo")
except Exception as error:
    incorrecto(9, error)


try:
    resultado = ejercicio_10()

    if resultado is not None:
        correcto(10)

    else:
        incorrecto(10, "Debe retornar algún valor.")

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
