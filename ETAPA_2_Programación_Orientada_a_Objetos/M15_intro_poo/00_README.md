# M15 — Introducción a POO 🚀

Hasta ahora programamos usando variables, funciones, listas y diccionarios.

A este estilo se lo suele llamar programación procedural o secuencial.

A partir de este módulo vamos a comenzar a aprender un nuevo paradigma:

# Programación Orientada a Objetos (POO)

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es POO
* comprender qué es una clase
* comprender qué es un objeto
* identificar objetos del mundo real
* diferenciar clase y objeto
* entender por qué existe POO

---

# 🤔 ¿Qué es POO?

POO significa:

```text
Programación Orientada a Objetos
```

Es una forma de organizar programas utilizando objetos.

La idea es representar elementos del mundo real mediante código.

---

# 🌎 Objetos del mundo real

Miremos algunos ejemplos:

```text
Auto
Persona
Perro
Libro
Celular
Alumno
Cuenta bancaria
```

Todos ellos tienen:

### Características

Por ejemplo un auto:

```text
marca
modelo
color
año
```

---

### Comportamientos

Por ejemplo un auto puede:

```text
arrancar
frenar
acelerar
```

---

# 🏗 ¿Cómo representamos eso en Python?

Utilizando clases.

---

# 📌 ¿Qué es una clase?

Una clase es un molde.

Por ejemplo:

```text
Plano de una casa
Molde de una torta
Plantilla
```

Una clase define cómo serán los objetos.

---

# 🏠 Ejemplo

Plano:

```text
Casa
```

Casas construidas:

```text
Casa 1
Casa 2
Casa 3
```

Todas fueron creadas usando el mismo plano.

---

# 🐍 En Python

Una clase se crea con:

```python
class Persona:
    pass
```

---

# 📌 ¿Qué es un objeto?

Un objeto es una instancia de una clase.

En palabras simples:

```text
Clase = Molde

Objeto = Elemento creado a partir del molde
```

---

# 🧪 Ejemplo

Clase:

```python
class Persona:
    pass
```

Objeto:

```python
persona = Persona()
```

---

# 🧠 ¿Qué ocurrió?

Creamos una variable llamada:

```python
persona
```

que contiene un objeto de tipo:

```python
Persona
```

---

# 🧪 Otro ejemplo

```python
class Auto:
    pass
```

Creamos objetos:

```python
auto1 = Auto()

auto2 = Auto()

auto3 = Auto()
```

Todos son objetos diferentes.

---

# 📌 Clase vs Objeto

Clase:

```text
Persona
```

Objeto:

```text
Juan
Ana
Luis
```

---

Clase:

```text
Auto
```

Objeto:

```text
Ford Fiesta
Toyota Corolla
Volkswagen Golf
```

---

# 🎯 ¿Por qué existe POO?

Cuando los programas crecen:

```text
más código
más funciones
más datos
más usuarios
```

se vuelven difíciles de mantener.

POO permite:

* organizar mejor el código
* reutilizar lógica
* modelar sistemas reales
* crear aplicaciones más grandes

---

# 🧪 Ejemplo completo

```python
class Perro:
    pass

perro = Perro()
```

Creamos:

* una clase
* un objeto

Nada más.

Todavía NO veremos:

```python
__init__
self
herencia
polimorfismo
```

Eso llegará en módulos posteriores.

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 📌 Importante

En este módulo vamos a trabajar únicamente con:

* class
* objetos
* instancias

Todavía no utilizaremos atributos ni métodos.

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

Retornar:

```python
Persona.__name__
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

Crear un objeto:

```python
auto = Auto()
```

Retornar:

```python
type(auto).__name__
```

Resultado esperado:

```text
Auto
```

---

## Ejercicio 3

Crear:

```python
class Perro:
    pass
```

Crear un objeto.

Retornar:

```python
True
```

si el objeto existe.

---

## Ejercicio 4

Crear:

```python
class Alumno:
    pass
```

Crear dos objetos.

Retornar:

```python
2
```

---

## Ejercicio 5

Crear:

```python
class Producto:
    pass
```

Crear tres objetos.

Retornar:

```python
3
```

---

## Ejercicio 6

Crear:

```python
class Celular:
    pass
```

Crear un objeto.

Retornar:

```text
Celular
```

---

## Ejercicio 7

Crear:

```python
class Libro:
    pass
```

Retornar:

```python
Libro.__name__
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

```text
Pelicula
```

---

## Ejercicio 9

Crear:

```python
class Cuenta:
    pass
```

Crear un objeto.

Retornar:

```python
True
```

---

## Ejercicio 10

Crear:

```python
class Usuario:
    pass
```

Crear:

```python
usuario1
usuario2
usuario3
```

Retornar:

```python
3
```

---

# 🎯 Lo más importante que aprendiste

* POO significa Programación Orientada a Objetos.
* Una clase es un molde.
* Un objeto es una instancia.
* Podemos representar elementos del mundo real.
* Python permite crear clases mediante la palabra reservada:

```python
class
```

* Los objetos se crean usando paréntesis:

```python
objeto = Clase()
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M16 — Clases y objetos
```

donde comenzaremos a trabajar más profundamente con instancias y creación de objetos.