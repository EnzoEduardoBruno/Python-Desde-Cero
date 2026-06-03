# M07 — Strings 🔤

En este módulo vas a aprender a trabajar con textos en Python.

Los textos en programación se llaman:

```text
strings
```

---

# 🧠 ¿Qué es un string?

Un string es texto.

Ejemplos:

```python
"Hola"
"Python"
"Enzo"
"123"
```

Todo lo que esté entre comillas es un string.

---

# 🧪 Ejemplo — Crear un string

## Paso 1 — Código

```python
nombre = "Enzo"

print(nombre)
```

## Paso 2 — Resultado

```text
Enzo
```

---

# 📌 Métodos

Los métodos son funciones que pertenecen a un tipo de dato.

Los strings tienen muchos métodos útiles.

---

# 🔠 upper()

Convierte el texto a MAYÚSCULAS.

---

# 🧪 Ejemplo — upper()

## Paso 1 — Código

```python
texto = "python"

resultado = texto.upper()

print(resultado)
```

## Paso 2 — Resultado

```text
PYTHON
```

---

# 🔡 lower()

Convierte el texto a minúsculas.

---

# 🧪 Ejemplo — lower()

```python
texto = "PYTHON"

resultado = texto.lower()

print(resultado)
```

Resultado:

```text
python
```

---

# ✂ Slicing

Slicing sirve para cortar partes de un string.

---

# 🧪 Ejemplo — slicing

```python
texto = "Python"

print(texto[0:3])
```

Resultado:

```text
Pyt
```

---

# 🔍 Explicación

```python
texto[0:3]
```

significa:

```text
desde la posición 0
hasta la posición 3
```

⚠ El último número NO se incluye.

---

# 📌 Posiciones

```text
P  y  t  h  o  n
0  1  2  3  4  5
```

---

# 🧪 Otro ejemplo

```python
texto = "Python"

print(texto[2:6])
```

Resultado:

```text
thon
```

---

# 🧩 Formateo

Formatear significa construir textos dinámicos.

---

# 🧪 Ejemplo — concatenación

```python
nombre = "Enzo"

mensaje = "Hola " + nombre

print(mensaje)
```

Resultado:

```text
Hola Enzo
```

---

# ✨ f-strings

Los f-strings son la forma moderna de insertar variables en textos.

---

# 🧪 Ejemplo — f-string

```python
nombre = "Enzo"

mensaje = f"Hola {nombre}"

print(mensaje)
```

Resultado:

```text
Hola Enzo
```

---

# 🔍 Explicación

## La letra f

```python
f"Hola {nombre}"
```

permite insertar variables dentro del texto.

---

# 📌 Las llaves {}

```python
{nombre}
```

significan:

```text
insertar el valor de la variable nombre
```

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

- NO borrar `def`
- NO cambiar el nombre de la función
- borrar `pass`
- escribir la solución dentro de la función
- usar `return`

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Retornar un string.

---

## Ejercicio 2

Usar `upper()`.

---

## Ejercicio 3

Usar `lower()`.

---

## Ejercicio 4

Usar slicing.

---

## Ejercicio 5

Usar concatenación.

---

## Ejercicio 6

Usar f-string.

---

## Ejercicio 7

Retornar la primera letra de un string.

---

## Ejercicio 8

Retornar las últimas letras usando slicing.

---

## Ejercicio 9

Concatenar nombre y apellido.

---

## Ejercicio 10

Crear un string libre y retornar cualquier resultado.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear strings
- usar métodos
- usar `upper()`
- usar `lower()`
- usar slicing
- concatenar textos
- usar f-strings
- entender posiciones en strings