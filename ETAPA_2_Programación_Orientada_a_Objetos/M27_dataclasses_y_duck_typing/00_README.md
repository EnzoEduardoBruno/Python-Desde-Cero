# M27 — Dataclasses y Duck Typing 🦆

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
- composición y agregación

Ahora vamos a aprender dos conceptos muy útiles en Python moderno:

- `@dataclass`
- Duck Typing

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender qué es una dataclass
- usar `@dataclass`
- crear clases con constructor automático
- reducir código repetido
- entender qué es Duck Typing
- usar objetos diferentes con el mismo comportamiento

---

# 📌 ¿Qué es una dataclass?

Una `dataclass` es una forma más simple de crear clases que principalmente guardan datos.

Para usarla importamos:

```python
from dataclasses import dataclass
```

---

# 🧪 Clase tradicional

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Crear objeto:

```python
persona = Persona("Ana", 20)
```

Acceder:

```python
persona.nombre
```

Resultado:

```text
Ana
```

---

# 🧪 Lo mismo usando dataclass

```python
from dataclasses import dataclass


@dataclass
class Persona:

    nombre: str
    edad: int
```

Crear objeto:

```python
persona = Persona("Ana", 20)
```

Acceder:

```python
persona.nombre
```

Resultado:

```text
Ana
```

---

# 🧠 ¿Qué hizo Python?

Al usar:

```python
@dataclass
```

Python crea automáticamente:

```python
__init__
```

Por eso no necesitamos escribir:

```python
def __init__(self, nombre, edad):

    self.nombre = nombre
    self.edad = edad
```

---

# 📌 Constructor automático

Una dataclass genera automáticamente el constructor.

Ejemplo:

```python
@dataclass
class Producto:

    nombre: str
    precio: int
```

Podemos crear:

```python
producto = Producto("Mouse", 1500)
```

Y acceder:

```python
producto.precio
```

Resultado:

```text
1500
```

---

# 📌 También genera __repr__

```python
@dataclass
class Persona:

    nombre: str
    edad: int
```

Crear objeto:

```python
persona = Persona("Ana", 20)
```

Mostrar:

```python
print(persona)
```

Resultado:

```text
Persona(nombre='Ana', edad=20)
```

---

# 📌 ¿Cuándo usar dataclass?

Conviene usar `dataclass` cuando una clase principalmente guarda datos.

Ejemplos:

```text
Persona
Producto
Alumno
Libro
Usuario
Pedido
Factura
```

---

# ⚠ Cuándo NO usar dataclass

No siempre es necesario usar dataclass.

Si una clase tiene mucha lógica, muchos métodos o reglas complejas, puede convenir una clase tradicional.

---

# 🦆 ¿Qué es Duck Typing?

Duck Typing es una idea muy usada en Python.

La frase viene de:

```text
Si camina como pato y hace cuac como pato, entonces es un pato.
```

En programación significa:

```text
No importa tanto qué clase es el objeto.

Importa qué métodos o comportamientos tiene.
```

---

# 🧪 Ejemplo

```python
class Perro:

    def hablar(self):

        return "Guau"


class Gato:

    def hablar(self):

        return "Miau"
```

Ambas clases tienen:

```python
hablar()
```

Entonces podemos usarlas de la misma manera.

---

# 🧪 Función con Duck Typing

```python
def hacer_hablar(animal):

    return animal.hablar()
```

Usar:

```python
perro = Perro()

gato = Gato()

hacer_hablar(perro)

hacer_hablar(gato)
```

Resultado:

```text
Guau

Miau
```

---

# 🧠 ¿Qué importa?

No importa si el objeto es:

```python
Perro
```

o:

```python
Gato
```

Lo importante es que tenga el método:

```python
hablar()
```

---

# 📌 Duck Typing y polimorfismo

Duck Typing se parece al polimorfismo.

La diferencia es que en Duck Typing no necesitamos que las clases hereden de una clase padre.

---

# 🧪 Ejemplo sin herencia

```python
class Auto:

    def mover(self):

        return "Auto moviéndose"


class Barco:

    def mover(self):

        return "Barco navegando"


def iniciar_movimiento(objeto):

    return objeto.mover()
```

Uso:

```python
auto = Auto()

barco = Barco()

iniciar_movimiento(auto)

iniciar_movimiento(barco)
```

Resultado:

```text
Auto moviéndose

Barco navegando
```

---

# 📌 Resumen visual

```python
from dataclasses import dataclass


@dataclass
class Persona:

    nombre: str
    edad: int


persona = Persona("Ana", 20)

print(persona)
```

Resultado:

```text
Persona(nombre='Ana', edad=20)
```

---

```python
class Perro:

    def hablar(self):

        return "Guau"


def ejecutar(objeto):

    return objeto.hablar()
```

Si el objeto tiene `hablar()`, funciona.

Eso es Duck Typing.

---

# 📊 Comparación rápida

| Concepto | Idea principal |
|---|---|
| Dataclass | Crear clases de datos con menos código |
| Duck Typing | Usar objetos por comportamiento, no por tipo |

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

# 🎯 Lo más importante que aprendiste

- `@dataclass` permite crear clases de datos con menos código.
- Las dataclasses generan automáticamente `__init__`.
- También generan una representación útil del objeto.
- Duck Typing se basa en comportamientos.
- En Duck Typing importa qué puede hacer un objeto, no exactamente qué clase es.
- Python favorece este estilo flexible.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M28 — Proyecto final POO
```

donde integrarás todo lo aprendido en un sistema completo orientado a objetos.