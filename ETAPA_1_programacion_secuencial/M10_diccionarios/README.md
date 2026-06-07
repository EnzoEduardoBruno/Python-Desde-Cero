# M10 — Diccionarios 📚

En este módulo vas a aprender a trabajar con diccionarios.

Los diccionarios permiten guardar información usando una relación:

```text
clave → valor
(key → value)
```

Son una de las estructuras más utilizadas en Python.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* crear diccionarios
* entender qué es una clave (key)
* entender qué es un valor (value)
* acceder a valores
* agregar datos
* modificar datos
* eliminar datos
* usar keys()
* usar values()
* usar items()
* recorrer diccionarios
* verificar si existe una clave

---

# 🧠 ¿Qué es un diccionario?

Un diccionario es una colección de datos organizados mediante:

```text
clave → valor
```

Ejemplo:

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}
```

---

# 🔍 Explicación línea por línea

```python
persona
```

es el nombre de la variable.

---

Las llaves:

```python
{}
```

indican que estamos creando un diccionario.

---

Dentro del diccionario tenemos:

```python
"nombre": "Ana"
```

donde:

```text
nombre → clave (key)
Ana → valor (value)
```

---

Y también:

```python
"edad": 25
```

donde:

```text
edad → clave (key)
25 → valor (value)
```

---

# 📌 Visualmente

```text
┌─────────┬─────────┐
│ CLAVE   │ VALOR   │
├─────────┼─────────┤
│ nombre  │ Ana     │
│ edad    │ 25      │
└─────────┴─────────┘
```

---

# 🧪 Ejemplo — Crear un diccionario

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona)
```

## Paso 2 — Resultado

```text
{'nombre': 'Ana', 'edad': 25}
```

---

# 📌 Acceder a un valor

Podemos obtener un valor usando su clave.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona["nombre"])
```

## Paso 2 — Resultado

```text
Ana
```

---

# 🔍 Explicación

```python
persona["nombre"]
```

significa:

```text
buscar el valor asociado a la clave "nombre"
```

---

# 🧪 Otro ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona["edad"])
```

## Paso 2 — Resultado

```text
25
```

---

# 📌 Agregar datos

Podemos agregar una nueva clave.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana"
}

persona["edad"] = 25

print(persona)
```

## Paso 2 — Resultado

```text
{'nombre': 'Ana', 'edad': 25}
```

---

# 🔍 Explicación

```python
persona["edad"] = 25
```

significa:

```text
crear una nueva clave llamada edad
y guardar el valor 25
```

---

# 📌 Modificar datos

Si la clave ya existe, podemos cambiar su valor.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

persona["edad"] = 30

print(persona)
```

## Paso 2 — Resultado

```text
{'nombre': 'Ana', 'edad': 30}
```

---

# 🔍 Explicación

```python
persona["edad"] = 30
```

significa:

```text
cambiar el valor existente
```

---

# 📌 Eliminar datos con pop()

pop() sirve para eliminar una clave.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

persona.pop("edad")

print(persona)
```

## Paso 2 — Resultado

```text
{'nombre': 'Ana'}
```

---

# 🔍 Explicación

```python
persona.pop("edad")
```

significa:

```text
eliminar la clave edad
y su valor asociado
```

---

# 📌 keys()

Devuelve todas las claves del diccionario.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona.keys())
```

## Paso 2 — Resultado

```text
dict_keys(['nombre', 'edad'])
```

---

# 📌 values()

Devuelve todos los valores.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona.values())
```

## Paso 2 — Resultado

```text
dict_values(['Ana', 25])
```

---

# 📌 items()

Devuelve clave y valor al mismo tiempo.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona.items())
```

## Paso 2 — Resultado

```text
dict_items([('nombre', 'Ana'), ('edad', 25)])
```

---

# 📌 Recorrer un diccionario

Podemos recorrer todas las claves y valores.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

for clave, valor in persona.items():
    print(clave, valor)
```

## Paso 2 — Resultado

```text
nombre Ana
edad 25
```

---

# 🔍 Explicación línea por línea

```python
for clave, valor in persona.items():
```

significa:

```text
recorrer todas las claves y valores
del diccionario
```

---

```python
print(clave, valor)
```

significa:

```text
mostrar cada clave y su valor
```

---

# 📌 Verificar si existe una clave

Podemos usar:

```python
in
```

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print("nombre" in persona)
```

## Paso 2 — Resultado

```text
True
```

---

# 🧪 Otro ejemplo

## Paso 1 — Código

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}

print("apellido" in persona)
```

## Paso 2 — Resultado

```text
False
```

---

# 📊 Resumen

| Método   | Uso                      |
| -------- | ------------------------ |
| keys()   | obtener claves           |
| values() | obtener valores          |
| items()  | obtener claves y valores |
| pop()    | eliminar claves          |
| in       | verificar claves         |

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
def ejercicio_1():
    pass
```

Tu trabajo es:

* NO borrar `def`
* NO cambiar el nombre de la función
* borrar `pass`
* escribir la solución dentro de la función
* usar `return`

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Crear el diccionario:

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}
```

Retornar el diccionario completo.

---

## Ejercicio 2

Retornar el valor asociado a `"nombre"`.

---

## Ejercicio 3

Retornar el valor asociado a `"edad"`.

---

## Ejercicio 4

Agregar la clave:

```python
"edad": 25
```

---

## Ejercicio 5

Modificar:

```python
"edad": 30
```

---

## Ejercicio 6

Eliminar la clave `"edad"` usando `pop()`.

---

## Ejercicio 7

Retornar las claves usando `keys()`.

---

## Ejercicio 8

Retornar los valores usando `values()`.

---

## Ejercicio 9

Verificar si existe la clave `"nombre"`.

---

## Ejercicio 10

Agregar:

```python
"stock": 5
```

al diccionario producto.

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

* Los diccionarios usan llaves `{}`.
* Guardan información mediante clave → valor.
* Se accede usando la clave.
* Podemos agregar datos.
* Podemos modificar datos.
* Podemos eliminar datos.
* Podemos recorrer claves y valores.
* Son una de las estructuras más utilizadas de Python.

```
```