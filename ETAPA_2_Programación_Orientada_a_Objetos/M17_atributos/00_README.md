# M17 — Atributos 🏷️

En los módulos anteriores aprendimos:

* qué es una clase
* qué es un objeto
* cómo crear instancias

Ahora vamos a aprender algo fundamental en POO:

# Los atributos

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es un atributo
* crear atributos de instancia
* comprender el uso de `self`
* acceder a atributos desde un objeto
* almacenar información dentro de objetos

---

# 🤔 ¿Qué es un atributo?

Un atributo es una característica de un objeto.

Por ejemplo:

```text
Persona
```

puede tener:

```text
nombre
edad
altura
```

---

```text
Auto
```

puede tener:

```text
marca
modelo
color
```

---

```text
Perro
```

puede tener:

```text
nombre
raza
edad
```

---

# 🌎 Objetos del mundo real

Objeto:

```text
Persona
```

Atributos:

```text
nombre
edad
```

---

Objeto:

```text
Auto
```

Atributos:

```text
marca
modelo
```

---

# 🐍 En Python

Creamos una clase:

```python
class Persona:
    pass
```

Pero por ahora no tiene información.

---

# 📌 Atributos de instancia

Los atributos de instancia pertenecen a cada objeto.

Ejemplo:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

---

# 🔍 Explicación

```python
self.nombre
```

significa:

```text
el atributo nombre de ESTE objeto
```

---

# 📌 ¿Qué es self?

`self` representa al objeto actual.

No es una palabra reservada.

Pero por convención siempre usamos:

```python
self
```

---

# 🧪 Ejemplo

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Crear objeto:

```python
persona = Persona()
```

---

Acceder al atributo:

```python
print(persona.nombre)
```

Resultado:

```text
Ana
```

---

# 📌 **init**()

El método:

```python
__init__()
```

se ejecuta automáticamente cuando se crea un objeto.

Ejemplo:

```python
persona = Persona()
```

Python ejecuta:

```python
__init__()
```

automáticamente.

---

# 🧠 Visualmente

Clase:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

---

Objeto:

```python
persona = Persona()
```

---

Atributo:

```python
persona.nombre
```

---

Resultado:

```text
Ana
```

---

# 🧪 Otro ejemplo

```python
class Auto:

    def __init__(self):
        self.marca = "Toyota"
```

---

Crear objeto:

```python
auto = Auto()
```

---

Acceder:

```python
print(auto.marca)
```

---

Resultado:

```text
Toyota
```

---

# 📌 Acceso a atributos

La sintaxis es:

```python
objeto.atributo
```

Ejemplos:

```python
persona.nombre
```

```python
auto.marca
```

```python
libro.titulo
```

---

# ⚠ Importante

Todavía NO veremos:

```python
def saludar(self):
```

porque eso corresponde al módulo siguiente.

---

Tampoco veremos:

```python
__init__(self, nombre)
```

con parámetros.

Eso llegará más adelante.

---

Por ahora solamente:

* atributos
* self
* acceso a atributos

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

## Ejercicio 1

Crear:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Retornar:

```python
persona.nombre
```

Resultado esperado:

```text
Ana
```

---

## Ejercicio 2

Crear:

```python
class Auto:

    def __init__(self):
        self.marca = "Toyota"
```

Retornar:

```text
Toyota
```

---

## Ejercicio 3

Crear:

```python
class Perro:

    def __init__(self):
        self.nombre = "Firulais"
```

Retornar:

```text
Firulais
```

---

## Ejercicio 4

Crear:

```python
class Alumno:

    def __init__(self):
        self.edad = 20
```

Retornar:

```python
20
```

---

## Ejercicio 5

Crear:

```python
class Producto:

    def __init__(self):
        self.precio = 1500
```

Retornar:

```python
1500
```

---

## Ejercicio 6

Crear:

```python
class Celular:

    def __init__(self):
        self.modelo = "Samsung"
```

Retornar:

```text
Samsung
```

---

## Ejercicio 7

Crear:

```python
class Libro:

    def __init__(self):
        self.titulo = "Python"
```

Retornar:

```text
Python
```

---

## Ejercicio 8

Crear:

```python
class Pelicula:

    def __init__(self):
        self.genero = "Acción"
```

Retornar:

```text
Acción
```

---

## Ejercicio 9

Crear:

```python
class Cuenta:

    def __init__(self):
        self.saldo = 1000
```

Retornar:

```python
1000
```

---

## Ejercicio 10

Crear:

```python
class Usuario:

    def __init__(self):
        self.nombre = "Admin"
```

Retornar:

```text
Admin
```

---

# 🎯 Lo más importante que aprendiste

* Un atributo es una característica de un objeto.
* Los atributos de instancia pertenecen a cada objeto.
* `self` representa al objeto actual.
* `__init__()` se ejecuta automáticamente al crear una instancia.
* Podemos acceder a los atributos usando:

```python
objeto.atributo
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M18 — Métodos
```

donde los objetos empezarán a tener comportamientos además de datos.