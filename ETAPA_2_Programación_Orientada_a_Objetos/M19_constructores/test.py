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
        "nombre",
        "self.nombre",
        'Persona("Ana")',
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
        "marca",
        "self.marca",
        'Auto("Toyota")',
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
        "nombre",
        "self.nombre",
        'Perro("Firulais")',
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
        "nombre",
        "edad",
        "self.nombre",
        "self.edad",
        'Alumno("Ana", 20)',
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
        "nombre",
        "precio",
        "self.nombre",
        "self.precio",
        'Producto("Mouse", 1500)',
        "producto.precio"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "A54",
    [
        "class Celular",
        "__init__",
        "marca",
        "modelo",
        "self.marca",
        "self.modelo",
        'Celular("Samsung", "A54")',
        "celular.modelo"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Guido",
    [
        "class Libro",
        "__init__",
        "titulo",
        "autor",
        "self.titulo",
        "self.autor",
        'Libro("Python", "Guido")',
        "libro.autor"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Ciencia ficción",
    [
        "class Pelicula",
        "__init__",
        "titulo",
        "genero",
        "self.titulo",
        "self.genero",
        'Pelicula("Matrix", "Ciencia ficción")',
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
        "titular",
        "saldo",
        "self.titular",
        "self.saldo",
        'Cuenta("Ana", 1000)',
        "cuenta.saldo"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "administrador",
    [
        "class Usuario",
        "__init__",
        "nombre",
        "email",
        "rol",
        "self.nombre",
        "self.email",
        "self.rol",
        "Usuario(",
        "usuario.rol"
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