# M13 — Modularización 📦

En este módulo vas a aprender a organizar mejor tus programas.

Hasta ahora todo nuestro código estaba dentro de un único archivo.

A medida que los programas crecen, necesitamos dividir el código en varios archivos para mantenerlo ordenado.

Vamos a ver:

- import
- módulos
- paquetes
- alias con as

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- importar módulos de Python
- usar funciones de otros archivos
- crear tus propios módulos
- crear paquetes
- utilizar alias con `as`
- organizar proyectos de manera profesional

---

# 🧠 ¿Qué es modularizar?

Modularizar significa dividir un programa en partes más pequeñas.

Por ejemplo:

En lugar de tener:

```text
programa.py
```

con 1000 líneas de código,

podemos tener:

```text
matematicas.py
textos.py
usuarios.py
```

Cada archivo cumple una función específica.

Esto hace que el código sea:

- más ordenado
- más fácil de leer
- más fácil de mantener
- más fácil de reutilizar

---

# 📌 ¿Qué es un módulo?

Un módulo es simplemente un archivo `.py`.

Por ejemplo:

```text
matematicas.py
```

```python
def sumar(a, b):
    return a + b
```

Ese archivo ya es un módulo.

---

# 📌 ¿Qué es import?

La palabra:

```python
import
```

permite utilizar código que se encuentra en otro módulo.

---

# 🧪 Ejemplo

## Paso 1

```python
import math
```

## Paso 2

```python
resultado = math.sqrt(25)

print(resultado)
```

Resultado:

```text
5.0
```

---

# 🔍 Explicación línea por línea

```python
import math
```

Importa el módulo llamado:

```text
math
```

---

```python
math.sqrt(25)
```

- math → módulo
- sqrt → función
- 25 → parámetro

---

# 📌 Módulo math

Python incluye muchos módulos incorporados.

Uno de ellos es:

```python
math
```

Permite realizar cálculos matemáticos.

---

# 🧪 Ejemplo

```python
import math

print(math.pow(2, 3))
```

Resultado:

```text
8.0
```

---

# 📌 Importar una sola función

A veces no queremos importar todo el módulo.

Podemos importar únicamente una función.

---

# 🧪 Ejemplo

```python
from math import sqrt

resultado = sqrt(36)

print(resultado)
```

Resultado:

```text
6.0
```

---

# 🔍 Explicación

```python
from math import sqrt
```

Significa:

```text
Traer solamente la función sqrt
del módulo math.
```

Ahora ya no necesitamos escribir:

```python
math.sqrt()
```

Podemos escribir directamente:

```python
sqrt()
```

---

# 📌 Alias con as

Podemos cambiar el nombre de un módulo utilizando:

```python
as
```

---

# 🧪 Ejemplo

```python
import math as m

resultado = m.sqrt(25)

print(resultado)
```

Resultado:

```text
5.0
```

---

# 🔍 Explicación

```python
math
```

es el nombre original.

---

```python
m
```

es el alias.

Ahora podemos escribir:

```python
m.sqrt()
```

en lugar de:

```python
math.sqrt()
```

---

# 📌 ¿Por qué existe as?

Porque algunos módulos tienen nombres largos.

Por ejemplo:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Lo vas a encontrar constantemente en proyectos reales.

---

# 📌 Crear nuestros propios módulos

Supongamos que tenemos:

```text
matematicas.py
```

con este contenido:

```python
def sumar(a, b):
    return a + b
```

---

Podemos usar esa función desde otro archivo.

---

# 🧪 Ejemplo

```python
from matematicas import sumar

resultado = sumar(10, 5)

print(resultado)
```

Resultado:

```text
15
```

---

# 📌 ¿Qué es un paquete?

Un paquete es una carpeta que contiene módulos.

Por ejemplo:

```text
utilidades/
│
├── __init__.py
├── matematicas.py
└── textos.py
```

---

# 🔍 Explicación

```text
utilidades
```

es el paquete.

---

```text
matematicas.py
```

es un módulo.

---

```text
textos.py
```

es otro módulo.

---

# 📌 __init__.py

Este archivo le indica a Python que la carpeta puede utilizarse como paquete.

---

# 🧪 Ejemplo

Archivo:

```text
utilidades/matematicas.py
```

```python
def sumar(a, b):
    return a + b
```

---

Uso:

```python
from utilidades.matematicas import sumar

print(sumar(10, 5))
```

Resultado:

```text
15
```

---

# 📌 Importar varias funciones

También podemos importar varias funciones a la vez.

---

# 🧪 Ejemplo

```python
from utilidades.matematicas import sumar, multiplicar
```

---

Luego:

```python
resultado = multiplicar(
    sumar(2, 3),
    5
)

print(resultado)
```

Resultado:

```text
25
```

---

# 📊 Resumen

| Concepto | Significado |
|----------|-------------|
| módulo | archivo .py |
| paquete | carpeta con módulos |
| import | importar un módulo |
| from | importar partes específicas |
| as | crear alias |

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

Desde la terminal, dentro de la carpeta del módulo:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Usar:

```python
import math
```

Retornar:

```python
math.sqrt(25)
```

Resultado esperado:

```python
5.0
```

---

## Ejercicio 2

Usar:

```python
from math import sqrt
```

Retornar:

```python
sqrt(36)
```

Resultado esperado:

```python
6.0
```

---

## Ejercicio 3

Usar:

```python
import math as m
```

Retornar:

```python
m.pow(2, 3)
```

Resultado esperado:

```python
8.0
```

---

## Ejercicio 4

Importar:

```python
sumar
```

desde:

```python
utilidades.matematicas
```

Retornar:

```python
15
```

---

## Ejercicio 5

Importar:

```python
saludar
```

desde:

```python
utilidades.textos
```

Retornar:

```python
"Hola"
```

---

## Ejercicio 6

Importar:

```python
sumar
```

y

```python
multiplicar
```

Retornar:

```python
25
```

---

## Ejercicio 7

Usar:

```python
from math import pi
```

Retornar:

```python
round(pi, 2)
```

Resultado esperado:

```python
3.14
```

---

## Ejercicio 8

Usar:

```python
import random
```

Retornar:

```python
True
```

si existe:

```python
random.randint
```

---

## Ejercicio 9

Importar:

```python
multiplicar
```

desde:

```python
utilidades.matematicas
```

Retornar:

```python
20
```

---

## Ejercicio 10

Usar en la misma función:

```python
import
```

```python
from
```

```python
as
```

Retornar:

```python
"Módulo completado"
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

- Un módulo es un archivo `.py`.
- Un paquete es una carpeta con módulos.
- `import` permite reutilizar código.
- `from` importa elementos específicos.
- `as` permite usar alias.
- Modularizar hace que los proyectos sean más ordenados y profesionales.