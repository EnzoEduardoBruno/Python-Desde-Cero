# M04 — Condicionales 🔀

En este módulo vas a aprender a tomar decisiones en Python.

Los condicionales permiten ejecutar código dependiendo de si una condición es verdadera o falsa.

Vamos a ver:

- `if`
- `else`
- `elif`

---

# 🤔 ¿Qué es un condicional?

Un condicional permite que un programa tome decisiones.

Ejemplo:

- si llueve → llevo paraguas
- si tengo hambre → como algo
- si soy mayor de edad → puedo entrar

La computadora hace exactamente lo mismo usando condiciones.

---

# ✅ if

`if` significa:

```text
si esto ocurre...
```

---

# 🧪 Ejemplo — if

## Paso 1 — Código

```python
edad = 20

if edad >= 18:
    print("Sos mayor de edad")
```

## Paso 2 — Resultado

```text
Sos mayor de edad
```

---

# 🧠 ¿Qué ocurrió?

Python evaluó:

```python
edad >= 18
```

Como el resultado fue `True`,
ejecutó el `print()`.

---

# ❌ else

`else` significa:

```text
si no ocurre lo anterior...
```

---

# 🧪 Ejemplo — else

## Paso 1 — Código

```python
edad = 15

if edad >= 18:
    print("Sos mayor de edad")

else:
    print("Sos menor de edad")
```

## Paso 2 — Resultado

```text
Sos menor de edad
```

---

# 🔀 elif

`elif` significa:

```text
si lo anterior no ocurrió,
probar esta otra condición
```

---

# 🧪 Ejemplo — elif

## Paso 1 — Código

```python
nota = 7

if nota >= 9:
    print("Excelente")

elif nota >= 6:
    print("Aprobado")

else:
    print("Desaprobado")
```

## Paso 2 — Resultado

```text
Aprobado
```

---

# 📌 Importante — Indentación

Python usa indentación para saber qué código pertenece a cada bloque.

---

# ✅ Correcto

```python
edad = 20

if edad >= 18:
    print("Mayor")
```

---

# ❌ Incorrecto

```python
edad = 20

if edad >= 18:
print("Mayor")
```

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

Cada ejercicio ya tiene una función creada.

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Usar `if` para retornar:

```text
Mayor
```

si una edad es mayor o igual a 18.

---

## Ejercicio 2

Usar `if` y `else`
para retornar:

```text
Aprobado
```

o:

```text
Desaprobado
```

---

## Ejercicio 3

Usar `if`, `elif` y `else`
para retornar:

- Excelente
- Aprobado
- Desaprobado

---

## Ejercicio 4

Retornar `True`
si un número es positivo.

---

## Ejercicio 5

Retornar `False`
si un número es negativo.

---

## Ejercicio 6

Usar `if`
para verificar si una persona puede votar.

---

## Ejercicio 7

Usar `if` y `else`
para verificar si una persona puede entrar.

---

## Ejercicio 8

Usar `elif`
para clasificar una nota.

---

## Ejercicio 9

Usar operadores lógicos dentro de un condicional.

---

## Ejercicio 10

Crear un condicional libre
y retornar cualquier texto.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- usar `if`
- usar `else`
- usar `elif`
- tomar decisiones
- usar condiciones
- combinar operadores lógicos
- entender indentación
- controlar el flujo de un programa