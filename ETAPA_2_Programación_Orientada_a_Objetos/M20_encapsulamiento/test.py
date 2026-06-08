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
    1000,
    [
        "class Cuenta",
        "self._saldo",
        "Cuenta()",
        "cuenta._saldo"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    "1234",
    [
        "class Usuario",
        "self.__clave",
        "Usuario()",
        "_Usuario__clave"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Corolla",
    [
        "class Auto",
        "self.marca",
        "self._modelo",
        "Auto()",
        "auto._modelo"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    100,
    [
        "class Alumno",
        "self.__legajo",
        "Alumno()",
        "_Alumno__legajo"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    50,
    [
        "class Producto",
        "self.nombre",
        "self._stock",
        "Producto()",
        "producto._stock"
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
        "self.__titulo",
        "Libro()",
        "_Libro__titulo"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    120,
    [
        "class Pelicula",
        "self.genero",
        "self._duracion",
        "Pelicula()",
        "pelicula._duracion"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    "ABC123",
    [
        "class Celular",
        "self.__imei",
        "Celular()",
        "_Celular__imei"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    1000,
    [
        "class CuentaBancaria",
        "self.titular",
        "self._saldo",
        "self.__clave",
        "CuentaBancaria()",
        "cuenta._saldo"
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