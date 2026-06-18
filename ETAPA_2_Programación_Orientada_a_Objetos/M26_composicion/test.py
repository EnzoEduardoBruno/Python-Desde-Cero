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

        faltantes = validar_requisitos(
            codigo,
            requisitos
        )

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
    "Motor encendido",
    [
        "class Motor",
        "class Auto",
        "self.motor = Motor()",
        "auto.motor.arrancar()"
    ]
)


# =========================
# Ejercicio 2
# =========================

validar(
    2,
    practica.ejercicio_2,
    "Ryzen 7",
    [
        "class Procesador",
        "class Computadora",
        "self.procesador = Procesador()",
        "pc.procesador.informacion()"
    ]
)


# =========================
# Ejercicio 3
# =========================

validar(
    3,
    practica.ejercicio_3,
    "Ana",
    [
        "class Profesor",
        "class Curso",
        "self.profesor = profesor",
        "curso.profesor.nombre"
    ]
)


# =========================
# Ejercicio 4
# =========================

validar(
    4,
    practica.ejercicio_4,
    "Juan",
    [
        "class Alumno",
        "class Curso",
        "self.alumno = alumno",
        "curso.alumno.nombre"
    ]
)


# =========================
# Ejercicio 5
# =========================

validar(
    5,
    practica.ejercicio_5,
    "Batería cargada",
    [
        "class Bateria",
        "class Celular",
        "self.bateria = Bateria()",
        "celular.bateria.estado()"
    ]
)


# =========================
# Ejercicio 6
# =========================

validar(
    6,
    practica.ejercicio_6,
    "Córdoba",
    [
        "class Direccion",
        "class Persona",
        "self.direccion = direccion",
        "persona.direccion.ciudad"
    ]
)


# =========================
# Ejercicio 7
# =========================

validar(
    7,
    practica.ejercicio_7,
    "Mostrando imagen",
    [
        "class Pantalla",
        "class Televisor",
        "self.pantalla = Pantalla()",
        "televisor.pantalla.mostrar()"
    ]
)


# =========================
# Ejercicio 8
# =========================

validar(
    8,
    practica.ejercicio_8,
    "Guido",
    [
        "class Autor",
        "class Libro",
        "self.autor = autor",
        "libro.autor.nombre"
    ]
)


# =========================
# Ejercicio 9
# =========================

validar(
    9,
    practica.ejercicio_9,
    "Escribiendo",
    [
        "class Teclado",
        "class Notebook",
        "self.teclado = Teclado()",
        "notebook.teclado.escribir()"
    ]
)


# =========================
# Ejercicio 10
# =========================

validar(
    10,
    practica.ejercicio_10,
    "BeeSoftware",
    [
        "class Empresa",
        "class Empleado",
        "self.empresa = empresa",
        "empleado.empresa.nombre"
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