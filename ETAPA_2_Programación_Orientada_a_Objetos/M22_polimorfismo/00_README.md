# M22 — Polimorfismo 🎭

En los módulos anteriores aprendimos:

* clases
* objetos
* atributos
* métodos
* constructores
* encapsulamiento
* herencia

Ahora vamos a aprender otro de los pilares fundamentales de la Programación Orientada a Objetos:

# Polimorfismo

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es el polimorfismo
* utilizar el mismo método en distintas clases
* comprender cómo un mismo mensaje genera comportamientos diferentes
* aprovechar la herencia para crear comportamientos personalizados

---

# 🤔 ¿Qué es el polimorfismo?

La palabra polimorfismo significa:

```text
muchas formas
```

En programación significa que varias clases pueden tener un método con el mismo nombre, pero comportarse de manera diferente.

---

# 🌎 Ejemplo del mundo real

Pensemos en los animales.

Todos pueden:

```text
hablar
```

Pero cada uno lo hace de manera distinta.

---

Perro:

```text
Guau
```

---

Gato:

```text
Miau
```

---

Vaca:

```text
Muuu
```

---

Todos responden al mismo mensaje:

```python
hablar()
```

pero cada uno responde diferente.

Eso es polimorfismo.

---

# 🧪 Ejemplo básico

```python
class Animal:

    def hablar(self):
        return "Sonido"


class Perro(Animal):

    def hablar(self):
        return "Guau"


class Gato(Animal):

    def hablar(self):
        return "Miau"
```

---

Crear objetos:

```python
perro = Perro()

gato = Gato()
```

---

Usar el mismo método:

```python
perro.hablar()

gato.hablar()
```

Resultado:

```text
Guau

Miau
```

---

# 📌 Mismo método

Las clases tienen:

```python
hablar()
```

---

Pero el resultado es diferente:

```text
Perro → Guau

Gato → Miau
```

---

# 🧠 ¿Cómo es posible?

Porque las clases hijas reemplazan el método heredado.

---

Clase padre:

```python
class Animal:

    def hablar(self):
        return "Sonido"
```

---

Clase hija:

```python
class Perro(Animal):

    def hablar(self):
        return "Guau"
```

---

La versión de la clase hija tiene prioridad.

---

# 📌 Otro ejemplo

```python
class Vehiculo:

    def mover(self):
        return "Moviéndose"
```

---

```python
class Auto(Vehiculo):

    def mover(self):
        return "Circulando por la calle"
```

---

```python
class Avion(Vehiculo):

    def mover(self):
        return "Volando"
```

---

Resultado:

```python
auto.mover()
```

```text
Circulando por la calle
```

---

```python
avion.mover()
```

```text
Volando
```

---

# 📌 Ventajas

El polimorfismo permite:

* reutilizar código
* escribir programas más flexibles
* trabajar con distintas clases de forma uniforme

---

# 🧪 Ejemplo completo

```python
class Animal:

    def hablar(self):
        return "Sonido"


class Perro(Animal):

    def hablar(self):
        return "Guau"


perro = Perro()

print(perro.hablar())
```

Resultado:

```text
Guau
```

---

# 📌 Resumen visual

```python
class Animal:

    def hablar(self):
        return "Sonido"


class Perro(Animal):

    def hablar(self):
        return "Guau"


class Gato(Animal):

    def hablar(self):
        return "Miau"
```

---

```python
perro.hablar()
```

Resultado:

```text
Guau
```

---

```python
gato.hablar()
```

Resultado:

```text
Miau
```

---

# ⚠ Importante

El método tiene el mismo nombre:

```python
hablar()
```

Pero el comportamiento cambia según el objeto.

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

    def hablar(self):
        return "Sonido"


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

Crear:

```python
class Animal:

    def hablar(self):
        return "Sonido"


class Gato(Animal):

    def hablar(self):
        return "Miau"
```

Retornar:

```python
gato.hablar()
```

Resultado esperado:

```text
Miau
```

---

## Ejercicio 3

Crear:

```python
class Vehiculo:

    def mover(self):
        return "Moviéndose"


class Auto(Vehiculo):

    def mover(self):
        return "Circulando"
```

Retornar:

```python
auto.mover()
```

Resultado esperado:

```text
Circulando
```

---

## Ejercicio 4

Crear una clase `Avion` que herede de `Vehiculo` y sobrescriba:

```python
mover()
```

para retornar:

```text
Volando
```

---

## Ejercicio 5

Crear una clase `Vaca` que herede de `Animal` y sobrescriba:

```python
hablar()
```

para retornar:

```text
Muuu
```

---

## Ejercicio 6

Crear una clase `Moto` que herede de `Vehiculo` y sobrescriba:

```python
mover()
```

para retornar:

```text
Acelerando
```

---

## Ejercicio 7

Crear una clase `Profesor` que herede de `Persona` y sobrescriba:

```python
saludar()
```

para retornar:

```text
Buenos días
```

---

## Ejercicio 8

Crear una clase `Alumno` que herede de `Persona` y sobrescriba:

```python
saludar()
```

para retornar:

```text
Hola profe
```

---

## Ejercicio 9

Crear una clase `Camion` que herede de `Vehiculo` y sobrescriba:

```python
mover()
```

para retornar:

```text
Transportando carga
```

---

## Ejercicio 10

Crear una clase `Pajaro` que herede de `Animal` y sobrescriba:

```python
hablar()
```

para retornar:

```text
Pío pío
```

---

# 🎯 Lo más importante que aprendiste

* Polimorfismo significa muchas formas.
* Distintas clases pueden tener métodos con el mismo nombre.
* El mismo método puede producir resultados diferentes.
* Las clases hijas pueden sobrescribir métodos heredados.
* El comportamiento depende del objeto que ejecuta el método.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M23 — Abstracción
```

donde veremos cómo definir estructuras generales que otras clases deberán implementar.