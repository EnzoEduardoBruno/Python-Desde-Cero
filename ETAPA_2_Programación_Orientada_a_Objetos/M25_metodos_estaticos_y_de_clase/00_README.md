# M25 — Métodos estáticos y de clase 🧰

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

Ahora vamos a aprender dos tipos de métodos muy usados en Programación Orientada a Objetos:

- `@staticmethod`
- `@classmethod`

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- entender qué es un método estático
- entender qué es un método de clase
- usar `@staticmethod`
- usar `@classmethod`
- diferenciar `self`, `cls` y métodos sin instancia
- saber cuándo usar cada tipo de método

---

# 📌 Recordatorio

Hasta ahora vimos métodos normales de instancia.

Ejemplo:

```python
class Persona:

    def saludar(self):
        return "Hola"


persona = Persona()

print(persona.saludar())
```

Resultado:

```text
Hola
```

---

# 🧠 Método de instancia

Un método de instancia usa:

```python
self
```

Ejemplo:

```python
def saludar(self):
    return "Hola"
```

`self` representa al objeto actual.

---

# 🧰 ¿Qué es un método estático?

Un método estático pertenece a la clase, pero no usa:

```python
self
```

ni:

```python
cls
```

Se define usando:

```python
@staticmethod
```

---

# 🧪 Ejemplo

```python
class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b
```

Usar el método:

```python
resultado = Calculadora.sumar(10, 5)

print(resultado)
```

Resultado:

```text
15
```

---

# 🔍 Explicación

```python
@staticmethod
```

indica que el método es estático.

---

```python
def sumar(a, b):
```

No recibe `self`.

No recibe `cls`.

Solo recibe los parámetros necesarios.

---

```python
Calculadora.sumar(10, 5)
```

Usamos el método directamente desde la clase.

No necesitamos crear un objeto.

---

# 📌 ¿Cuándo usar staticmethod?

Cuando una función está relacionada con una clase, pero no necesita acceder a datos del objeto.

Ejemplo:

```python
class Conversor:

    @staticmethod
    def metros_a_centimetros(metros):
        return metros * 100
```

Uso:

```python
Conversor.metros_a_centimetros(2)
```

Resultado:

```text
200
```

---

# 🏫 ¿Qué es un método de clase?

Un método de clase pertenece a la clase y recibe:

```python
cls
```

Se define usando:

```python
@classmethod
```

---

# 🧪 Ejemplo

```python
class Usuario:

    cantidad = 0

    @classmethod
    def mostrar_cantidad(cls):
        return cls.cantidad
```

Uso:

```python
print(Usuario.mostrar_cantidad())
```

Resultado:

```text
0
```

---

# 🔍 Explicación

```python
@classmethod
```

indica que el método es de clase.

---

```python
def mostrar_cantidad(cls):
```

Recibe `cls`.

---

```python
cls.cantidad
```

Accede a un atributo de clase.

---

# 📌 ¿Qué es cls?

`cls` representa a la clase.

Así como:

```python
self
```

representa al objeto,

```python
cls
```

representa a la clase.

---

# 🧠 Diferencia entre self y cls

| Nombre | Representa |
|---|---|
| `self` | objeto actual |
| `cls` | clase actual |

---

# 📊 Diferencia entre métodos

| Tipo de método | Usa self | Usa cls | Decorador |
|---|---|---|---|
| Método de instancia | Sí | No | No usa |
| Método estático | No | No | `@staticmethod` |
| Método de clase | No | Sí | `@classmethod` |

---

# 🧪 Ejemplo completo

```python
class Calculadora:

    cantidad_operaciones = 0

    @staticmethod
    def sumar(a, b):
        return a + b

    @classmethod
    def mostrar_cantidad(cls):
        return cls.cantidad_operaciones
```

Uso:

```python
print(Calculadora.sumar(10, 5))

print(Calculadora.mostrar_cantidad())
```

Resultado:

```text
15
0
```

---

# ⚠ Error frecuente

Un método estático NO debe recibir `self`.

Incorrecto:

```python
class Calculadora:

    @staticmethod
    def sumar(self, a, b):
        return a + b
```

Correcto:

```python
class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b
```

---

# ⚠ Otro error frecuente

Un método de clase debe recibir `cls`.

Incorrecto:

```python
class Usuario:

    @classmethod
    def mostrar_cantidad():
        return 0
```

Correcto:

```python
class Usuario:

    @classmethod
    def mostrar_cantidad(cls):
        return 0
```

---

# 📌 Resumen visual

```python
class Ejemplo:

    def metodo_instancia(self):
        return "usa self"

    @staticmethod
    def metodo_estatico():
        return "no usa self ni cls"

    @classmethod
    def metodo_clase(cls):
        return "usa cls"
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

Crear una clase:

```python
class Calculadora:
```

Crear un método estático:

```python
@staticmethod
def sumar(a, b):
    return a + b
```

Retornar:

```python
Calculadora.sumar(10, 5)
```

Resultado esperado:

```python
15
```

---

## Ejercicio 2

Crear una clase:

```python
class Calculadora:
```

Crear un método estático:

```python
@staticmethod
def restar(a, b):
    return a - b
```

Retornar:

```python
Calculadora.restar(10, 5)
```

Resultado esperado:

```python
5
```

---

## Ejercicio 3

Crear una clase:

```python
class Conversor:
```

Crear un método estático:

```python
@staticmethod
def metros_a_centimetros(metros):
    return metros * 100
```

Retornar:

```python
Conversor.metros_a_centimetros(2)
```

Resultado esperado:

```python
200
```

---

## Ejercicio 4

Crear una clase:

```python
class Validador:
```

Crear un método estático:

```python
@staticmethod
def es_mayor_de_edad(edad):
    return edad >= 18
```

Retornar:

```python
Validador.es_mayor_de_edad(20)
```

Resultado esperado:

```python
True
```

---

## Ejercicio 5

Crear una clase:

```python
class Usuario:
```

Crear un atributo de clase:

```python
cantidad = 5
```

Crear un método de clase:

```python
@classmethod
def mostrar_cantidad(cls):
    return cls.cantidad
```

Retornar:

```python
Usuario.mostrar_cantidad()
```

Resultado esperado:

```python
5
```

---

## Ejercicio 6

Crear una clase:

```python
class Producto:
```

Crear un atributo de clase:

```python
iva = 21
```

Crear un método de clase:

```python
@classmethod
def mostrar_iva(cls):
    return cls.iva
```

Retornar:

```python
Producto.mostrar_iva()
```

Resultado esperado:

```python
21
```

---

## Ejercicio 7

Crear una clase:

```python
class Configuracion:
```

Crear un atributo de clase:

```python
modo = "Producción"
```

Crear un método de clase:

```python
@classmethod
def mostrar_modo(cls):
    return cls.modo
```

Retornar:

```python
Configuracion.mostrar_modo()
```

Resultado esperado:

```text
Producción
```

---

## Ejercicio 8

Crear una clase:

```python
class Texto:
```

Crear un método estático:

```python
@staticmethod
def convertir_mayusculas(texto):
    return texto.upper()
```

Retornar:

```python
Texto.convertir_mayusculas("python")
```

Resultado esperado:

```text
PYTHON
```

---

## Ejercicio 9

Crear una clase:

```python
class Sistema:
```

Crear un atributo de clase:

```python
nombre = "Python Desde Cero"
```

Crear un método de clase:

```python
@classmethod
def mostrar_nombre(cls):
    return cls.nombre
```

Retornar:

```python
Sistema.mostrar_nombre()
```

Resultado esperado:

```text
Python Desde Cero
```

---

## Ejercicio 10

Crear una clase:

```python
class Herramienta:
```

Crear un método estático:

```python
@staticmethod
def saludar():
    return "Hola"
```

Crear un atributo de clase:

```python
version = "1.0"
```

Crear un método de clase:

```python
@classmethod
def mostrar_version(cls):
    return cls.version
```

Retornar:

```python
Herramienta.saludar() + " " + Herramienta.mostrar_version()
```

Resultado esperado:

```text
Hola 1.0
```

---

# 🎯 Lo más importante que aprendiste

- `@staticmethod` crea métodos que no usan `self` ni `cls`.
- `@classmethod` crea métodos que usan `cls`.
- `self` representa al objeto.
- `cls` representa a la clase.
- Los métodos estáticos suelen ser funciones relacionadas con una clase.
- Los métodos de clase suelen trabajar con atributos de clase.

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M26 — Composición y agregación
```

donde veremos cómo un objeto puede estar formado por otros objetos.