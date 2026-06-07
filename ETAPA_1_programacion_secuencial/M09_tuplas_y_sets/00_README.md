# M09 — Tuplas y Sets 📦

En este módulo vas a aprender dos nuevas estructuras de datos:

- Tuplas (`tuple`)
- Sets (`set`)

Ambas permiten guardar varios valores en una sola variable, pero tienen características diferentes.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear tuplas
- acceder a elementos de una tupla
- usar len()
- crear sets
- usar add()
- usar remove()
- usar in
- eliminar duplicados usando set()
- entender diferencias entre listas y tuplas

---

# 🧠 ¿Qué es una tupla?

Una tupla es una colección de elementos.

Se parece mucho a una lista.

Ejemplo:

```python
colores = ("rojo", "verde", "azul")
```

---

# 🔍 Explicación

```python
colores
```

es el nombre de la variable.

---

Los paréntesis:

```python
()
```

indican que estamos creando una tupla.

---

Cada elemento está separado por comas:

```python
("rojo", "verde", "azul")
```

---

# ⚠ Diferencia entre lista y tupla

Lista:

```python
colores = ["rojo", "verde", "azul"]
```

Tupla:

```python
colores = ("rojo", "verde", "azul")
```

---

La diferencia principal es:

```text
Las listas pueden modificarse.
Las tuplas no pueden modificarse.
```

---

# 🧪 Ejemplo — Crear una tupla

## Paso 1 — Código

```python
colores = ("rojo", "verde", "azul")

print(colores)
```

## Paso 2 — Resultado

```text
('rojo', 'verde', 'azul')
```

---

# 📌 Posiciones en una tupla

Las posiciones funcionan igual que en listas.

```text
rojo   verde   azul
  0      1       2
```

---

# 🧪 Ejemplo — Primer elemento

## Paso 1 — Código

```python
colores = ("rojo", "verde", "azul")

print(colores[0])
```

## Paso 2 — Resultado

```text
rojo
```

---

# 🧪 Ejemplo — Último elemento

## Paso 1 — Código

```python
colores = ("rojo", "verde", "azul")

print(colores[-1])
```

## Paso 2 — Resultado

```text
azul
```

---

# 📌 len()

También funciona con tuplas.

Sirve para contar elementos.

---

# 🧪 Ejemplo — len()

## Paso 1 — Código

```python
colores = ("rojo", "verde", "azul")

print(len(colores))
```

## Paso 2 — Resultado

```text
3
```

---

# 🧠 ¿Qué es un set?

Un set es una colección de elementos únicos.

---

# 📌 Sintaxis

```python
colores = {"rojo", "verde", "azul"}
```

---

# 🔍 Diferencia visual

Lista:

```python
["rojo", "verde", "azul"]
```

Tupla:

```python
("rojo", "verde", "azul")
```

Set:

```python
{"rojo", "verde", "azul"}
```

---

# ⚠ Característica importante

Los sets NO permiten duplicados.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
numeros = {1, 1, 2, 2, 3, 3}

print(numeros)
```

## Paso 2 — Resultado

```text
{1, 2, 3}
```

---

# 🔍 Explicación

Aunque escribimos:

```python
1, 1, 2, 2, 3, 3
```

el set guarda:

```python
1, 2, 3
```

porque elimina duplicados automáticamente.

---

# 📌 add()

Sirve para agregar elementos a un set.

---

# 🧪 Ejemplo — add()

## Paso 1 — Código

```python
colores = {"rojo", "verde"}

colores.add("azul")

print(colores)
```

## Paso 2 — Resultado

```text
{'rojo', 'verde', 'azul'}
```

---

# 🔍 Explicación

```python
colores.add("azul")
```

significa:

```text
agregar "azul" al set
```

---

# 📌 remove()

Sirve para eliminar elementos.

---

# 🧪 Ejemplo — remove()

## Paso 1 — Código

```python
colores = {"rojo", "verde", "azul"}

colores.remove("verde")

print(colores)
```

## Paso 2 — Resultado

```text
{'rojo', 'azul'}
```

---

# 🔍 Explicación

```python
colores.remove("verde")
```

significa:

```text
eliminar "verde" del set
```

---

# 📌 Operador in

Sirve para verificar si un elemento existe.

---

# 🧪 Ejemplo — in

## Paso 1 — Código

```python
colores = {"rojo", "verde", "azul"}

print("verde" in colores)
```

## Paso 2 — Resultado

```text
True
```

---

# 🧪 Otro ejemplo

## Paso 1 — Código

```python
colores = {"rojo", "verde", "azul"}

print("negro" in colores)
```

## Paso 2 — Resultado

```text
False
```

---

# 🔍 Explicación

```python
"verde" in colores
```

pregunta:

```text
¿verde existe dentro del set?
```

---

# 📌 Convertir una lista a set

Esto se usa muchísimo para eliminar duplicados.

---

# 🧪 Ejemplo

## Paso 1 — Código

```python
numeros = [1, 1, 2, 2, 3, 3]

resultado = set(numeros)

print(resultado)
```

## Paso 2 — Resultado

```text
{1, 2, 3}
```

---

# 🔍 Explicación línea por línea

```python
numeros = [1, 1, 2, 2, 3, 3]
```

Creamos una lista con duplicados.

---

```python
resultado = set(numeros)
```

Convertimos la lista en un set.

---

```python
print(resultado)
```

Mostramos el resultado.

---

# 📊 Resumen

| Estructura | Sí permite duplicados | Se puede modificar |
|------------|----------------------|--------------------|
| Lista | ✅ Sí | ✅ Sí |
| Tupla | ✅ Sí | ❌ No |
| Set | ❌ No | ✅ Sí |

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

Crear la tupla:

```python
colores = ("rojo", "verde", "azul")
```

Retornar la tupla completa.

---

## Ejercicio 2

Crear la tupla:

```python
colores = ("rojo", "verde", "azul")
```

Retornar el primer elemento.

---

## Ejercicio 3

Crear la tupla:

```python
colores = ("rojo", "verde", "azul")
```

Retornar el último elemento.

---

## Ejercicio 4

Crear el set:

```python
colores = {"rojo", "verde", "azul"}
```

Retornar el set completo.

---

## Ejercicio 5

Crear el set:

```python
colores = {"rojo", "verde", "azul"}
```

Agregar `"amarillo"` usando `add()`.

Retornar el set.

---

## Ejercicio 6

Crear el set:

```python
colores = {"rojo", "verde", "azul"}
```

Eliminar `"verde"` usando `remove()`.

Retornar el set.

---

## Ejercicio 7

Crear la tupla:

```python
numeros = (10, 20, 30)
```

Retornar la cantidad de elementos usando `len()`.

---

## Ejercicio 8

Crear el set:

```python
numeros = {1, 2, 3}
```

Verificar si existe el número `2` usando `in`.

Retornar `True` o `False`.

---

## Ejercicio 9

Crear la lista:

```python
numeros = [1, 1, 2, 2, 3, 3]
```

Convertirla a set y retornarla.

---

## Ejercicio 10

Crear la tupla:

```python
lenguajes = (
    "Python",
    "JavaScript",
    "Java"
)
```

Retornar el elemento de la posición `1`.

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

- Las tuplas usan paréntesis `()`
- Los sets usan llaves `{}`
- Las tuplas no se modifican
- Los sets eliminan duplicados
- Los sets permiten usar `add()` y `remove()`
- `in` sirve para buscar elementos
- `set()` permite eliminar duplicados de una lista