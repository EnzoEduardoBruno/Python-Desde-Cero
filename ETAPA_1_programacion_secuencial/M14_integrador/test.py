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


def validar_ejercicio(numero, funcion, casos, requisitos):
    try:
        codigo = obtener_codigo(funcion)
        errores = []

        faltantes = validar_requisitos(codigo, requisitos)

        for faltante in faltantes:
            errores.append(f"Falta usar: {faltante}")

        for argumentos, esperado in casos:
            resultado = funcion(*argumentos)

            if resultado != esperado:
                errores.append(
                    f"Con argumentos {argumentos} esperaba {esperado}, pero recibió {resultado}"
                )

        if len(errores) == 0:
            correcto(numero)
        else:
            incorrecto(numero, " | ".join(errores))

    except Exception as error:
        incorrecto(numero, error)


# =========================
# Ejercicio 1
# =========================

validar_ejercicio(
    1,
    practica.ejercicio_1,
    [
        ((10, 5), 15),
        ((2, 3), 5),
    ],
    ["+"]
)


# =========================
# Ejercicio 2
# =========================

validar_ejercicio(
    2,
    practica.ejercicio_2,
    [
        ((10, 5), 5),
        ((20, 8), 12),
    ],
    ["-"]
)


# =========================
# Ejercicio 3
# =========================

validar_ejercicio(
    3,
    practica.ejercicio_3,
    [
        ((10, 5, "suma"), 15),
        ((10, 5, "resta"), 5),
        ((10, 5, "multiplicacion"), 50),
        ((10, 5, "division"), 2.0),
        ((10, 5, "potencia"), "Operación inválida"),
    ],
    ["if", "elif", "else"]
)


# =========================
# Ejercicio 4
# =========================

validar_ejercicio(
    4,
    practica.ejercicio_4,
    [
        ((10, 2), 5.0),
        ((10, 0), "No se puede dividir por cero"),
    ],
    ["try", "except", "ZeroDivisionError"]
)


# =========================
# Ejercicio 5
# =========================

validar_ejercicio(
    5,
    practica.ejercicio_5,
    [
        (
            ("Ana", "123456"),
            {
                "nombre": "Ana",
                "telefono": "123456"
            }
        ),
        (
            ("Luis", "789000"),
            {
                "nombre": "Luis",
                "telefono": "789000"
            }
        ),
    ],
    ["{", "nombre", "telefono"]
)


# =========================
# Ejercicio 6
# =========================

agenda = [
    {
        "nombre": "Ana",
        "telefono": "123456"
    },
    {
        "nombre": "Luis",
        "telefono": "789000"
    }
]

validar_ejercicio(
    6,
    practica.ejercicio_6,
    [
        (
            (agenda, "Luis"),
            {
                "nombre": "Luis",
                "telefono": "789000"
            }
        ),
        (
            (agenda, "Carlos"),
            "Contacto no encontrado"
        ),
    ],
    ["for", "if"]
)


# =========================
# Ejercicio 7
# =========================

validar_ejercicio(
    7,
    practica.ejercicio_7,
    [
        (
            (
                [
                    {
                        "nombre": "Ana",
                        "telefono": "123456"
                    }
                ],
                {
                    "nombre": "Luis",
                    "telefono": "789000"
                }
            ),
            [
                {
                    "nombre": "Ana",
                    "telefono": "123456"
                },
                {
                    "nombre": "Luis",
                    "telefono": "789000"
                }
            ]
        ),
    ],
    ["append"]
)


# =========================
# Ejercicio 8
# =========================

validar_ejercicio(
    8,
    practica.ejercicio_8,
    [
        (([8, 9, 10],), 9.0),
        (([6, 6, 6],), 6.0),
    ],
    ["for", "len"]
)


# =========================
# Ejercicio 9
# =========================

validar_ejercicio(
    9,
    practica.ejercicio_9,
    [
        ((7,), True),
        ((4,), False),
    ],
    ["if", "else"]
)


# =========================
# Ejercicio 10
# =========================

validar_ejercicio(
    10,
    practica.ejercicio_10,
    [
        (
            (
                {
                    "nombre": "Ana",
                    "notas": [8, 9, 10]
                },
            ),
            {
                "nombre": "Ana",
                "promedio": 9.0,
                "aprobado": True
            }
        ),
        (
            (
                {
                    "nombre": "Luis",
                    "notas": [4, 5, 6]
                },
            ),
            {
                "nombre": "Luis",
                "promedio": 5.0,
                "aprobado": False
            }
        ),
    ],
    ["for", "len", "notas", "promedio", "aprobado"]
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