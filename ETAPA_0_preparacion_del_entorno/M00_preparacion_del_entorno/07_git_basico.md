# 07 - 🌿 Git básico + 🐍 Primer programa en Python

En este módulo aprenderemos a utilizar **Git** para versionar nuestros proyectos, crearemos nuestro primer programa en **Python** y lo subiremos a **GitHub**.

---

# 📖 ¿Qué es Git?

Git es un sistema de control de versiones.

Permite:

* 📂 Guardar cambios.
* ⏪ Recuperar versiones anteriores.
* ☁️ Trabajar con GitHub.
* 📝 Mantener un historial del proyecto.

---

# 🧪 PASO 1: Verificar Git

Abrir **Git Bash** y ejecutar:

```bash
git --version
```

Resultado esperado:

```text
git version 2.xx.x.windows.x
```

---

# 👤 PASO 2: Configurar nombre y correo

Git necesita saber quién realiza los cambios.

```bash
git config --global user.name "EnzoISPC"
git config --global user.email "EnzoISPC@outlook.com"
```

---

# 🔑 PASO 3: Configurar autenticación por navegador

Para que Git abra automáticamente el navegador cuando necesites autenticarte:

```bash
git config --global credential.helper manager
git config --global credential.gitHubAuthModes browser
```

---

# ✅ PASO 4: Verificar configuración

```bash
git config --list
```

Resultado esperado:

```text
user.name=EnzoISPC
user.email=EnzoISPC@outlook.com
credential.helper=manager
credential.gitHubAuthModes=browser
```

---

# 📁 PASO 5: Crear carpeta del proyecto

```bash
mkdir nuevoproyecto
cd nuevoproyecto
```

---

# 🌱 PASO 6: Inicializar repositorio Git

```bash
git init
```

Resultado esperado:

```text
Initialized empty Git repository in /c/Users/EnzoISPC/OneDrive/Desktop/nuevoproyecto/.git/
```

---

# 🐍 PASO 7: Crear archivo `hola.py`

### Opción A: Desde Git Bash

```bash
echo "print('Hola mundo')" > hola.py
```

### Opción B: Desde VS Code

1. Abrir VS Code:

```bash
code .
```

2. Crear un nuevo archivo llamado:

```text
hola.py
```

3. Escribir:

```python
print("Hola mundo")
```

4. Guardar con:

```text
Ctrl + S
```

---

# 📄 PASO 8: Ver contenido del archivo

```bash
cat hola.py
```

Resultado esperado:

```python
print('Hola mundo')
```

---

# 🔍 PASO 9: Ver estado de Git

```bash
git status
```

Resultado esperado:

```text
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        hola.py

nothing added to commit but untracked files present (use "git add" to track)
```

---

# ➕ PASO 10: Agregar archivos al área de staging

```bash
git add .
```

El punto:

```text
.
```

significa:

```text
Todos los archivos de la carpeta actual.
```

---

# 📋 PASO 11: Verificar estado nuevamente

```bash
git status
```

Resultado esperado:

```text
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   hola.py
```

# 💾 PASO 12: Crear el commit (guardar cambios)

```bash
git commit -m "Mi primer commit - agregando hola.py"
```

Resultado esperado:

```text
[master (root-commit) 1234567] Mi primer commit - agregando hola.py
 1 file changed, 1 insertion(+)
 create mode 100644 hola.py
```

---

# 📜 PASO 13: Ver historial de commits

```bash
git log
```

Resultado esperado:

```text
commit 1234567890abcdef...

Author: EnzoISPC <EnzoISPC@outlook.com>

Date: Mon Jul 20 11:11:06 2026 -0300

    Mi primer commit - agregando hola.py
```

---

# ☁️ PASO 14: Crear repositorio en GitHub

1. Entrar a:

```text
https://github.com
```

2. Iniciar sesión con tu cuenta.

3. Hacer clic en:

```text
New
```

o

```text
+

New repository
```

4. Configurar:

```text
Repository name:
nuevoproyecto

Description:
(opcional)

Visibility:
Public o Private
```

No marcar:

* Add a README file
* Add .gitignore
* Choose a license

5. Hacer clic en:

```text
Create repository
```

---

# 🔗 PASO 15: Conectar repositorio local con GitHub

```bash
git remote add origin https://github.com/EnzoISPC/nuevoproyecto.git
```

---

# 🌐 PASO 16: Verificar conexión remota

```bash
git remote -v
```

Resultado esperado:

```text
origin  https://github.com/EnzoISPC/nuevoproyecto.git (fetch)

origin  https://github.com/EnzoISPC/nuevoproyecto.git (push)
```

---

# 🚀 PASO 17: Subir cambios a GitHub

```bash
git push -u origin master
```

La primera vez sucederá lo siguiente:

1. Git detectará que necesitás autenticarte.
2. Se abrirá automáticamente el navegador.
3. Iniciarás sesión en GitHub (si todavía no lo hiciste).
4. Autorizarás el acceso.
5. Git continuará automáticamente y subirá el proyecto.

---

# ✅ PASO 18: Verificar que subió correctamente

```bash
git status
```

Resultado esperado:

```text
On branch master

Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

---

# 🌍 PASO 19: Ver el repositorio en GitHub

Ingresar a:

```text
https://github.com/EnzoISPC/nuevoproyecto
```

Verificar que aparezcan:

* 📄 hola.py
* 💾 El commit **"Mi primer commit - agregando hola.py"**

---

# ▶ PASO 20: Ejecutar el programa

```bash
python hola.py
```

Resultado esperado:

```text
Hola mundo
```

---

# 🖨 ¿Qué hace `print()`?

La función:

```python
print()
```

permite mostrar información por pantalla.

Ejemplos:

```python
print("Hola")
print("Python")
print(123)
print(10 + 5)
```

Resultado:

```text
Hola

Python

123

15
```

Otro ejemplo:

```python
print("EnzoISPC")
```

Resultado:

```text
EnzoISPC
```

---

# 🧰 Comandos que más usaremos

| Comando                   | Función                 |
| ------------------------- | ----------------------- |
| `git init`                | Crear repositorio       |
| `git status`              | Ver cambios             |
| `git add .`               | Agregar archivos        |
| `git commit -m "mensaje"` | Guardar cambios         |
| `git push origin main`    | Enviar cambios a GitHub |
| `git pull`                | Descargar cambios       |
| `git log`                 | Ver historial           |
| `python hola.py`          | Ejecutar el programa    |

---

# 🔄 Flujo básico

Durante todo el curso utilizaremos siempre este flujo:

```bash
git add .

git commit -m "mensaje"

git push origin main
```

---

# ⚠ Problemas frecuentes

## ❌ Author identity unknown

Ejecutar:

```bash
git config --global user.name "EnzoISPC"

git config --global user.email "EnzoISPC@outlook.com"
```

---

## ❌ nothing to commit

No es un error.

Simplemente significa que no existen cambios para guardar.

---

## ❌ fatal: not a git repository

Significa que todavía no ejecutaste:

```bash
git init
```

---

## ❌ python: can't open file 'hola.py'

Verificar que estés dentro de la carpeta correcta:

```bash
cd nuevoproyecto
```

---

## ❌ 'python' no se reconoce

Verificar la instalación de Python.

---

## ❌ No se abre el navegador al hacer push

Ejecutar:

```bash
git config --global credential.helper manager

git config --global credential.gitHubAuthModes browser
```

---

# 🎯 Objetivos cumplidos

Al finalizar este módulo deberías poder:

* ✅ Configurar Git.
* ✅ Configurar la autenticación mediante navegador.
* ✅ Crear un repositorio con `git init`.
* ✅ Crear archivos y carpetas.
* ✅ Agregar archivos con `git add .`.
* ✅ Guardar cambios con `git commit`.
* ✅ Conectar un repositorio con GitHub.
* ✅ Subir cambios mediante `git push`.
* ✅ Ejecutar programas en Python.
* ✅ Consultar el historial con `git log`.

---

# 🎉 ¡Felicitaciones!

Acabás de:

* ✅ Configurar Git.
* ✅ Configurar GitHub.
* ✅ Crear tu primer repositorio.
* ✅ Escribir tu primer programa en Python.
* ✅ Ejecutar tu primer programa.
* ✅ Subir tu código a GitHub.

A partir de ahora comenzarás a desarrollar programas cada vez más complejos mientras aprendés a utilizar Git como cualquier desarrollador profesional.

---

# 📚 Próximo paso

Continuar con:

```text
08_clonar_repositorio.md
```
