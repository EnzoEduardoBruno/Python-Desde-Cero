# M20 — Encapsulamiento 🔒

En los módulos anteriores aprendimos:

* clases
* objetos
* atributos
* métodos
* constructores

Ahora vamos a aprender uno de los pilares fundamentales de la Programación Orientada a Objetos:

# Encapsulamiento

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es el encapsulamiento
* diferenciar atributos públicos, protegidos y privados
* utilizar `_` para atributos protegidos
* utilizar `__` para atributos privados
* comprender por qué se protege la información de un objeto

---

# 🤔 ¿Qué es el encapsulamiento?

El encapsulamiento consiste en controlar el acceso a los datos internos de un objeto.

La idea es evitar que cualquier parte del programa modifique información sensible de forma incorrecta.

---

# 🌎 Ejemplo del mundo real

Pensá en una cuenta bancaria.

Tiene información como:

```text
titular
saldo
número de cuenta
```

No sería buena idea que cualquier parte del sistema pueda modificar el saldo libremente.

Por eso se protege la información.

---

# 📌 Tipos de acceso

En Python solemos utilizar tres niveles:

```text
Público
Protegido
Privado
```

---

# 🟢 Público

Un atributo público puede ser accedido desde cualquier lugar.

Ejemplo:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Acceder:

```python
persona = Persona()

print(persona.nombre)
```

Resultado:

```text
Ana
```

---

# 📌 Convención

Cuando un atributo NO tiene guiones bajos:

```python
self.nombre
```

se considera público.

---

# 🟡 Protegido (_)

Un atributo protegido utiliza un guion bajo:

```python
self._saldo
```

Ejemplo:

```python
class Cuenta:

    def __init__(self):
        self._saldo = 1000
```

---

# ⚠ Importante

Python NO impide acceder al atributo.

Podemos hacer:

```python
cuenta = Cuenta()

print(cuenta._saldo)
```

Resultado:

```text
1000
```

---

# 📌 Entonces...

¿Por qué existe?

Porque funciona como una advertencia para otros programadores.

Significa:

```text
"Podés acceder, pero no deberías hacerlo directamente."
```

---

# 🔴 Privado (__)

Un atributo privado utiliza dos guiones bajos:

```python
self.__saldo
```

Ejemplo:

```python
class Cuenta:

    def __init__(self):
        self.__saldo = 1000
```

---

# ⚠ Intentar acceder directamente

```python
cuenta = Cuenta()

print(cuenta.__saldo)
```

Produce un error.

---

# 🧠 ¿Por qué?

Porque Python modifica internamente el nombre del atributo para protegerlo.

Este mecanismo se conoce como:

```text
Name Mangling
```

---

# 📌 Ejemplo

```python
class Persona:

    def __init__(self):
        self.__edad = 30
```

No podemos hacer:

```python
persona.__edad
```

directamente.

---

# 🧪 Comparación rápida

Público:

```python
self.nombre
```

---

Protegido:

```python
self._nombre
```

---

Privado:

```python
self.__nombre
```

---

# 📌 Resumen visual

```python
class Usuario:

    def __init__(self):

        self.nombre = "Ana"       # público

        self._email = "ana@mail.com"  # protegido

        self.__clave = "1234"     # privado
```

---

# 🧠 ¿Cuál debo usar?

En proyectos reales:

* Público → información normal
* Protegido → uso interno de la clase o herencia
* Privado → información sensible

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
class Cuenta:

    def __init__(self):
        self._saldo = 1000
```

Retornar:

```python
cuenta._saldo
```

Resultado esperado:

```python
1000
```

---

## Ejercicio 3

Crear:

```python
class Usuario:

    def __init__(self):
        self.__clave = "1234"
```

Retornar:

```python
usuario._Usuario__clave
```

Resultado esperado:

```text
1234
```

---

## Ejercicio 4

Crear:

```python
class Auto:

    def __init__(self):
        self.marca = "Toyota"
        self._modelo = "Corolla"
```

Retornar:

```python
auto._modelo
```

Resultado esperado:

```text
Corolla
```

---

## Ejercicio 5

Crear:

```python
class Alumno:

    def __init__(self):
        self.__legajo = 100
```

Retornar:

```python
alumno._Alumno__legajo
```

Resultado esperado:

```python
100
```

---

## Ejercicio 6

Crear:

```python
class Producto:

    def __init__(self):
        self.nombre = "Mouse"
        self._stock = 50
```

Retornar:

```python
producto._stock
```

Resultado esperado:

```python
50
```

---

## Ejercicio 7

Crear:

```python
class Libro:

    def __init__(self):
        self.__titulo = "Python"
```

Retornar:

```python
libro._Libro__titulo
```

Resultado esperado:

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
        self._duracion = 120
```

Retornar:

```python
pelicula._duracion
```

Resultado esperado:

```python
120
```

---

## Ejercicio 9

Crear:

```python
class Celular:

    def __init__(self):
        self.__imei = "ABC123"
```

Retornar:

```python
celular._Celular__imei
```

Resultado esperado:

```text
ABC123
```

---

## Ejercicio 10

Crear:

```python
class CuentaBancaria:

    def __init__(self):
        self.titular = "Ana"
        self._saldo = 1000
        self.__clave = "1234"
```

Retornar:

```python
cuenta._saldo
```

Resultado esperado:

```python
1000
```

---

# 🎯 Lo más importante que aprendiste

* Los atributos públicos no tienen guiones bajos.
* Los atributos protegidos utilizan un guion bajo (`_`).
* Los atributos privados utilizan dos guiones bajos (`__`).
* El encapsulamiento protege la información interna de los objetos.
* Python utiliza Name Mangling para los atributos privados.
* Los atributos privados no deben accederse directamente desde fuera de la clase.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M21 — Herencia
```

donde una clase podrá reutilizar atributos y métodos de otra clase.