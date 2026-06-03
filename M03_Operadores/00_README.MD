# M03 — Operadores ➕➖✖️➗

En este módulo vas a aprender a usar operadores en Python.

Los operadores nos permiten realizar operaciones con datos.

Vamos a ver:

- operadores matemáticos
- operadores relacionales
- operadores lógicos

---

# ➕ Operadores matemáticos

Sirven para hacer cálculos.

| Operador | Significado |
|---|---|
| `+` | suma |
| `-` | resta |
| `*` | multiplicación |
| `/` | división |
| `//` | división entera |
| `%` | módulo/resto |
| `**` | potencia |

---

# 🧪 Ejemplo 1 — Suma

## Paso 1 — Código

```python
numero_1 = 10
numero_2 = 5

resultado = numero_1 + numero_2

print(resultado)
```

## Paso 2 — Resultado

```text
15
```

---

# 🧪 Ejemplo 2 — División

```python
resultado = 10 / 2

print(resultado)
```

Resultado:

```text
5.0
```

---

# 🧪 Ejemplo 3 — Módulo

El operador `%` devuelve el resto de una división.

```python
resultado = 10 % 3

print(resultado)
```

Resultado:

```text
1
```

Porque 10 dividido 3 da 3 y sobra 1.

---

# 🔍 Operadores relacionales

Sirven para comparar valores.

El resultado siempre es `True` o `False`.

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | distinto |
| `>` | mayor que |
| `<` | menor que |
| `>=` | mayor o igual |
| `<=` | menor o igual |

---

# 🧪 Ejemplo 4 — Comparación

```python
edad = 18

resultado = edad >= 18

print(resultado)
```

Resultado:

```text
True
```

---

# ⚠ Diferencia entre `=` y `==`

## `=`

Sirve para asignar un valor.

```python
edad = 18
```

## `==`

Sirve para comparar.

```python
edad == 18
```

---

# 🧠 Operadores lógicos

Sirven para combinar condiciones.

| Operador | Significado |
|---|---|
| `and` | y |
| `or` | o |
| `not` | negación |

---

# 🧪 Ejemplo 5 — and

```python
edad = 20
tiene_dni = True

puede_entrar = edad >= 18 and tiene_dni

print(puede_entrar)
```

Resultado:

```text
True
```

---

# 🧪 Ejemplo 6 — or

```python
tiene_entrada = False
esta_invitado = True

puede_entrar = tiene_entrada or esta_invitado

print(puede_entrar)
```

Resultado:

```text
True
```

---

# 🧪 Ejemplo 7 — not

```python
llueve = True

print(not llueve)
```

Resultado:

```text
False
```

---

# ✍ ¿Dónde tengo que escribir el código?

Los ejercicios se resuelven en:

```text
practica.py
```

Cada ejercicio ya tiene una función creada.

Ejemplo:

```python
def ejercicio_1():
    pass
```

Tenés que borrar `pass`, escribir tu solución y usar `return`.

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Crear dos variables numéricas y retornar la suma.

---

## Ejercicio 2

Crear dos variables numéricas y retornar la resta.

---

## Ejercicio 3

Crear dos variables numéricas y retornar la multiplicación.

---

## Ejercicio 4

Crear dos variables numéricas y retornar la división.

---

## Ejercicio 5

Crear dos variables numéricas y retornar la división entera.

---

## Ejercicio 6

Crear dos variables numéricas y retornar el resto de la división usando `%`.

---

## Ejercicio 7

Crear dos variables numéricas y retornar una potencia usando `**`.

---

## Ejercicio 8

Crear una comparación usando `>` o `<` y retornar el resultado.

---

## Ejercicio 9

Crear una comparación usando `==` y retornar el resultado.

---

## Ejercicio 10

Crear una comparación usando `!=` y retornar el resultado.

---

## Ejercicio 11

Usar `and` y retornar el resultado.

---

## Ejercicio 12

Usar `or` y retornar el resultado.

---

## Ejercicio 13

Usar `not` y retornar el resultado.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- realizar operaciones matemáticas
- usar suma, resta, multiplicación y división
- usar división entera
- usar módulo
- usar potencia
- comparar valores
- diferenciar `=` de `==`
- usar operadores lógicos
- combinar condiciones simples