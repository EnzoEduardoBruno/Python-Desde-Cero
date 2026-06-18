# M26 — Composición y agregación 🧩

En los módulos anteriores aprendimos:

- clases
- objetos
- atributos
- métodos
- constructores
- encapsulamiento
- herencia
- polimorfismo
- abstracción
- métodos especiales
- métodos estáticos y de clase

Ahora vamos a aprender cómo los objetos pueden relacionarse entre sí.

Veremos:

- ES UN
- Tiene un
- Usa un

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender las relaciones entre objetos
- diferenciar herencia, composición y agregación
- crear objetos dentro de otros objetos
- pasar objetos como parámetros
- modelar sistemas reales

---

# 📌 Relaciones entre clases

En Programación Orientada a Objetos existen tres relaciones muy comunes:

| Concepto | Relación | Ejemplo |
|----------|----------|---------|
| Herencia | ES UN | Perro es un Animal |
| Composición | TIENE UN | Auto tiene un Motor |
| Agregación | USA UN | Curso usa un Profesor |

---

# 🐶 Herencia → ES UN

Ya la vimos anteriormente.

```python
class Animal:
    pass


class Perro(Animal):
    pass
```

```text
Perro ES un Animal
```

---

# 🚗 Composición → TIENE UN

En composición, un objeto contiene a otro objeto.

Ejemplo:

```python
class Motor:

    def arrancar(self):

        return "Motor encendido"


class Auto:

    def __init__(self):

        self.motor = Motor()
```

---

Crear objeto:

```python
auto = Auto()
```

Usar el motor:

```python
auto.motor.arrancar()
```

Resultado:

```text
Motor encendido
```

---

# 🔍 Explicación

```python
self.motor = Motor()
```

El objeto `Motor` se crea dentro del `Auto`.

Por eso decimos:

```text
Auto TIENE un Motor
```

---

# 👨‍🏫 Agregación → USA UN

En agregación, el objeto se recibe desde afuera.

Ejemplo:

```python
class Profesor:

    def __init__(self, nombre):

        self.nombre = nombre


class Curso:

    def __init__(self, profesor):

        self.profesor = profesor
```

---

Crear objetos:

```python
profesor = Profesor("Ana")

curso = Curso(profesor)
```

---

Acceder:

```python
curso.profesor.nombre
```

Resultado:

```text
Ana
```

---

# 🔍 Explicación

El profesor ya existía.

El curso simplemente lo usa.

Por eso decimos:

```text
Curso USA un Profesor
```

---

# 🧠 Diferencia importante

### Composición

El objeto se crea dentro de otro objeto.

```python
self.motor = Motor()
```

---

### Agregación

El objeto se recibe desde afuera.

```python
curso = Curso(profesor)
```

---

# 📊 Comparación

| Concepto | Se crea dentro | Se recibe por parámetro |
|---------|---------------|------------------------|
| Composición | Sí | No |
| Agregación | No | Sí |

---

# 🧪 Ejemplo real

```python
class Procesador:

    def informacion(self):

        return "Ryzen 7"


class Computadora:

    def __init__(self):

        self.procesador = Procesador()


pc = Computadora()

print(pc.procesador.informacion())
```

Resultado:

```text
Ryzen 7
```

---

# 🧪 Otro ejemplo

```python
class Alumno:

    def __init__(self, nombre):

        self.nombre = nombre


class Curso:

    def __init__(self, alumno):

        self.alumno = alumno


alumno = Alumno("Juan")

curso = Curso(alumno)

print(curso.alumno.nombre)
```

Resultado:

```text
Juan
```

---

# 📌 Resumen visual

```text
HERENCIA
ES UN

Perro → Animal
```

---

```text
COMPOSICIÓN
TIENE UN

Auto → Motor
Computadora → Procesador
```

---

```text
AGREGACIÓN
USA UN

Curso → Profesor
Curso → Alumno
```

---

# ⚠ Importante

Antes de usar composición o agregación, preguntate:

```text
¿Mi objeto ES otro objeto?

o

¿Mi objeto TIENE otro objeto?

o

¿Mi objeto USA otro objeto?
```

Eso te ayudará a elegir la relación correcta.

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
class Motor
```

con:

```python
arrancar()
```

que retorne:

```text
Motor encendido
```

Crear:

```python
class Auto
```

que tenga un:

```python
self.motor
```

Retornar:

```python
auto.motor.arrancar()
```

Resultado esperado:

```text
Motor encendido
```

---

## Ejercicio 2

Crear:

```python
class Procesador
```

y:

```python
class Computadora
```

La computadora debe tener un procesador.

Resultado esperado:

```text
Ryzen 7
```

---

## Ejercicio 3

Crear:

```python
class Profesor
```

y:

```python
class Curso
```

El curso usa un profesor.

Resultado esperado:

```text
Ana
```

---

## Ejercicio 4

Crear:

```python
class Alumno
```

y:

```python
class Curso
```

Resultado esperado:

```text
Juan
```

---

## Ejercicio 5 al 10

Más ejercicios mezclando:

- Tiene un
- Usa un
- Objetos dentro de objetos
- Objetos recibidos por parámetro

---

# 🎯 Lo más importante que aprendiste

- Herencia → ES UN
- Composición → TIENE UN
- Agregación → USA UN
- La composición crea objetos internamente.
- La agregación recibe objetos externos.
- Estas relaciones permiten modelar sistemas reales.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M27 — Herencia múltiple
```

y veremos cómo una clase puede heredar de varias clases al mismo tiempo.