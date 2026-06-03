# M02 — Variables y Tipos de Datos 📦

Bienvenido al segundo módulo de **Python Desde Cero**.

En este módulo vas a aprender:

- qué son las variables
- cómo guardar información
- tipos de datos básicos
- strings
- enteros
- decimales
- booleanos
- constantes
- concatenación de texto
- f-strings

---

# 📦 ¿Qué es una variable?

Una variable sirve para guardar información.

## Paso 1 — Escribimos el código

```python
nombre = "Enzo"

print(nombre)
```

## Paso 2 — Ejecutamos el programa

```bash
python ejemplo.py
```

## Paso 3 — Resultado en la terminal

```text
Enzo
```

---

# 🔠 Strings (`str`)

Los strings son textos. Se escriben entre comillas.

## Paso 1 — Código

```python
mensaje = "Hola mundo"

print(mensaje)
```

## Paso 2 — Resultado

```text
Hola mundo
```

---

# 🔢 Enteros (`int`)

Los enteros son números sin decimales.

## Paso 1 — Código

```python
edad = 30

print(edad)
```

## Paso 2 — Resultado

```text
30
```

---

# 🔢 Decimales (`float`)

Los `float` son números con decimales.

## Paso 1 — Código

```python
altura = 1.75

print(altura)
```

## Paso 2 — Resultado

```text
1.75
```

---

# ✅ Booleanos (`bool`)

Los booleanos representan verdadero o falso.

En Python se escriben:

```python
True
False
```

## Paso 1 — Código

```python
es_estudiante = True

print(es_estudiante)
```

## Paso 2 — Resultado

```text
True
```

---

# 📌 Constantes

Python no tiene constantes reales como otros lenguajes.

Pero por convención, cuando un valor no debería modificarse, se escribe en MAYÚSCULAS.

## Paso 1 — Código

```python
PAIS = "Argentina"

print(PAIS)
```

## Paso 2 — Resultado

```text
Argentina
```

Aunque Python permite cambiar el valor, no es recomendable hacerlo.

---

# ➕ Concatenación

Concatenar significa unir textos.

## Paso 1 — Código

```python
nombre = "Enzo"

print("Hola, " + nombre)
```

## Paso 2 — Resultado

```text
Hola, Enzo
```

---

# ✨ f-strings

Los f-strings permiten insertar variables dentro de un texto de forma más cómoda.

## Paso 1 — Código

```python
nombre = "Enzo"
edad = 30

print(f"Me llamo {nombre} y tengo {edad} años")
```

## Paso 2 — Resultado

```text
Me llamo Enzo y tengo 30 años
```

---

# 📥 input y variables

Podemos pedir información al usuario y guardarla en una variable.

## Paso 1 — Código

```python
nombre = input("Ingrese su nombre: ")

print("Hola, " + nombre + "! Bienvenido a Python.")
```

## Paso 2 — Ejecutamos el programa

```bash
python ejemplo.py
```

## Paso 3 — El programa pide información

```text
Ingrese su nombre:
```

## Paso 4 — El usuario escribe su nombre

```text
Ingrese su nombre: Enzo
```

## Paso 5 — Resultado final

```text
Hola, Enzo! Bienvenido a Python.
```

---

# 🧠 Diferencia entre guardar y mostrar

Guardar información:

```python
nombre = "Enzo"
```

Mostrar información:

```python
print(nombre)
```

Ejemplo completo:

```python
nombre = "Enzo"

print(nombre)
```

Resultado:

```text
Enzo
```

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

Cada ejercicio ya tiene una función creada.

Ejemplo:

```python
def ejercicio_1():
    pass
```

La palabra `pass` significa que la función está vacía.

Tu trabajo es:

1. borrar `pass`
2. escribir tu solución
3. usar `return`

Ejemplo:

```python
def ejercicio_1():
    return "Hola"
```

---

# 🧪 ¿Cómo pruebo los ejercicios?

## Paso 1 — Completar `practica.py`

```python
def ejercicio_1():
    return "Hola"
```

## Paso 2 — Guardar el archivo

Usá:

```text
CTRL + S
```

## Paso 3 — Ejecutar el test

```bash
python test.py
```

## Paso 4 — Ver el resultado

```text
🧪 Corrigiendo ejercicios...

✅ Ejercicio 1 correcto
❌ Ejercicio 2 incorrecto

🎯 Resultado final: 1/10
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Retornar un texto (`str`).

---

## Ejercicio 2

Retornar un número entero (`int`).

---

## Ejercicio 3

Retornar un número decimal (`float`).

---

## Ejercicio 4

Retornar `True`.

---

## Ejercicio 5

Crear una variable llamada `nombre` y retornar su valor.

---

## Ejercicio 6

Crear una variable llamada `edad` y retornar su valor.

---

## Ejercicio 7

Crear una constante llamada `PAIS` y retornar su valor.

---

## Ejercicio 8

Retornar un texto concatenado.

Ejemplo:

```text
Hola Enzo
```

---

## Ejercicio 9

Usar f-string y retornar:

```text
Me llamo Enzo
```

---

## Ejercicio 10

Crear:

- un string
- un int
- un float
- un bool

y retornar uno de ellos.

---

# 🧪 Ejercicios manuales

Estos ejercicios no son autocorregibles porque utilizan `input()`.

Para resolverlos:

1. Crear un archivo `.py`
2. Escribir el código
3. Guardar el archivo
4. Ejecutarlo desde la terminal

---

# Ejercicio Manual 11

## Objetivo

Pedir un nombre usando `input()` y mostrar un saludo por pantalla.

## Archivo sugerido

```text
manual_11.py
```

## Ejemplo esperado

```text
Ingrese su nombre: Enzo
Hola Enzo
```

---

# Ejercicio Manual 12

## Objetivo

Pedir una edad usando `input()` y mostrar un mensaje concatenado.

## Archivo sugerido

```text
manual_12.py
```

## Ejemplo esperado

```text
Ingrese su edad: 30
Tu edad es 30 años
```

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear variables
- guardar texto
- guardar números enteros
- guardar números decimales
- guardar valores booleanos
- entender qué es una constante por convención
- concatenar textos
- usar f-strings
- guardar información ingresada con `input()`