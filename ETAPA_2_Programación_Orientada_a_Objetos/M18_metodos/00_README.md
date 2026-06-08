# M18 — Métodos ⚙️

En el módulo anterior aprendimos a crear atributos.

Los atributos permiten almacenar información dentro de los objetos.

Ahora vamos a aprender algo igual de importante:

# Los métodos

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

* entender qué es un método
* crear métodos dentro de una clase
* utilizar `self`
* invocar métodos desde objetos
* comprender que los métodos representan comportamientos

---

# 📌 Recordatorio

Un objeto tiene:

* atributos
* métodos

---

# 🏷️ Atributos

Los atributos representan datos.

Ejemplo:

```python
class Persona:

    def __init__(self):
        self.nombre = "Ana"
```

Atributo:

```python
self.nombre
```

Contiene información.

---

# ⚙️ Métodos

Los métodos representan acciones o comportamientos.

Ejemplo:

```python
class Persona:

    def saludar(self):
        return "Hola"
```

Método:

```python
saludar()
```

Realiza una acción.

---

# 🌎 Ejemplos del mundo real

## Persona

Atributos:

```text
nombre
edad
altura
```

Métodos:

```text
saludar
caminar
hablar
```

---

## Auto

Atributos:

```text
marca
modelo
color
```

Métodos:

```text
arrancar
frenar
acelerar
```

---

## Perro

Atributos:

```text
nombre
raza
edad
```

Métodos:

```text
ladrar
correr
dormir
```

---

# 🐍 Crear un método

Ejemplo:

```python
class Persona:

    def saludar(self):
        return "Hola"
```

---

# 🔍 Explicación

```python
def saludar(self):
```

Define un método.

---

```python
self
```

Representa al objeto actual.

---

```python
return "Hola"
```

Devuelve un resultado.

---

# 📌 Crear un objeto

```python
class Persona:

    def saludar(self):
        return "Hola"
```

---

Crear instancia:

```python
persona = Persona()
```

---

# 📌 Invocar un método

Usamos:

```python
objeto.metodo()
```

Ejemplo:

```python
persona.saludar()
```

---

Resultado:

```text
Hola
```

---

# 🧪 Ejemplo completo

```python
class Perro:

    def ladrar(self):
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
perro.ladrar()
```

---

Resultado:

```text
Guau
```

---

# 🧠 Diferencia entre atributo y método

Atributo:

```python
persona.nombre
```

No lleva paréntesis.

Representa información.

---

Método:

```python
persona.saludar()
```

Lleva paréntesis.

Representa una acción.

---

# ⚠ Error frecuente

Incorrecto:

```python
persona.saludar
```

---

Correcto:

```python
persona.saludar()
```

---

Porque los métodos deben ejecutarse usando:

```python
()
```

---

# 📌 self en los métodos

Todos los métodos de instancia reciben:

```python
self
```

Ejemplo:

```python
class Persona:

    def saludar(self):
        return "Hola"
```

---

Por ahora simplemente recordá:

```text
self representa al objeto actual
```

Más adelante veremos usos más avanzados.

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

    def saludar(self):
        return "Hola"
```

Retornar:

```python
persona.saludar()
```

Resultado esperado:

```text
Hola
```

---

## Ejercicio 2

Crear:

```python
class Perro:

    def ladrar(self):
        return "Guau"
```

Retornar:

```text
Guau
```

---

## Ejercicio 3

Crear:

```python
class Auto:

    def arrancar(self):
        return "Motor encendido"
```

Retornar:

```text
Motor encendido
```

---

## Ejercicio 4

Crear:

```python
class Alumno:

    def estudiar(self):
        return "Estudiando"
```

Retornar:

```text
Estudiando
```

---

## Ejercicio 5

Crear:

```python
class Libro:

    def abrir(self):
        return "Libro abierto"
```

Retornar:

```text
Libro abierto
```

---

## Ejercicio 6

Crear:

```python
class Celular:

    def llamar(self):
        return "Llamando"
```

Retornar:

```text
Llamando
```

---

## Ejercicio 7

Crear:

```python
class Cuenta:

    def consultar(self):
        return "Saldo disponible"
```

Retornar:

```text
Saldo disponible
```

---

## Ejercicio 8

Crear:

```python
class Usuario:

    def iniciar_sesion(self):
        return "Sesión iniciada"
```

Retornar:

```text
Sesión iniciada
```

---

## Ejercicio 9

Crear:

```python
class Producto:

    def vender(self):
        return "Producto vendido"
```

Retornar:

```text
Producto vendido
```

---

## Ejercicio 10

Crear:

```python
class Pelicula:

    def reproducir(self):
        return "Reproduciendo película"
```

Retornar:

```text
Reproduciendo película
```

---

# 🎯 Lo más importante que aprendiste

* Los atributos representan datos.
* Los métodos representan comportamientos.
* Los métodos se definen con `def`.
* Los métodos utilizan `self`.
* Los métodos se ejecutan con paréntesis.
* Los métodos se invocan mediante:

```python
objeto.metodo()
```

---

# 🚀 Próximo módulo

En el siguiente módulo aprenderás:

```text
M19 — Constructores
```

donde comenzaremos a crear objetos con datos personalizados utilizando parámetros.