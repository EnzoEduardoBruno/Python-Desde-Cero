# M28 — Proyecto final POO 🏁

Llegaste al final de la **ETAPA 2 — Programación Orientada a Objetos**.

En este módulo no vamos a aprender un concepto nuevo.

Vamos a integrar todo lo aprendido construyendo pequeños sistemas orientados a objetos.

Trabajaremos con:

- Sistema de Biblioteca
- Sistema Bancario
- Sistema de Gestión de Alumnos

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear clases para representar entidades reales
- usar constructores
- usar atributos
- crear métodos
- usar listas dentro de objetos
- aplicar composición
- usar `@dataclass`
- organizar lógica dentro de clases
- resolver problemas más parecidos a sistemas reales

---

# 📌 Temas integrados

En este proyecto vas a practicar:

- clases
- objetos
- atributos
- métodos
- `__init__`
- encapsulamiento básico
- composición
- listas
- dataclasses
- comportamiento de objetos

---

# 📚 Sistema de Biblioteca

Una biblioteca puede tener libros.

Un libro puede tener:

```text
titulo
autor
disponible
```

Ejemplo:

```python
from dataclasses import dataclass


@dataclass
class Libro:

    titulo: str
    autor: str
    disponible: bool = True
```

---

# 🧪 Crear un libro

```python
libro = Libro("Python desde cero", "Guido")
```

Acceder:

```python
libro.titulo
```

Resultado:

```text
Python desde cero
```

---

# 📌 Biblioteca con libros

```python
class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
```

Crear:

```python
biblioteca = Biblioteca()

libro = Libro("Python desde cero", "Guido")

biblioteca.agregar_libro(libro)
```

---

# 🏦 Sistema Bancario

Una cuenta bancaria puede tener:

```text
titular
saldo
```

Ejemplo:

```python
class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
```

---

# 🧪 Depositar dinero

```python
def depositar(self, monto):
    self.saldo += monto
```

---

# 🧪 Extraer dinero

```python
def extraer(self, monto):

    if monto <= self.saldo:
        self.saldo -= monto
        return "Extracción realizada"

    return "Saldo insuficiente"
```

---

# 🎓 Sistema de Gestión de Alumnos

Un alumno puede tener:

```text
nombre
notas
```

Ejemplo:

```python
class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
```

---

# 🧪 Agregar notas

```python
def agregar_nota(self, nota):
    self.notas.append(nota)
```

---

# 🧪 Calcular promedio

```python
def calcular_promedio(self):

    suma = 0

    for nota in self.notas:
        suma += nota

    return suma / len(self.notas)
```

---

# 📌 Organización del módulo

Los ejercicios se dividen así:

```text
Ejercicios 1 a 4   → Sistema de Biblioteca
Ejercicios 5 a 7   → Sistema Bancario
Ejercicios 8 a 10  → Sistema de Gestión de Alumnos
```

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1 — Crear libro

Crear una `dataclass` llamada:

```python
Libro
```

Con los atributos:

```python
titulo: str
autor: str
disponible: bool = True
```

Crear:

```python
libro = Libro("Python desde cero", "Guido")
```

Retornar:

```python
libro.titulo
```

Resultado esperado:

```text
Python desde cero
```

---

## Ejercicio 2 — Crear biblioteca

Crear una clase:

```python
Biblioteca
```

Con un atributo:

```python
self.libros = []
```

Retornar la cantidad de libros inicial.

Resultado esperado:

```python
0
```

---

## Ejercicio 3 — Agregar libro

Crear:

```python
Libro
Biblioteca
```

La biblioteca debe tener un método:

```python
agregar_libro(self, libro)
```

que agregue el libro a la lista.

Retornar la cantidad de libros.

Resultado esperado:

```python
1
```

---

## Ejercicio 4 — Buscar libro

Crear un método:

```python
buscar_libro(self, titulo)
```

Si encuentra el libro, retornar su título.

Resultado esperado:

```text
Python desde cero
```

---

## Ejercicio 5 — Crear cuenta bancaria

Crear una clase:

```python
CuentaBancaria
```

Con:

```python
titular
saldo
```

Crear:

```python
cuenta = CuentaBancaria("Ana", 1000)
```

Retornar:

```python
cuenta.saldo
```

Resultado esperado:

```python
1000
```

---

## Ejercicio 6 — Depositar dinero

Crear un método:

```python
depositar(self, monto)
```

Sumar el monto al saldo.

Crear cuenta con saldo `1000`.

Depositar `500`.

Retornar saldo.

Resultado esperado:

```python
1500
```

---

## Ejercicio 7 — Extraer dinero

Crear un método:

```python
extraer(self, monto)
```

Si el monto es menor o igual al saldo, restarlo y retornar:

```text
Extracción realizada
```

Si no alcanza el saldo, retornar:

```text
Saldo insuficiente
```

Resultado esperado:

```text
Extracción realizada
```

---

## Ejercicio 8 — Crear alumno

Crear una clase:

```python
Alumno
```

Con:

```python
nombre
notas
```

La lista de notas debe iniciar vacía.

Crear:

```python
alumno = Alumno("Juan")
```

Retornar:

```python
alumno.nombre
```

Resultado esperado:

```text
Juan
```

---

## Ejercicio 9 — Agregar nota

Crear un método:

```python
agregar_nota(self, nota)
```

Agregar la nota a la lista.

Retornar la lista de notas.

Resultado esperado:

```python
[8]
```

---

## Ejercicio 10 — Calcular promedio

Crear un método:

```python
calcular_promedio(self)
```

Agregar las notas:

```python
8
9
10
```

Retornar el promedio.

Resultado esperado:

```python
9.0
```

---

# 🎯 Lo más importante que aprendiste

- Un sistema real se puede dividir en clases.
- Las clases representan entidades del problema.
- Los objetos guardan datos y ejecutan comportamientos.
- Las listas pueden formar parte de los objetos.
- `@dataclass` simplifica clases que guardan datos.
- Los métodos permiten organizar acciones dentro de una clase.
- POO ayuda a modelar problemas reales de forma ordenada.

---

# 🏁 Cierre de la ETAPA 2

Con este módulo terminás la etapa de Programación Orientada a Objetos.

Ya trabajaste con:

```text
clases
objetos
atributos
métodos
constructores
encapsulamiento
herencia
polimorfismo
abstracción
métodos especiales
métodos estáticos
métodos de clase
composición
agregación
dataclasses
duck typing
```

A partir de acá, ya tenés una base muy sólida para construir proyectos más grandes en Python.