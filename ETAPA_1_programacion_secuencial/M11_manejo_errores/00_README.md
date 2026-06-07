# M11 — Manejo de errores ⚠️

En este módulo vas a aprender a manejar errores en Python.

Cuando un programa tiene un error, puede detenerse.  
Con `try`, `except` y `finally` podemos controlar esos errores y evitar que el programa se rompa.

Vamos a ver:

- `try`
- `except`
- `finally`

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender qué es un error
- usar `try`
- usar `except`
- usar `finally`
- evitar que un programa se detenga
- manejar errores comunes
- devolver mensajes claros cuando algo falla

---

# 🧠 ¿Qué es un error?

Un error ocurre cuando Python no puede ejecutar una instrucción.

Ejemplo:

```python
numero = int("hola")
```

Esto da error porque Python no puede convertir `"hola"` en número.

---

# ❌ Ejemplo sin manejo de errores

## Paso 1 — Código

```python
numero = int("hola")

print(numero)
```

## Paso 2 — Resultado

```text
ValueError: invalid literal for int() with base 10: 'hola'
```

El programa se rompe.

---

# ✅ try / except

`try` significa:

```text
intentar ejecutar este código
```

`except` significa:

```text
si ocurre un error, hacer esto otro
```

---

# 🧪 Ejemplo — try / except

## Paso 1 — Código

```python
try:
    numero = int("hola")
    print(numero)

except:
    print("Ocurrió un error")
```

## Paso 2 — Resultado

```text
Ocurrió un error
```

---

# 🔍 Explicación línea por línea

```python
try:
```

Python intenta ejecutar el bloque.

---

```python
numero = int("hola")
```

Esto genera un error porque `"hola"` no puede convertirse en número.

---

```python
except:
```

Python entra acá cuando ocurre un error.

---

```python
print("Ocurrió un error")
```

Muestra un mensaje amigable en vez de romper el programa.

---

# 📌 Capturar errores específicos

Es mejor indicar qué tipo de error queremos manejar.

---

# 🧪 Ejemplo — ValueError

```python
try:
    numero = int("hola")

except ValueError:
    print("No se pudo convertir el texto a número")
```

Resultado:

```text
No se pudo convertir el texto a número
```

---

# 📌 División por cero

Otro error común es dividir por cero.

---

# ❌ Sin manejo

```python
resultado = 10 / 0

print(resultado)
```

Resultado:

```text
ZeroDivisionError: division by zero
```

---

# ✅ Con manejo

```python
try:
    resultado = 10 / 0

except ZeroDivisionError:
    print("No se puede dividir por cero")
```

Resultado:

```text
No se puede dividir por cero
```

---

# 📌 finally

`finally` se ejecuta siempre.

No importa si hubo error o no.

---

# 🧪 Ejemplo — finally

## Paso 1 — Código

```python
try:
    numero = int("10")
    print(numero)

except ValueError:
    print("Error al convertir")

finally:
    print("Fin del programa")
```

## Paso 2 — Resultado

```text
10
Fin del programa
```

---

# 🧪 Ejemplo — finally con error

```python
try:
    numero = int("hola")
    print(numero)

except ValueError:
    print("Error al convertir")

finally:
    print("Fin del programa")
```

Resultado:

```text
Error al convertir
Fin del programa
```

---

# 📊 Resumen

| Bloque | Para qué sirve |
|---|---|
| `try` | intentar ejecutar código |
| `except` | manejar un error |
| `finally` | ejecutar código siempre |

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

Usar `try` y `except` para convertir:

```python
"10"
```

a número entero.

Retornar:

```python
10
```

---

## Ejercicio 2

Usar `try` y `except` para intentar convertir:

```python
"hola"
```

a número entero.

Si falla, retornar:

```text
Error
```

---

## Ejercicio 3

Usar `try` y `except` para dividir:

```python
10 / 2
```

Retornar el resultado.

---

## Ejercicio 4

Usar `try` y `except` para dividir:

```python
10 / 0
```

Si falla, retornar:

```text
No se puede dividir por cero
```

---

## Ejercicio 5

Capturar específicamente `ValueError`.

Intentar convertir:

```python
"python"
```

a entero.

Si falla, retornar:

```text
Valor inválido
```

---

## Ejercicio 6

Capturar específicamente `ZeroDivisionError`.

Intentar dividir:

```python
20 / 0
```

Si falla, retornar:

```text
División inválida
```

---

## Ejercicio 7

Usar `finally`.

Retornar:

```text
Finalizado
```

---

## Ejercicio 8

Usar `try`, `except` y `finally`.

Intentar convertir:

```python
"abc"
```

a entero.

Si falla, guardar:

```text
Error
```

y finalmente retornar:

```text
Finalizado
```

---

## Ejercicio 9

Usar `try` y `except`.

Intentar acceder a una posición inexistente de esta lista:

```python
numeros = [1, 2, 3]
```

posición:

```python
10
```

Si falla, retornar:

```text
Índice inválido
```

---

## Ejercicio 10

Usar `try` y `except`.

Crear este diccionario:

```python
persona = {
    "nombre": "Ana"
}
```

Intentar acceder a la clave:

```python
"edad"
```

Si falla, retornar:

```text
Clave inexistente
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

- Los errores pueden detener un programa.
- `try` intenta ejecutar código.
- `except` permite manejar errores.
- `finally` se ejecuta siempre.
- Podemos capturar errores específicos.
- Manejar errores hace que nuestros programas sean más seguros.