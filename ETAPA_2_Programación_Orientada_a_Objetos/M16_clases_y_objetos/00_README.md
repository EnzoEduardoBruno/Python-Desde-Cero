# M16 — Clases y Objetos 🏗️

En el módulo anterior aprendimos qué es la Programación Orientada a Objetos (POO) y la diferencia entre una clase y un objeto.

Ahora vamos a profundizar en la creación de clases y objetos en Python.

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* crear clases en Python
* crear objetos a partir de clases
* crear múltiples instancias
* identificar el tipo de un objeto
* entender qué significa instanciar una clase
* diferenciar una clase de un objeto

---

# 📌 Recordatorio

Una clase es un molde.

Un objeto es una instancia creada a partir de ese molde.

---

# 🏠 Ejemplo del mundo real

Clase:

```text
Auto
```

Objetos:

```text
Mi auto
Tu auto
Auto de Juan
```

Todos son autos, pero son objetos diferentes.

---

# 🐍 Crear una clase

Para crear una clase usamos:

```python
class Persona:
    pass
```

---

# 🔍 Explicación

```python
class Persona:
```

Crea una clase llamada:

```text
Persona
```

---

```python
pass
```

Indica que por ahora la clase está vacía.

---

# 📌 Crear un objeto

Una vez creada la clase:

```python
class Persona:
    pass
```

podemos crear objetos:

```python
persona = Persona()
```

---

# 🧠 ¿Qué ocurrió?

Python creó un objeto de tipo:

```text
Persona
```

y lo guardó en la variable:

```python
persona
```

---

# 🧪 Crear varios objetos

```python
class Persona:
    pass

persona1 = Persona()

persona2 = Persona()

persona3 = Persona()
```

---

# 📌 ¿Son el mismo objeto?

No.

Cada llamada a:

```python
Persona()
```

crea un objeto nuevo.

---

# 🧪 Verificar el tipo

Podemos usar:

```python
type()
```

Ejemplo:

```python
class Auto:
    pass

auto = Auto()

print(type(auto))
```

Resultado:

```text
<class '__main__.Auto'>
```

---

# 🧪 Obtener solamente el nombre

```python
type(auto).__name__
```

Resultado:

```text
Auto
```

---

# 📌 Instancia

Una instancia es un objeto creado a partir de una clase.

Ejemplo:

Clase:

```python
class Perro:
    pass
```

Instancia:

```python
perro = Perro()
```

---

# 🧪 Ejemplo completo

```python
class Libro:
    pass

libro1 = Libro()

libro2 = Libro()

libro3 = Libro()
```

Tenemos:

* una clase
* tres objetos

---

# ⚠ Importante

Todavía NO veremos:

```python
self
```

---

Tampoco veremos:

```python
__init__
```

---

Tampoco veremos:

```python
atributos
```

---

Eso llegará en los próximos módulos.

Por ahora solamente trabajaremos con:

* clases
* objetos
* instancias

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 📌 Importante

Las clases deben crearse dentro de cada función.

Ejemplo:

```python
def ejercicio_1():

    class Persona:
        pass

    return Persona.__name__
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
    pass
```

Crear un objeto:

```python
persona = Persona()
```

Retornar:

```python
type(persona).__name__
```

Resultado esperado:

```text
Persona
```

---

## Ejercicio 2

Crear:

```python
class Auto:
    pass
```

Crear dos objetos.

Retornar:

```python
2
```

---

## Ejercicio 3

Crear:

```python
class Perro:
    pass
```

Crear tres objetos.

Retornar:

```python
3
```

---

## Ejercicio 4

Crear:

```python
class Alumno:
    pass
```

Crear un objeto.

Retornar:

```python
True
```

si el objeto existe.

---

## Ejercicio 5

Crear:

```python
class Producto:
    pass
```

Crear un objeto.

Retornar:

```python
"Producto"
```

---

## Ejercicio 6

Crear:

```python
class Celular:
    pass
```

Crear dos objetos.

Retornar:

```python
2
```

---

## Ejercicio 7

Crear:

```python
class Libro:
    pass
```

Crear cuatro objetos.

Retornar:

```python
4
```

---

## Ejercicio 8

Crear:

```python
class Pelicula:
    pass
```

Crear un objeto.

Retornar:

```python
"Pelicula"
```

---

## Ejercicio 9

Crear:

```python
class Cuenta:
    pass
```

Crear dos objetos.

Retornar:

```python
2
```

---

## Ejercicio 10

Crear:

```python
class Usuario:
    pass
```

Crear cinco objetos.

Retornar:

```python
5
```

---

# 🎯 Lo más importante que aprendiste

* Una clase es un molde.
* Un objeto es una instancia.
* Podemos crear múltiples objetos desde una misma clase.
* Cada objeto es independiente.
* Python crea objetos usando:

```python
Clase()
```

* Podemos conocer el tipo usando:

```python
type()
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M17 — Atributos
```

donde los objetos comenzarán a tener información propia.