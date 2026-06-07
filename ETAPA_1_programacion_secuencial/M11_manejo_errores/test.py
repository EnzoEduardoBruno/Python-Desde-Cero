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


def contiene(codigo, texto):
    return texto in codigo


def validar(numero, funcion, esperado, requisitos):
    try:
        codigo = obtener_codigo(funcion)
        resultado = funcion()

        errores = []

        if resultado != esperado:
            errores.append(f"Esperado: {esperado} | Recibido: {resultado}")

        for requisito in requisitos:
            if requisito not in codigo:
                errores.append(f"Falta usar: {requisito}")

        if len(errores) == 0:
            correcto(numero)
        else:
            incorrecto(numero, " | ".join(errores))

    except Exception as error:
        incorrecto(numero, error)


validar(
    1,
    practica.ejercicio_1,
    10,
    ["try", "except", "int("]
)

validar(
    2,
    practica.ejercicio_2,
    "Error",
    ["try", "except", "int("]
)

validar(
    3,
    practica.ejercicio_3,
    5.0,
    ["try", "except", "/"]
)

validar(
    4,
    practica.ejercicio_4,
    "No se puede dividir por cero",
    ["try", "except", "ZeroDivisionError", "/"]
)

validar(
    5,
    practica.ejercicio_5,
    "Valor inválido",
    ["try", "except", "ValueError", "int("]
)

validar(
    6,
    practica.ejercicio_6,
    "División inválida",
    ["try", "except", "ZeroDivisionError", "/"]
)

validar(
    7,
    practica.ejercicio_7,
    "Finalizado",
    ["try", "except", "finally"]
)

validar(
    8,
    practica.ejercicio_8,
    "Finalizado",
    ["try", "except", "finally", "int("]
)

validar(
    9,
    practica.ejercicio_9,
    "Índice inválido",
    ["try", "except", "IndexError"]
)

validar(
    10,
    practica.ejercicio_10,
    "Clave inexistente",
    ["try", "except", "KeyError"]
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