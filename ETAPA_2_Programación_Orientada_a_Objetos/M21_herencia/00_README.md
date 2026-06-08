# M21 — Herencia 👨‍👦

En los módulos anteriores aprendimos:

* clases
* objetos
* atributos
* métodos
* constructores
* encapsulamiento

Ahora vamos a aprender uno de los conceptos más poderosos de la Programación Orientada a Objetos:

# Herencia

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es la herencia
* crear clases padre
* crear clases hija
* reutilizar atributos y métodos
* evitar duplicar código

---

# 🤔 ¿Qué es la herencia?

La herencia permite que una clase reutilice atributos y métodos de otra clase.

Gracias a la herencia podemos evitar repetir código.

---

# 🌎 Ejemplo del mundo real

Pensemos en los animales.

Todos los animales pueden:

```text
respirar
comer
dormir
```

Entonces podríamos crear una clase:

```python
class Animal:
```

---

Luego podríamos crear:

```python
class Perro
```

y

```python
class Gato
```

que hereden de:

```python
Animal
```

---

# 📌 Clase padre

La clase padre contiene información común.

Ejemplo:

```python
class Animal:

    def respirar(self):
        return "Respirando"
```

---

# 📌 Clase hija

La clase hija hereda de la clase padre.

Ejemplo:

```python
class Perro(Animal):
    pass
```

---

# 🔍 ¿Qué significa esto?

```python
class Perro(Animal):
```

significa:

```text
Perro hereda de Animal
```

---

# 🧪 Ejemplo completo

```python
class Animal:

    def respirar(self):
        return "Respirando"


class Perro(Animal):
    pass
```

Crear objeto:

```python
perro = Perro()
```

---

Usar método heredado:

```python
perro.respirar()
```

Resultado:

```text
Respirando
```

---

# 🧠 ¿Dónde está respirar()?

No está en:

```python
Perro
```

Está en:

```python
Animal
```

Pero gracias a la herencia:

```python
Perro
```

puede utilizarlo.

---

# 📌 Reutilización de código

Sin herencia:

```python
class Perro:

    def respirar(self):
        return "Respirando"


class Gato:

    def respirar(self):
        return "Respirando"
```

Código repetido.

---

Con herencia:

```python
class Animal:

    def respirar(self):
        return "Respirando"


class Perro(Animal):
    pass


class Gato(Animal):
    pass
```

Código reutilizado.

---

# 🧪 Otro ejemplo

```python
class Vehiculo:

    def arrancar(self):
        return "Motor encendido"


class Auto(Vehiculo):
    pass
```

Crear objeto:

```python
auto = Auto()
```

Usar método heredado:

```python
auto.arrancar()
```

Resultado:

```text
Motor encendido
```

---

# 📌 Heredar atributos

También podemos heredar atributos.

Ejemplo:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"


class Alumno(Persona):
    pass
```

---

Crear objeto:

```python
alumno = Alumno()
```

Acceder:

```python
alumno.nombre
```

Resultado:

```text
Ana
```

---

# 📌 Resumen visual

```python
class Animal:

    def respirar(self):
        return "Respirando"


class Perro(Animal):
    pass


perro = Perro()

print(perro.respirar())
```

Resultado:

```text
Respirando
```

---

# ⚠ Importante

La clase hija puede usar:

* atributos heredados
* métodos heredados

sin volver a escribirlos.

---

# 🧠 Ventajas de la herencia

* menos código repetido
* más reutilización
* programas más organizados
* mantenimiento más sencillo

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
class Animal:

    def respirar(self):
        return "Respirando"


class Perro(Animal):
    pass
```

Crear:

```python
perro = Perro()
```

Retornar:

```python
perro.respirar()
```

Resultado esperado:

```text
Respirando
```

---

## Ejercicio 2

Crear:

```python
class Vehiculo:

    def arrancar(self):
        return "Motor encendido"


class Auto(Vehiculo):
    pass
```

Retornar:

```python
auto.arrancar()
```

Resultado esperado:

```text
Motor encendido
```

---

## Ejercicio 3

Crear:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"


class Alumno(Persona):
    pass
```

Retornar:

```python
alumno.nombre
```

Resultado esperado:

```text
Ana
```

---

## Ejercicio 4

Crear:

```python
class Animal:

    def comer(self):
        return "Comiendo"


class Gato(Animal):
    pass
```

Retornar:

```python
gato.comer()
```

Resultado esperado:

```text
Comiendo
```

---

## Ejercicio 5

Crear:

```python
class Dispositivo:

    def encender(self):
        return "Encendido"


class Celular(Dispositivo):
    pass
```

Retornar:

```python
celular.encender()
```

Resultado esperado:

```text
Encendido
```

---

## Ejercicio 6

Crear:

```python
class Empleado:

    def trabajar(self):
        return "Trabajando"


class Programador(Empleado):
    pass
```

Retornar:

```python
programador.trabajar()
```

Resultado esperado:

```text
Trabajando
```

---

## Ejercicio 7

Crear:

```python
class Cuenta:

    def consultar(self):
        return "Saldo disponible"


class CuentaCorriente(Cuenta):
    pass
```

Retornar:

```python
cuenta.consultar()
```

Resultado esperado:

```text
Saldo disponible
```

---

## Ejercicio 8

Crear:

```python
class Libro:

    def leer(self):
        return "Leyendo"
        

class Manual(Libro):
    pass
```

Retornar:

```python
manual.leer()
```

Resultado esperado:

```text
Leyendo
```

---

## Ejercicio 9

Crear:

```python
class Persona:

    def saludar(self):
        return "Hola"


class Profesor(Persona):
    pass
```

Retornar:

```python
profesor.saludar()
```

Resultado esperado:

```text
Hola
```

---

## Ejercicio 10

Crear:

```python
class Vehiculo:

    def avanzar(self):
        return "Avanzando"


class Moto(Vehiculo):
    pass
```

Retornar:

```python
moto.avanzar()
```

Resultado esperado:

```text
Avanzando
```

---

# 🎯 Lo más importante que aprendiste

* La herencia permite reutilizar código.
* Una clase hija hereda de una clase padre.
* Los métodos heredados pueden utilizarse directamente.
* Los atributos heredados también pueden utilizarse.
* La herencia evita repetir código.
* Se define usando:

```python
class Hija(Padre):
    pass
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M22 — Polimorfismo
```

donde veremos cómo distintas clases pueden responder de manera diferente al mismo método.