# M06 — Funciones ⚙️

En este módulo vas a aprender a crear y usar funciones.

Las funciones sirven para organizar código y reutilizar instrucciones.

Vamos a ver:

- `def`
- parámetros
- `return`

---

# 🤔 ¿Qué es una función?

Una función es un bloque de código que realiza una tarea específica.

Las funciones nos ayudan a:

- reutilizar código
- organizar programas
- evitar repetir instrucciones
- hacer programas más claros

---

# ⚙️ def

`def` sirve para crear funciones.

---

# 🧪 Ejemplo — Función simple

## Paso 1 — Código

```python
def saludar():
    print("Hola")
```

---

# 🔍 Explicación línea por línea

## Línea 1

```python
def saludar():
```

- `def` significa:
  
```text
definir función
```

- `saludar` es el nombre de la función
- `()` son los paréntesis de la función
- `:` indica el inicio del bloque

---

## Línea 2

```python
print("Hola")
```

Es el código que ejecutará la función.

---

# ⚠ Importante

Crear una función NO la ejecuta.

---

# 🧪 Ejemplo

```python
def saludar():
    print("Hola")
```

Esto solamente crea la función.

---

# ▶ Ejecutar una función

Para ejecutar una función usamos:

```python
nombre_funcion()
```

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
def saludar():
    print("Hola")

saludar()
```

## Paso 2 — Resultado

```text
Hola
```

---

# 📦 Parámetros

Los parámetros permiten enviar información a una función.

---

# 🧪 Ejemplo — Parámetros

## Paso 1 — Código

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Enzo")
```

---

# 🔍 Explicación

## nombre

```python
def saludar(nombre):
```

`nombre` es una variable que recibe información.

---

## "Enzo"

```python
saludar("Enzo")
```

La función recibe:

```text
Enzo
```

---

## Resultado

```text
Hola Enzo
```

---

# 🔙 return

`return` sirve para devolver un valor.

---

# 🧪 Ejemplo — return

## Paso 1 — Código

```python
def sumar():
    return 10 + 5
```

---

# 🔍 ¿Qué devuelve?

```text
15
```

---

# 📌 Diferencia entre print y return

## print()

Muestra información por pantalla.

---

## return

Devuelve un valor.

---

# 🧪 Ejemplo

```python
def sumar():
    return 10 + 5

resultado = sumar()

print(resultado)
```

Resultado:

```text
15
```

---

# 📌 Función con parámetros y return

## Paso 1 — Código

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

resultado = sumar(10, 5)

print(resultado)
```

---

# 🔍 Explicación

## numero_1 y numero_2

Son parámetros.

---

## sumar(10, 5)

Envía:

```text
10 y 5
```

a la función.

---

## Resultado

```text
15
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

Crear una función que retorne:

```text
Hola
```

---

## Ejercicio 2

Crear una función con un parámetro llamado `nombre`
y retornar ese valor.

---

## Ejercicio 3

Crear una función con dos parámetros
y retornar la suma.

---

## Ejercicio 4

Crear una función con dos parámetros
y retornar la multiplicación.

---

## Ejercicio 5

Crear una función que retorne `True`.

---

## Ejercicio 6

Crear una función que retorne `False`.

---

## Ejercicio 7

Crear una función con un parámetro llamado `edad`
y retornar:

```text
Mayor
```

o:

```text
Menor
```

---

## Ejercicio 8

Crear una función que concatene textos.

---

## Ejercicio 9

Crear una función con parámetros
y usar f-strings.

---

## Ejercicio 10

Crear una función libre
y retornar cualquier resultado.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear funciones
- usar `def`
- usar parámetros
- usar `return`
- enviar información a funciones
- reutilizar código
- organizar programas
- diferenciar `print()` de `return`