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
    "Ana",
    [
        "class Persona",
        "__init__",
        "self.nombre",
        "Persona()",
        "persona.nombre"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    "Toyota",
    [
        "class Auto",
        "__init__",
        "self.marca",
        "Auto()",
        "auto.marca"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    "Firulais",
    [
        "class Perro",
        "__init__",
        "self.nombre",
        "Perro()",
        "perro.nombre"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    20,
    [
        "class Alumno",
        "__init__",
        "self.edad",
        "Alumno()",
        "alumno.edad"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    1500,
    [
        "class Producto",
        "__init__",
        "self.precio",
        "Producto()",
        "producto.precio"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "Samsung",
    [
        "class Celular",
        "__init__",
        "self.modelo",
        "Celular()",
        "celular.modelo"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Python",
    [
        "class Libro",
        "__init__",
        "self.titulo",
        "Libro()",
        "libro.titulo"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Acción",
    [
        "class Pelicula",
        "__init__",
        "self.genero",
        "Pelicula()",
        "pelicula.genero"
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
        "class Cuenta",
        "__init__",
        "self.saldo",
        "Cuenta()",
        "cuenta.saldo"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "Admin",
    [
        "class Usuario",
        "__init__",
        "self.nombre",
        "Usuario()",
        "usuario.nombre"
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