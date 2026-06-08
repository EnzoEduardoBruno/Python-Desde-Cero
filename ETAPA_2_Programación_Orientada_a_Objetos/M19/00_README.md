# M19 — Constructores 🏗️

En los módulos anteriores aprendimos:

- clases
- objetos
- atributos
- métodos
- self

Ahora vamos a aprender a crear objetos con datos personalizados usando constructores.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender qué es un constructor
- usar `__init__`
- inicializar objetos
- enviar parámetros al crear objetos
- crear objetos con datos diferentes
- guardar parámetros dentro de atributos

---

# 📌 ¿Qué es un constructor?

Un constructor es un método especial que se ejecuta automáticamente cuando creamos un objeto.

En Python, el constructor se llama:

```python
__init__
```

---

# 🧪 Ejemplo básico

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Cuando hacemos:

```python
persona = Persona()
```

Python ejecuta automáticamente:

```python
__init__()
```

---

# 📌 Constructor con parámetros

Hasta ahora teníamos datos fijos:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Pero ahora podemos recibir datos al crear el objeto:

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
```

---

# 🧪 Ejemplo completo

## Paso 1 — Código

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

persona = Persona("Ana")

print(persona.nombre)
```

## Paso 2 — Resultado

```text
Ana
```

---

# 🔍 Explicación línea por línea

```python
def __init__(self, nombre):
```

Define el constructor.

```python
self
```

Representa al objeto actual.

```python
nombre
```

Es un parámetro.

```python
self.nombre = nombre
```

Guarda el valor recibido dentro del objeto.

---

# 🧠 ¿Qué significa esto?

Cuando hacemos:

```python
persona = Persona("Ana")
```

el valor:

```text
Ana
```

entra al parámetro:

```python
nombre
```

y luego se guarda en:

```python
self.nombre
```

---

# 📌 Objetos con datos diferentes

```python
persona1 = Persona("Ana")
persona2 = Persona("Luis")
```

Ahora:

```python
persona1.nombre
```

vale:

```text
Ana
```

y:

```python
persona2.nombre
```

vale:

```text
Luis
```

---

# 🧪 Otro ejemplo

```python
class Auto:

    def __init__(self, marca):
        self.marca = marca

auto = Auto("Toyota")

print(auto.marca)
```

Resultado:

```text
Toyota
```

---

# 📌 Constructor con más de un parámetro

Podemos recibir varios datos:

```python
class Alumno:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Crear objeto:

```python
alumno = Alumno("Ana", 20)
```

Acceder:

```python
print(alumno.nombre)
print(alumno.edad)
```

Resultado:

```text
Ana
20
```

---

# ⚠ Error frecuente

Si la clase espera un parámetro:

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
```

Esto da error:

```python
persona = Persona()
```

Porque falta enviar el nombre.

Correcto:

```python
persona = Persona("Ana")
```

---

# 📌 Resumen visual

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


persona = Persona("Ana")

print(persona.nombre)
```

Resultado:

```text
Ana
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

## Ejercicio 1

Crear:

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
```

Crear:

```python
persona = Persona("Ana")
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

    def __init__(self, marca):
        self.marca = marca
```

Crear:

```python
auto = Auto("Toyota")
```

Retornar:

```python
auto.marca
```

Resultado esperado:

```text
Toyota
```

---

## Ejercicio 3

Crear:

```python
class Perro:

    def __init__(self, nombre):
        self.nombre = nombre
```

Crear:

```python
perro = Perro("Firulais")
```

Retornar:

```python
perro.nombre
```

Resultado esperado:

```text
Firulais
```

---

## Ejercicio 4

Crear:

```python
class Alumno:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Crear:

```python
alumno = Alumno("Ana", 20)
```

Retornar:

```python
alumno.edad
```

Resultado esperado:

```python
20
```

---

## Ejercicio 5

Crear:

```python
class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
```

Crear:

```python
producto = Producto("Mouse", 1500)
```

Retornar:

```python
producto.precio
```

Resultado esperado:

```python
1500
```

---

## Ejercicio 6

Crear una clase `Celular` que reciba `marca` y `modelo`.

Crear:

```python
celular = Celular("Samsung", "A54")
```

Retornar:

```python
celular.modelo
```

Resultado esperado:

```text
A54
```

---

## Ejercicio 7

Crear una clase `Libro` que reciba `titulo` y `autor`.

Crear:

```python
libro = Libro("Python", "Guido")
```

Retornar:

```python
libro.autor
```

Resultado esperado:

```text
Guido
```

---

## Ejercicio 8

Crear una clase `Pelicula` que reciba `titulo` y `genero`.

Crear:

```python
pelicula = Pelicula("Matrix", "Ciencia ficción")
```

Retornar:

```python
pelicula.genero
```

Resultado esperado:

```text
Ciencia ficción
```

---

## Ejercicio 9

Crear una clase `Cuenta` que reciba `titular` y `saldo`.

Crear:

```python
cuenta = Cuenta("Ana", 1000)
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

## Ejercicio 10

Crear una clase `Usuario` que reciba `nombre`, `email` y `rol`.

Crear:

```python
usuario = Usuario("Admin", "admin@mail.com", "administrador")
```

Retornar:

```python
usuario.rol
```

Resultado esperado:

```text
administrador
```

---

# 🎯 Lo más importante que aprendiste

- `__init__` es el constructor.
- El constructor se ejecuta automáticamente al crear un objeto.
- Los parámetros permiten crear objetos con datos diferentes.
- `self.atributo = parametro` guarda información dentro del objeto.
- Podemos acceder a los datos usando:

```python
objeto.atributo
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M20 — Encapsulamiento
```

donde veremos cómo proteger los datos internos de un objeto.