# M05 — Bucles 🔁

En este módulo vas a aprender a repetir instrucciones usando bucles.

Los bucles permiten ejecutar código varias veces sin tener que escribirlo repetido.

Vamos a ver:

* `while`
* `for`
* `range()`
* `break`
* `continue`

---

# 🔄 ¿Qué es un bucle?

Un bucle permite repetir instrucciones.

Ejemplo:

* mostrar números
* recorrer listas
* repetir preguntas
* ejecutar tareas varias veces

Sin bucles tendríamos que escribir el mismo código muchas veces.

---

# 🔁 while

`while` significa:

```text
mientras esto sea verdadero...
```

---

# 🧪 Ejemplo — while

## Paso 1 — Código

```python
contador = 1

while contador <= 5:
    print(contador)

    contador += 1
```

---

# 🔍 Explicación línea por línea

## Línea 1

```python
contador = 1
```

Creamos una variable llamada `contador`.

La variable empieza con valor:

```text
1
```

---

## Línea 3

```python
while contador <= 5:
```

Python pregunta:

```text
¿contador es menor o igual a 5?
```

Si la respuesta es `True`,
el bloque se ejecuta.

---

## Línea 4

```python
print(contador)
```

Muestra el valor actual de `contador`.

---

## Línea 6

```python
contador += 1
```

Esto significa:

```python
contador = contador + 1
```

Aumenta el contador en 1.

---

# 🧠 ¿Qué ocurre?

## Primera vuelta

```text
contador = 1
```

Muestra:

```text
1
```

Luego aumenta:

```text
contador = 2
```

---

## Segunda vuelta

```text
contador = 2
```

Muestra:

```text
2
```

---

## Resultado final

```text
1
2
3
4
5
```

---

# ⚠ Cuidado con while

Si nunca modificamos el contador,
el bucle nunca termina.

---

# ❌ Incorrecto

```python
contador = 1

while contador <= 5:
    print(contador)
```

Esto crea un bucle infinito.

---

# ✅ Correcto

```python
contador = 1

while contador <= 5:
    print(contador)

    contador += 1
```

---

# 🔁 for

`for` sirve para recorrer elementos o repetir acciones.

---

# 🧪 Ejemplo — for

## Paso 1 — Código

```python
for numero in range(5):
    print(numero)
```

---

# 🔍 Explicación línea por línea

## Línea 1

```python
for numero in range(5):
```

Python genera números usando:

```python
range(5)
```

Eso genera:

```text
0
1
2
3
4
```

---

# 📌 ¿Qué es numero?

```python
for numero in range(5):
```

`numero` es una variable temporal.

En cada vuelta guarda un valor distinto.

Python hace internamente algo parecido a esto:

```text
numero = 0
numero = 1
numero = 2
numero = 3
numero = 4
```

---

# 📌 ¿Podría llamarse diferente?

Sí.

Esto funciona igual:

```python
for i in range(5):
```

o:

```python
for banana in range(5):
```

Pero usar nombres descriptivos es mejor para aprender.

---

# 📌 ¿Qué hace range()?

`range(5)` genera números desde:

```text
0 hasta 4
```

No incluye el 5.

---

# Línea 2

```python
print(numero)
```

Muestra el valor actual de `numero`.

---

# 🧠 Resultado final

```text
0
1
2
3
4
```

---

# 📦 Listas

Las listas permiten guardar múltiples valores.

---

# 🧪 Ejemplo — Lista vacía

```python
numeros = []
```

---

# 📌 ¿Qué significa esto?

## numeros

Es el nombre de la variable.

---

## []

Los corchetes representan una lista.

---

## Lista vacía

```python
[]
```

significa:

```text
lista sin elementos
```

---

# 📦 append()

`append()` sirve para agregar elementos a una lista.

---

# 🧪 Ejemplo — append()

## Paso 1 — Código

```python
numeros = []

numeros.append(1)
numeros.append(2)
numeros.append(3)

print(numeros)
```

---

# 🔍 Explicación paso a paso

## Inicio

```python
numeros = []
```

La lista está vacía:

```text
[]
```

---

## Primera línea

```python
numeros.append(1)
```

Agrega el número 1.

Lista actual:

```text
[1]
```

---

## Segunda línea

```python
numeros.append(2)
```

Lista actual:

```text
[1, 2]
```

---

## Tercera línea

```python
numeros.append(3)
```

Lista actual:

```text
[1, 2, 3]
```

---

# 🧪 Ejemplo completo — for + append()

## Paso 1 — Código

```python
numeros = []

for numero in range(5):
    numeros.append(numero)

print(numeros)
```

---

# 🔍 Explicación línea por línea

## Línea 1

```python
numeros = []
```

Creamos una lista vacía.

---

## Línea 3

```python
for numero in range(5):
```

`range(5)` genera:

```text
0
1
2
3
4
```

En cada vuelta:

* `numero` guarda un valor distinto

---

## Línea 4

```python
numeros.append(numero)
```

Agrega el valor actual de `numero`
a la lista.

---

# 🧠 ¿Qué ocurre en cada vuelta?

## Vuelta 1

```text
numero = 0
```

Lista:

```text
[0]
```

---

## Vuelta 2

```text
numero = 1
```

Lista:

```text
[0, 1]
```

---

## Vuelta 3

```text
numero = 2
```

Lista:

```text
[0, 1, 2]
```

---

## Resultado final

```text
[0, 1, 2, 3, 4]
```

---

# 🛑 break

`break` sirve para cortar un bucle.

---

# 🧪 Ejemplo — break

```python
for numero in range(10):

    if numero == 5:
        break

    print(numero)
```

---

# 🔍 ¿Qué ocurre?

Python recorre:

```text
0
1
2
3
4
5
...
```

Pero cuando:

```python
numero == 5
```

ejecuta:

```python
break
```

y el bucle termina.

---

# 🧠 Resultado

```text
0
1
2
3
4
```

---

# ⏭ continue

`continue` sirve para saltear una vuelta del bucle.

---

# 🧪 Ejemplo — continue

```python
for numero in range(5):

    if numero == 2:
        continue

    print(numero)
```

---

# 🔍 ¿Qué ocurre?

Cuando:

```python
numero == 2
```

Python ejecuta:

```python
continue
```

y salta directamente a la siguiente vuelta.

---

# 🧠 Resultado

```text
0
1
3
4
```

El número 2 no se muestra.

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* usar `while`
* usar `for`
* usar `range()`
* repetir instrucciones
* usar listas
* usar `append()`
* usar `break`
* usar `continue`
* entender cómo funciona un bucle paso a paso
* evitar bucles infinitos