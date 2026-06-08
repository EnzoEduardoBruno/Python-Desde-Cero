# M23 — Abstracción 🏛️

En los módulos anteriores aprendimos:

* clases
* objetos
* atributos
* métodos
* constructores
* encapsulamiento
* herencia
* polimorfismo

Ahora vamos a aprender el último gran pilar de la Programación Orientada a Objetos:

# Abstracción

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es la abstracción
* crear clases abstractas
* utilizar ABC
* crear métodos abstractos
* obligar a las clases hijas a implementar métodos

---

# 🤔 ¿Qué es la abstracción?

La abstracción consiste en definir una estructura general sin especificar todos los detalles.

Permite indicar:

```text
Qué debe hacer una clase
```

sin indicar:

```text
Cómo debe hacerlo
```

---

# 🌎 Ejemplo del mundo real

Pensemos en los animales.

Todos los animales pueden:

```text
hablar
```

Pero cada animal habla de una manera distinta.

No tiene sentido definir exactamente cómo habla un animal genérico.

---

Por eso podemos crear una clase abstracta:

```python
Animal
```

y obligar a las clases hijas a implementar:

```python
hablar()
```

---

# 📌 ¿Qué es una clase abstracta?

Es una clase que sirve como modelo para otras clases.

No está pensada para crear objetos directamente.

---

# 📌 ABC

Para crear clases abstractas usamos:

```python
from abc import ABC
```

---

Ejemplo:

```python
from abc import ABC


class Animal(ABC):
    pass
```

---

# 📌 Métodos abstractos

Para definir métodos obligatorios usamos:

```python
from abc import abstractmethod
```

---

Ejemplo:

```python
from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass
```

---

# 🧠 ¿Qué significa esto?

Significa que cualquier clase hija deberá implementar:

```python
hablar()
```

obligatoriamente.

---

# 🧪 Ejemplo completo

```python
from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass
```

---

Clase hija:

```python
class Perro(Animal):

    def hablar(self):
        return "Guau"
```

---

Crear objeto:

```python
perro = Perro()
```

---

Usar método:

```python
perro.hablar()
```

Resultado:

```text
Guau
```

---

# ⚠ Error frecuente

Intentar crear una instancia de una clase abstracta.

Ejemplo:

```python
animal = Animal()
```

Esto produce un error.

---

Porque las clases abstractas no deben instanciarse.

---

# 📌 Otro ejemplo

```python
from abc import ABC
from abc import abstractmethod


class Vehiculo(ABC):

    @abstractmethod
    def mover(self):
        pass
```

---

Clase hija:

```python
class Auto(Vehiculo):

    def mover(self):
        return "Circulando"
```

---

Resultado:

```python
auto.mover()
```

```text
Circulando
```

---

# 📌 Ventajas

La abstracción permite:

* definir contratos
* organizar mejor el código
* evitar errores
* obligar a implementar métodos importantes

---

# 📌 Resumen visual

```python
from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass


class Perro(Animal):

    def hablar(self):
        return "Guau"
```

---

```python
perro = Perro()

perro.hablar()
```

Resultado:

```text
Guau
```

---

# ⚠ Importante

Una clase abstracta:

```python
class Animal(ABC)
```

sirve como plantilla.

Las clases hijas implementan los métodos necesarios.

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
class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass
```

Crear:

```python
class Perro(Animal):

    def hablar(self):
        return "Guau"
```

Retornar:

```python
perro.hablar()
```

Resultado esperado:

```text
Guau
```

---

## Ejercicio 2

Crear una clase abstracta:

```python
Vehiculo
```

con:

```python
mover()
```

abstracto.

Crear:

```python
Auto
```

que retorne:

```text
Circulando
```

---

## Ejercicio 3

Crear:

```python
Animal
```

y:

```python
Gato
```

Retornar:

```text
Miau
```

---

## Ejercicio 4

Crear:

```python
Figura
```

y:

```python
Cuadrado
```

Retornar:

```text
Área calculada
```

---

## Ejercicio 5

Crear:

```python
Empleado
```

y:

```python
Programador
```

Retornar:

```text
Programando
```

---

## Ejercicio 6

Crear:

```python
Cuenta
```

y:

```python
CuentaCorriente
```

Retornar:

```text
Consultando saldo
```

---

## Ejercicio 7

Crear:

```python
Persona
```

y:

```python
Profesor
```

Retornar:

```text
Buenos días
```

---

## Ejercicio 8

Crear:

```python
Dispositivo
```

y:

```python
Celular
```

Retornar:

```text
Encendido
```

---

## Ejercicio 9

Crear:

```python
Libro
```

y:

```python
Manual
```

Retornar:

```text
Leyendo
```

---

## Ejercicio 10

Crear:

```python
Animal
```

y:

```python
Pajaro
```

Retornar:

```text
Pío pío
```

---

# 🎯 Lo más importante que aprendiste

* La abstracción define estructuras generales.
* Las clases abstractas sirven como plantillas.
* ABC permite crear clases abstractas.
* abstractmethod obliga a implementar métodos.
* Las clases hijas deben completar los métodos abstractos.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M24 — Métodos especiales
```

donde veremos:

```python
__init__()
__str__()
__repr__()
```

y cómo personalizar el comportamiento de los objetos.