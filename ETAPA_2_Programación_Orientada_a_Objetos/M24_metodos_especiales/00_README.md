# M24 — Métodos especiales ✨

En los módulos anteriores aprendimos:

* clases
* objetos
* atributos
* métodos
* constructores
* encapsulamiento
* herencia
* polimorfismo
* abstracción

Ahora vamos a aprender los **métodos especiales**.

En este módulo veremos:

* `__str__`
* `__repr__`

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué son los métodos especiales
* sobrescribir `__str__`
* sobrescribir `__repr__`
* personalizar cómo se muestran los objetos
* diferenciar `__str__` y `__repr__`

---

# 🤔 ¿Qué son los métodos especiales?

Son métodos que Python ejecuta automáticamente.

Se reconocen porque comienzan y terminan con:

```python
__
```

Por ejemplo:

```python
__str__

__repr__

__len__

__eq__
```

---

# 📌 ¿Para qué sirve `__str__`?

Permite definir cómo se mostrará un objeto cuando usamos:

```python
print(objeto)
```

---

# 🧪 Ejemplo sin `__str__`

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


persona = Persona("Ana")

print(persona)
```

Resultado:

```text
<__main__.Persona object at 0x000001F4...>
```

No es muy útil.

---

# 🧪 Ejemplo con `__str__`

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


persona = Persona("Ana")

print(persona)
```

Resultado:

```text
Ana
```

---

# 📌 ¿Para qué sirve `__repr__`?

`__repr__` devuelve una representación más técnica del objeto.

Python la usa cuando escribimos:

```python
objeto
```

en la consola o cuando el objeto está dentro de una lista.

---

# 🧪 Ejemplo

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Persona('{self.nombre}')"


persona = Persona("Ana")

print(repr(persona))
```

Resultado:

```text
Persona('Ana')
```

---

# 📌 Diferencias

`__str__`

```text
Pensado para usuarios.
Más amigable.
Se usa con print().
```

---

`__repr__`

```text
Pensado para programadores.
Más técnico.
Se usa con repr().
```

---

# 🧪 Ejemplo completo

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre}"

    def __repr__(self):
        return f"Persona('{self.nombre}')"


persona = Persona("Ana")

print(persona)

print(repr(persona))
```

Resultado:

```text
Nombre: Ana

Persona('Ana')
```

---

# 📌 Resumen visual

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return f"Persona('{self.nombre}')"
```

---

```python
print(persona)
```

Resultado:

```text
Ana
```

---

```python
repr(persona)
```

Resultado:

```text
Persona('Ana')
```

---

# ⚠ Importante

* `__str__` → pensado para personas.
* `__repr__` → pensado para programadores.
* Ambos son métodos especiales.
* Python los ejecuta automáticamente.

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

    def __str__(self):
        return self.nombre
```

Retornar:

```python
str(persona)
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

    def __str__(self):
        return self.marca
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

    def __init__(self):
        self.nombre = "Firulais"

    def __repr__(self):
        return f"Perro('{self.nombre}')"
```

Resultado esperado:

```text
Perro('Firulais')
```

---

## Ejercicio 4

Crear una clase `Libro`.

Implementar:

```python
__str__
```

Resultado esperado:

```text
Python desde cero
```

---

## Ejercicio 5

Crear una clase `Alumno`.

Implementar:

```python
__repr__
```

Resultado esperado:

```text
Alumno('Ana')
```

---

## Ejercicio 6

Crear una clase `Celular`.

Implementar:

```python
__str__
```

Resultado esperado:

```text
Samsung
```

---

## Ejercicio 7

Crear una clase `Producto`.

Implementar:

```python
__repr__
```

Resultado esperado:

```text
Producto('Mouse')
```

---

## Ejercicio 8

Crear una clase `Cuenta`.

Implementar:

```python
__str__
```

Resultado esperado:

```text
Saldo: 1000
```

---

## Ejercicio 9

Crear una clase `Pelicula`.

Implementar:

```python
__repr__
```

Resultado esperado:

```text
Pelicula('Matrix')
```

---

## Ejercicio 10

Crear una clase `Usuario`.

Implementar:

```python
__str__
```

Resultado esperado:

```text
admin@mail.com
```

---

# 🎯 Lo más importante que aprendiste

* Los métodos especiales comienzan y terminan con `__`.
* `__str__` personaliza `print(objeto)`.
* `__repr__` personaliza `repr(objeto)`.
* Python los ejecuta automáticamente.
* Permiten que nuestros objetos sean mucho más legibles.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M25 — Métodos estáticos y de clase
```

donde veremos:

```python
@staticmethod

@classmethod
```

y cuándo conviene usar cada uno.