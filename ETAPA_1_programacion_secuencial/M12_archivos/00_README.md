# M12 — Archivos 📄

En este módulo vas a aprender a trabajar con archivos en Python.

Vamos a ver:

- Lectura de archivos
- Escritura de archivos
- Archivos TXT
- Archivos CSV

---

# 🎯 Objetivo del módulo

Al finalizar este módulo deberías poder:

- crear archivos `.txt`
- escribir texto en archivos
- leer contenido de archivos
- agregar contenido a archivos existentes
- trabajar con archivos usando `with open()`
- crear archivos `.csv`
- leer archivos `.csv`
- entender los modos `"r"`, `"w"` y `"a"`

---

# 📁 Carpeta de trabajo

En este módulo todos los archivos que creemos se guardarán dentro de una carpeta llamada:

```text
archivos/
```

Por ejemplo:

```text
M12_archivos/
│
├── archivos/
│   ├── saludo.txt
│   ├── datos.txt
│   ├── notas.txt
│   ├── alumnos.csv
│   ├── productos.csv
│   └── resumen.txt
│
├── 00_README.md
├── practica.py
├── soluciones.py
└── test.py
```

¿Por qué hacemos esto?

Porque mantiene el proyecto ordenado y evita llenar la carpeta principal con archivos temporales.

Todos los ejercicios de este módulo deberán trabajar dentro de la carpeta:

```text
archivos/
```

Por ejemplo:

```python
with open("archivos/saludo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo")
```

Esto creará el archivo:

```text
archivos/saludo.txt
```

y no:

```text
saludo.txt
```

en la raíz del proyecto.

---

# 🧠 ¿Qué es un archivo?

Un archivo permite guardar información fuera del programa.

Por ejemplo:

```text
archivos/notas.txt
archivos/alumnos.csv
archivos/datos.txt
```

Cuando el programa termina, las variables se pierden.

Pero si guardamos información en un archivo, podemos volver a usarla después.

---

# 📌 open()

Para trabajar con archivos usamos:

```python
open()
```

Ejemplo:

```python
archivo = open("archivos/datos.txt", "w", encoding="utf-8")
```

---

# 📌 Modos de apertura

| Modo | Significado |
|---|---|
| `"r"` | leer |
| `"w"` | escribir desde cero |
| `"a"` | agregar al final |

---

# ✍ Escribir un archivo TXT

## Paso 1 — Código

```python
archivo = open("archivos/saludo.txt", "w", encoding="utf-8")
archivo.write("Hola mundo")
archivo.close()
```

## Paso 2 — Resultado

Se crea un archivo llamado:

```text
archivos/saludo.txt
```

Con este contenido:

```text
Hola mundo
```

---

# 🔍 Explicación línea por línea

```python
archivo = open("archivos/saludo.txt", "w", encoding="utf-8")
```

Abre o crea el archivo `archivos/saludo.txt` en modo escritura.

---

```python
archivo.write("Hola mundo")
```

Escribe texto dentro del archivo.

---

```python
archivo.close()
```

Cierra el archivo.

---

# ✅ Mejor forma: with open()

La forma recomendada es usar:

```python
with open(...)
```

Ejemplo:

```python
with open("archivos/saludo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola mundo")
```

---

# 🔍 ¿Por qué usar with?

Porque Python cierra el archivo automáticamente.

Esto evita errores y hace el código más seguro.

---

# 📖 Leer un archivo TXT

## Paso 1 — Código

```python
with open("archivos/saludo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

## Paso 2 — Resultado

```text
Hola mundo
```

---

# 🔍 Explicación

```python
archivo.read()
```

lee todo el contenido del archivo.

---

# ➕ Agregar contenido a un archivo

Para agregar texto al final usamos modo:

```python
"a"
```

---

# 🧪 Ejemplo

```python
with open("archivos/saludo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nBienvenido")
```

Si el archivo tenía:

```text
Hola mundo
```

queda así:

```text
Hola mundo
Bienvenido
```

---

# 📊 Archivos CSV

CSV significa:

```text
Comma Separated Values
```

En español:

```text
valores separados por coma
```

Ejemplo:

```csv
nombre,edad
Ana,25
Luis,30
```

---

# 📌 Importar csv

Para trabajar con CSV usamos:

```python
import csv
```

---

# ✍ Escribir CSV

## Paso 1 — Código

```python
import csv

with open("archivos/alumnos.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", 25])
```

## Paso 2 — Resultado

Se crea un archivo llamado:

```text
archivos/alumnos.csv
```

Con contenido similar a:

```csv
nombre,edad
Ana,25
```

---

# 📖 Leer CSV

## Paso 1 — Código

```python
import csv

with open("archivos/alumnos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)
```

## Paso 2 — Resultado

```text
['nombre', 'edad']
['Ana', '25']
```

---

# ⚠ Importante

Cuando leemos un CSV, los valores suelen venir como texto.

Por ejemplo:

```text
25
```

puede venir como:

```python
"25"
```

---

# ✍ ¿Dónde tengo que escribir el código?

Todos los ejercicios se resuelven en:

```text
practica.py
```

---

# 📌 Importante

En este módulo las funciones ya están creadas.

Ejemplo:

```python
def ejercicio_1():
    pass
```

Tu trabajo es:

- NO borrar `def`
- NO cambiar el nombre de la función
- borrar `pass`
- escribir la solución dentro de la función
- usar `return`

---

# 🧪 ¿Cómo pruebo los ejercicios?

Desde la terminal, dentro de la carpeta del módulo:

```bash
python test.py
```

---

# 🧪 Ejercicios autocorregibles

## Ejercicio 1

Crear el archivo:

```text
archivos/saludo.txt
```

Escribir:

```text
Hola mundo
```

Retornar:

```text
Archivo creado
```

---

## Ejercicio 2

Leer el archivo:

```text
archivos/saludo.txt
```

Retornar su contenido.

---

## Ejercicio 3

Crear el archivo:

```text
archivos/datos.txt
```

Escribir:

```text
Python desde cero
```

Retornar:

```text
Datos guardados
```

---

## Ejercicio 4

Leer el archivo:

```text
archivos/datos.txt
```

Retornar su contenido.

---

## Ejercicio 5

Crear el archivo:

```text
archivos/notas.txt
```

Escribir:

```text
Primera línea
```

Luego agregar:

```text
Segunda línea
```

usando modo append `"a"`.

Retornar el contenido completo del archivo.

---

## Ejercicio 6

Crear el archivo:

```text
archivos/alumnos.csv
```

Con estas filas:

```csv
nombre,edad
Ana,25
Luis,30
```

Retornar:

```text
CSV creado
```

---

## Ejercicio 7

Leer el archivo:

```text
archivos/alumnos.csv
```

Retornar una lista con sus filas.

---

## Ejercicio 8

Crear el archivo:

```text
archivos/productos.csv
```

Con estas filas:

```csv
producto,precio
Mouse,500
Teclado,1000
```

Retornar:

```text
Productos guardados
```

---

## Ejercicio 9

Leer el archivo:

```text
archivos/productos.csv
```

Retornar una lista con sus filas.

---

## Ejercicio 10

Crear el archivo:

```text
archivos/resumen.txt
```

Escribir:

```text
Módulo de archivos completado
```

Leer el archivo y retornar su contenido.

---

# 🚀 Resultado esperado

```text
🧪 Corrigiendo ejercicios...

✅ Ejercicio 1 correcto
✅ Ejercicio 2 correcto
❌ Ejercicio 3 incorrecto

🎯 Resultado final: 2/3
```

---

# 🎯 Lo más importante que aprendiste

- `open()` permite trabajar con archivos.
- `"w"` escribe desde cero.
- `"r"` lee archivos.
- `"a"` agrega contenido.
- `with open()` cierra archivos automáticamente.
- `read()` lee el contenido de un archivo.
- `write()` escribe contenido.
- `csv.writer()` permite escribir CSV.
- `csv.reader()` permite leer CSV.
- Usar una carpeta de trabajo mantiene el proyecto ordenado.