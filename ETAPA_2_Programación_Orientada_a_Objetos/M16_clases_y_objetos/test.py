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
            incorrecto(numero, " | ".join(errores))

    except Exception as error:
        incorrecto(numero, error)


validar(
    1,
    practica.ejercicio_1,
    "Persona",
    [
        "class Persona",
        "Persona()",
        "type(",
        ".__name__"
    ]
)

validar(
    2,
    practica.ejercicio_2,
    2,
    [
        "class Auto",
        "Auto()"
    ]
)

validar(
    3,
    practica.ejercicio_3,
    3,
    [
        "class Perro",
        "Perro()"
    ]
)

validar(
    4,
    practica.ejercicio_4,
    True,
    [
        "class Alumno",
        "Alumno()"
    ]
)

validar(
    5,
    practica.ejercicio_5,
    "Producto",
    [
        "class Producto",
        "Producto()",
        "type(",
        ".__name__"
    ]
)

validar(
    6,
    practica.ejercicio_6,
    2,
    [
        "class Celular",
        "Celular()"
    ]
)

validar(
    7,
    practica.ejercicio_7,
    4,
    [
        "class Libro",
        "Libro()"
    ]
)

validar(
    8,
    practica.ejercicio_8,
    "Pelicula",
    [
        "class Pelicula",
        "Pelicula()",
        "type(",
        ".__name__"
    ]
)

validar(
    9,
    practica.ejercicio_9,
    2,
    [
        "class Cuenta",
        "Cuenta()"
    ]
)

validar(
    10,
    practica.ejercicio_10,
    5,
    [
        "class Usuario",
        "Usuario()"
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