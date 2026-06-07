# M08 — Listas 📋

En este módulo vas a aprender a trabajar con listas.

Las listas permiten guardar varios valores dentro de una misma variable.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* crear listas
* acceder a elementos
* agregar elementos
* eliminar elementos
* insertar elementos
* contar elementos
* recorrer listas con for
* buscar elementos usando in

---

# 🧠 ¿Qué es una lista?

Una lista es una colección de elementos.

Ejemplo:

```python
frutas = ["manzana", "banana", "pera"]
```

En este caso:

```text
frutas
```

es el nombre de la variable.

Los corchetes:

```python
[]
```

indican que estamos creando una lista.

Cada elemento está separado por comas.

---

# 🧪 Ejemplo — Crear una lista

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

print(frutas)
```

## Paso 2 — Resultado

```text
['manzana', 'banana', 'pera']
```

---

# 📌 Posiciones de una lista

Cada elemento tiene una posición.

```text
manzana   banana   pera
   0         1       2
```

La primera posición siempre es:

```text
0
```

---

# 🧪 Ejemplo — Obtener el primer elemento

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

print(frutas[0])
```

## Paso 2 — Resultado

```text
manzana
```

---

# 🧪 Ejemplo — Obtener el último elemento

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

print(frutas[-1])
```

## Paso 2 — Resultado

```text
pera
```

---

# 📌 append()

append() sirve para agregar elementos al final de una lista.

---

# 🧪 Ejemplo — append()

## Paso 1 — Código

```python
frutas = ["manzana", "banana"]

frutas.append("pera")

print(frutas)
```

## Paso 2 — Resultado

```text
['manzana', 'banana', 'pera']
```

---

# 🔍 Explicación

```python
frutas.append("pera")
```

significa:

```text
agregar "pera" al final de la lista
```

---

# 📌 remove()

remove() sirve para eliminar elementos.

---

# 🧪 Ejemplo — remove()

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

frutas.remove("banana")

print(frutas)
```

## Paso 2 — Resultado

```text
['manzana', 'pera']
```

---

# 🔍 Explicación

```python
frutas.remove("banana")
```

significa:

```text
eliminar "banana" de la lista
```

---

# 📌 insert()

insert() sirve para insertar elementos en una posición específica.

---

# 🧪 Ejemplo — insert()

## Paso 1 — Código

```python
frutas = ["manzana", "pera"]

frutas.insert(1, "banana")

print(frutas)
```

## Paso 2 — Resultado

```text
['manzana', 'banana', 'pera']
```

---

# 🔍 Explicación

```python
frutas.insert(1, "banana")
```

significa:

```text
insertar "banana" en la posición 1
```

---

# 📌 len()

len() sirve para contar elementos.

---

# 🧪 Ejemplo — len()

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

print(len(frutas))
```

## Paso 2 — Resultado

```text
3
```

---

# 🔍 Explicación

```python
len(frutas)
```

significa:

```text
cantidad de elementos de la lista
```

---

# 📌 Recorrer listas con for

Podemos recorrer todos los elementos de una lista.

---

# 🧪 Ejemplo — Recorrer lista

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)
```

## Paso 2 — Resultado

```text
manzana
banana
pera
```

---

# 🔍 Explicación línea por línea

```python
for fruta in frutas:
```

significa:

```text
recorrer todos los elementos de la lista frutas
```

---

```python
print(fruta)
```

significa:

```text
mostrar cada elemento
```

---

# 📌 Operador in

Sirve para verificar si un elemento existe dentro de una lista.

---

# 🧪 Ejemplo — in

## Paso 1 — Código

```python
frutas = ["manzana", "banana", "pera"]

print("banana" in frutas)
```

## Paso 2 — Resultado

```text
True
```

---

# 🔍 Explicación

```python
"banana" in frutas
```

significa:

```text
¿banana existe dentro de frutas?
```

Si existe:

```python
True
```

Si no existe:

```python
False
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

* NO borrar `def`
* NO cambiar el nombre de la función
* borrar `pass`
* escribir la solución dentro de la función
* usar `return`

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo, ejecutar:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Retornar la lista completa.

---

## Ejercicio 2

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Retornar el primer elemento de la lista.

---

## Ejercicio 3

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Retornar el último elemento de la lista.

---

## Ejercicio 4

Crear la lista:

```python
colores = ["rojo", "verde"]
```

Agregar `"azul"` usando:

```python
append()
```

Retornar la lista completa.

---

## Ejercicio 5

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Eliminar `"verde"` usando:

```python
remove()
```

Retornar la lista completa.

---

## Ejercicio 6

Crear la lista:

```python
colores = ["rojo", "azul"]
```

Insertar `"verde"` en la posición `1` usando:

```python
insert()
```

Retornar la lista completa.

---

## Ejercicio 7

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Retornar la cantidad de elementos usando:

```python
len()
```

---

## Ejercicio 8

Crear una lista vacía llamada:

```python
numeros = []
```

Usar:

```python
for
append()
```

para agregar los números del:

```text
0 al 4
```

Retornar:

```python
[0, 1, 2, 3, 4]
```

---

## Ejercicio 9

Crear la lista:

```python
colores = ["rojo", "verde", "azul"]
```

Verificar si:

```python
"verde"
```

existe dentro de la lista usando:

```python
in
```

Retornar:

```python
True
```

---

## Ejercicio 10

Crear la lista:

```python
lenguajes = ["Python", "JavaScript", "Java"]
```

Luego:

### Paso 1

Agregar:

```python
"C#"
```

usando:

```python
append()
```

### Paso 2

Eliminar:

```python
"Java"
```

usando:

```python
remove()
```

### Paso 3

Insertar:

```python
"TypeScript"
```

en la posición:

```python
1
```

usando:

```python
insert()
```

### Paso 4

Retornar la lista final.

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

# ⚠ Importante

* No borrar los nombres de las funciones.
* No cambiar el nombre del archivo.
* Recordar guardar antes de ejecutar el test.
* Solo modificar el código dentro de cada función.