# M14 — Ejercicios Integradores 🧩

Llegaste al último módulo de la **ETAPA 1 — Programación Secuencial**.

En este módulo no vamos a aprender una herramienta nueva.

Vamos a integrar todo lo visto hasta ahora mediante ejercicios más completos.

Trabajaremos con:

- Calculadora
- Agenda
- Sistema de alumnos

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- combinar funciones
- usar parámetros
- usar return
- usar operadores
- usar condicionales
- usar listas
- usar diccionarios
- recorrer datos
- validar información
- resolver problemas más parecidos a programas reales

---

# 🧠 ¿Qué significa integrar?

Integrar significa usar varios temas juntos para resolver un problema.

Por ejemplo, una calculadora puede usar:

- funciones
- parámetros
- operadores
- condicionales
- manejo de errores

Una agenda puede usar:

- listas
- diccionarios
- funciones
- búsqueda de datos

Un sistema de alumnos puede usar:

- listas
- diccionarios
- promedios
- condicionales
- recorridos

---

# 📌 Temas que vamos a practicar

En este módulo vas a reutilizar conocimientos de módulos anteriores:

| Módulo | Tema |
|---|---|
| M02 | Variables y tipos de datos |
| M03 | Operadores |
| M04 | Condicionales |
| M05 | Bucles |
| M06 | Funciones |
| M08 | Listas |
| M10 | Diccionarios |
| M11 | Manejo de errores |

---

# 🧮 Proyecto 1 — Calculadora

Una calculadora permite realizar operaciones matemáticas.

---

# 🧪 Ejemplo — Sumar

## Paso 1 — Código

```python
def sumar(a, b):
    return a + b
```

## Paso 2 — Uso

```python
resultado = sumar(10, 5)

print(resultado)
```

## Paso 3 — Resultado

```text
15
```

---

# 🧪 Ejemplo — Calculadora con operación

## Paso 1 — Código

```python
def calcular(a, b, operacion):

    if operacion == "suma":
        return a + b

    elif operacion == "resta":
        return a - b

    else:
        return "Operación inválida"
```

## Paso 2 — Uso

```python
print(calcular(10, 5, "suma"))
```

## Paso 3 — Resultado

```text
15
```

---

# 📒 Proyecto 2 — Agenda

Una agenda permite guardar contactos.

Un contacto puede representarse con un diccionario.

---

# 🧪 Ejemplo — Contacto

```python
contacto = {
    "nombre": "Ana",
    "telefono": "123456"
}
```

---

# 🧪 Ejemplo — Lista de contactos

```python
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
```

---

# 🔍 Buscar un contacto

Podemos recorrer la agenda con `for`.

```python
def buscar_contacto(agenda, nombre):

    for contacto in agenda:

        if contacto["nombre"] == nombre:
            return contacto

    return "Contacto no encontrado"
```

---

# 🧠 ¿Qué ocurre?

Python recorre cada contacto.

Si encuentra uno con el nombre buscado, lo retorna.

Si termina el recorrido y no encontró nada, retorna:

```text
Contacto no encontrado
```

---

# 🎓 Proyecto 3 — Sistema de alumnos

Un sistema de alumnos puede guardar estudiantes y notas.

---

# 🧪 Ejemplo — Alumno

```python
alumno = {
    "nombre": "Ana",
    "notas": [8, 9, 10]
}
```

---

# 🧪 Calcular promedio

```python
def calcular_promedio(notas):

    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)

    return promedio
```

---

# 🧪 Saber si aprueba

```python
def esta_aprobado(promedio):

    if promedio >= 6:
        return True

    else:
        return False
```

---

# 📌 Importante

En este módulo los ejercicios son más largos.

Es normal que te lleven más tiempo.

La idea no es memorizar.

La idea es aprender a pensar paso a paso.

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 📌 Importante

En este módulo las funciones ya están creadas.

Ejemplo:

```python
def ejercicio_1(a, b):
    pass
```

Tu trabajo es:

- NO borrar `def`
- NO cambiar el nombre de la función
- NO cambiar los parámetros
- borrar `pass`
- escribir la solución dentro de la función
- usar `return`

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1 — Sumar

Crear una función que reciba dos números:

```python
a
b
```

Retornar la suma.

---

## Ejercicio 2 — Restar

Crear una función que reciba dos números:

```python
a
b
```

Retornar la resta.

---

## Ejercicio 3 — Calculadora

Crear una función que reciba:

```python
a
b
operacion
```

Si `operacion` es `"suma"`, retornar la suma.

Si `operacion` es `"resta"`, retornar la resta.

Si `operacion` es `"multiplicacion"`, retornar la multiplicación.

Si `operacion` es `"division"`, retornar la división.

Si la operación no existe, retornar:

```text
Operación inválida
```

---

## Ejercicio 4 — División segura

Crear una función que reciba:

```python
a
b
```

Intentar dividir `a / b`.

Si `b` es `0`, retornar:

```text
No se puede dividir por cero
```

---

## Ejercicio 5 — Crear contacto

Crear una función que reciba:

```python
nombre
telefono
```

Retornar un diccionario con esta estructura:

```python
{
    "nombre": nombre,
    "telefono": telefono
}
```

---

## Ejercicio 6 — Buscar contacto

Crear una función que reciba:

```python
agenda
nombre
```

La agenda será una lista de diccionarios.

Si encuentra el contacto, retornar el diccionario completo.

Si no lo encuentra, retornar:

```text
Contacto no encontrado
```

---

## Ejercicio 7 — Agregar contacto

Crear una función que reciba:

```python
agenda
contacto
```

Agregar el contacto a la agenda usando `append()`.

Retornar la agenda actualizada.

---

## Ejercicio 8 — Calcular promedio

Crear una función que reciba una lista de notas.

Retornar el promedio.

---

## Ejercicio 9 — Verificar aprobación

Crear una función que reciba un promedio.

Si el promedio es mayor o igual a `6`, retornar:

```python
True
```

Si no, retornar:

```python
False
```

---

## Ejercicio 10 — Sistema de alumnos

Crear una función que reciba:

```python
alumno
```

El alumno será un diccionario con esta estructura:

```python
{
    "nombre": "Ana",
    "notas": [8, 9, 10]
}
```

La función debe:

1. Calcular el promedio.
2. Verificar si está aprobado.
3. Retornar un diccionario con esta estructura:

```python
{
    "nombre": "Ana",
    "promedio": 9.0,
    "aprobado": True
}
```

---

# 🚀 Resultado esperado

```text
🧪 Corrigiendo ejercicios...

✅ Ejercicio 1 correcto
✅ Ejercicio 2 correcto
❌ Ejercicio 3 incorrecto

🎯 Resultado final: 2/3
```

---

# 🎯 Lo más importante que aprendiste

- Un programa real combina varios conceptos.
- Las funciones ayudan a organizar la lógica.
- Las listas sirven para guardar varios elementos.
- Los diccionarios sirven para representar entidades.
- Los condicionales permiten tomar decisiones.
- Los bucles permiten recorrer datos.
- El manejo de errores evita que el programa se rompa.

---

# 🏁 Cierre de la ETAPA 1

Con este módulo cerrás la primera gran etapa del curso.

Ya tenés base para avanzar hacia:

```text
ETAPA 2 — Programación Orientada a Objetos
```

Ahí vamos a empezar a modelar programas usando:

- clases
- objetos
- atributos
- métodos
- herencia
- polimorfismo