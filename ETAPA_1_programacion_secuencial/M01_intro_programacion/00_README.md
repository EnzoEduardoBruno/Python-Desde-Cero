# M01 — Introducción a la Programación 🚀

Bienvenido al primer módulo de **Python Desde Cero**.

En este módulo vas a aprender:

- qué es programar
- qué es un algoritmo
- qué es la programación secuencial
- cómo mostrar información por pantalla
- cómo pedir información al usuario
- cómo devolver valores usando return
- cómo resolver ejercicios simples paso a paso

---

# 🧠 ¿Qué es programar?

Programar es darle instrucciones a una computadora para que realice una tarea.

La computadora no adivina lo que queremos hacer.  
Nosotros tenemos que indicarle los pasos de forma clara y ordenada.

---

# 💡 ¿Qué es un algoritmo?

Un algoritmo es una serie de pasos ordenados para resolver un problema.

Ejemplo cotidiano:

## Preparar un café ☕

1. Calentar agua
2. Poner café en una taza
3. Agregar agua caliente
4. Revolver
5. Tomar el café

Eso es un algoritmo porque tiene pasos ordenados.

---

# 🔄 ¿Qué es la programación secuencial?

La programación secuencial significa que las instrucciones se ejecutan una después de otra, en orden.

Python lee el código desde arriba hacia abajo.

---

# 🧪 Ejemplo — Programación secuencial

## Paso 1 — Código

```python
print("Hola")
print("Bienvenido")
print("Python")
```

## Paso 2 — Resultado

```text
Hola
Bienvenido
Python
```

## Paso 3 — ¿Qué ocurrió?

Python ejecutó:

1. `print("Hola")`
2. `print("Bienvenido")`
3. `print("Python")`

en ese mismo orden.

---

# 🖨 Mostrar información con print()

`print()` sirve para mostrar información por pantalla.

---

# 🧪 Ejemplo — print()

## Paso 1 — Código

```python
print("Hola mundo")
```

## Paso 2 — Resultado

```text
Hola mundo
```

---

# ⌨ Pedir información con input()

`input()` sirve para pedirle información al usuario.

---

# 🧪 Ejemplo — input()

## Paso 1 — Código

```python
nombre = input("Ingrese su nombre: ")

print(nombre)
```

## Paso 2 — Programa ejecutándose

```text
Ingrese su nombre:
```

## Paso 3 — El usuario escribe

```text
Enzo
```

## Paso 4 — Resultado final

```text
Enzo
```

---

# 🧠 ¿Qué ocurrió?

- `input()` esperó información del usuario
- el usuario escribió un texto
- Python guardó ese texto en la variable `nombre`
- luego `print(nombre)` mostró el resultado

---

# 🔁 Entrada → Proceso → Salida

Muchos programas funcionan con esta lógica.

---

# 📥 Entrada

El usuario ingresa información.

Ejemplo:

```python
nombre = input("Ingrese su nombre: ")
```

---

# ⚙️ Proceso

El programa trabaja con la información recibida.

Ejemplo:

```python
saludo = "Hola " + nombre
```

---

# 📤 Salida

El programa muestra un resultado.

Ejemplo:

```python
print(saludo)
```

---

# 🧪 Ejemplo completo

## Paso 1 — Código

```python
nombre = input("Ingrese su nombre: ")

saludo = "Hola " + nombre

print(saludo)
```

## Paso 2 — Resultado

```text
Ingrese su nombre: Enzo
Hola Enzo
```

---

# 🔙 ¿Qué es return?

`return` sirve para devolver un valor desde una función.

---

# 🧪 Ejemplo — return

## Paso 1 — Código

```python
def saludar():
    return "Hola"
```

## Paso 2 — ¿Qué devuelve la función?

```text
Hola
```

---

# 🧠 Importante

`return` NO muestra información por pantalla.

Solo devuelve un valor.

Para mostrarlo, usamos `print()`:

```python
print(saludar())
```

Resultado:

```text
Hola
```

---

# 🖨 Diferencia entre print y return

## print()

`print()` muestra información por pantalla.

---

# 🧪 Ejemplo

```python
print("Hola")
```

Resultado:

```text
Hola
```

---

## return

`return` devuelve un valor.

---

# 🧪 Ejemplo

```python
def saludar():
    return "Hola"
```

---

# 📌 Importante

Para que el sistema de autocorrección funcione correctamente,
los ejercicios deben usar:

```python
return
```

y NO:

```python
print()
```

---

# ❌ Incorrecto

```python
def ejercicio_1():
    print("Hola mundo")
```

---

# ✅ Correcto

```python
def ejercicio_1():
    return "Hola mundo"
```

---

# 🤔 ¿Por qué?

Porque el archivo `test.py` necesita comparar el resultado de cada ejercicio.

Ejemplo:

```python
if ejercicio_1() == "Hola mundo":
```

Por eso las funciones deben devolver valores usando `return`.

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en el archivo:

```text
practica.py
```

Cada ejercicio ya tiene una función creada.

---

# 🧪 Ejemplo

## Paso 1 — Código inicial

```python
def ejercicio_1():
    pass
```

La palabra `pass` significa que la función está vacía.

---

## Paso 2 — Tu trabajo

Tenés que:

- borrar `pass`
- escribir la solución dentro de la función
- usar `return`
- guardar el archivo

---

## Paso 3 — Solución

```python
def ejercicio_1():
    return "Hola mundo"
```

---

# 🧪 ¿Cómo pruebo mis ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🧪 Resultado esperado

```text
🧪 Corrigiendo ejercicios...

✅ Ejercicio 1 correcto
❌ Ejercicio 2 incorrecto

🎯 Resultado final: 1/10
```

---

# 📌 Importante

- No cambies el nombre de las funciones.
- No cambies el nombre del archivo `practica.py`.
- No modifiques `test.py`.
- Guardá el archivo antes de ejecutar.
- Usá `return`, no `print()`.

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Retornar el texto:

```text
Hola mundo
```

---

## Ejercicio 2

Retornar el texto:

```text
Estoy aprendiendo a programar
```

---

## Ejercicio 3

Retornar el texto:

```text
Python es divertido
```

---

## Ejercicio 4

Retornar el texto:

```text
Programar es dar instrucciones
```

---

## Ejercicio 5

Retornar el texto:

```text
Un algoritmo es una serie de pasos
```

---

## Ejercicio 6

Retornar el texto:

```text
La programación secuencial ejecuta instrucciones en orden
```

---

## Ejercicio 7

Retornar el texto:

```text
Entrada
```

---

## Ejercicio 8

Retornar el texto:

```text
Proceso
```

---

## Ejercicio 9

Retornar el texto:

```text
Salida
```

---

## Ejercicio 10

Retornar el texto:

```text
Entrada Proceso Salida
```

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender qué es programar
- entender qué es un algoritmo
- comprender la programación secuencial
- usar `print()`
- usar `input()`
- entender la lógica Entrada → Proceso → Salida
- entender la diferencia entre `print()` y `return`
- usar funciones básicas
- usar `return`