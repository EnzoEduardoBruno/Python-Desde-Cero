# 📥 08 - Clonar este repositorio

Una vez instalado:

* Python
* VS Code
* Git
* GitHub

ya podemos descargar este curso completo a nuestra computadora.

A esto se lo llama:

```text
Clonar un repositorio
```

---

# 📌 ¿Qué significa clonar?

Clonar significa:

```text
Descargar una copia completa del repositorio
y mantenerla conectada con GitHub.
```

Cuando el repositorio se actualice, podremos descargar los cambios.

---

# 🌎 Repositorio del curso

La dirección del repositorio es:

```text
https://github.com/EnzoEduardoBruno/Python-Desde-Cero
```

También podés abrirlo desde tu navegador:

```text
https://github.com/EnzoEduardoBruno/Python-Desde-Cero
```

---

# 📋 Copiar la URL

Dentro del repositorio hacer clic en:

```text
Code

→ HTTPS

→ Copiar URL
```

La URL será:

```text
https://github.com/EnzoEduardoBruno/Python-Desde-Cero.git
```

---

# 📂 Crear una carpeta de trabajo

Se recomienda crear una carpeta llamada:

```text
WorkSpace
```

Por ejemplo:

```text
C:\Users\TU_USUARIO\Documents\WorkSpace
```

o:

```text
C:\Users\TU_USUARIO\Desktop\WorkSpace
```

---

# 🐚 Abrir Git Bash

Abrir Git Bash.

Ir a la carpeta donde querés guardar el proyecto.

Ejemplo:

```bash
cd ~/Desktop

mkdir WorkSpace

cd WorkSpace
```

---

# 📥 Clonar el repositorio

Ejecutar:

```bash
git clone https://github.com/EnzoEduardoBruno/Python-Desde-Cero.git
```

Git comenzará a descargar todos los archivos.

Resultado esperado:

```text
Cloning into 'Python-Desde-Cero'...

Receiving objects: 100%

Resolving deltas: 100%
```

---

# 📂 Entrar a la carpeta

Una vez finalizada la descarga:

```bash
cd Python-Desde-Cero
```

Podés verificar:

```bash
ls
```

Deberías ver algo parecido a:

```text
ETAPA_0_preparacion_del_entorno

ETAPA_1_programacion_secuencial

ETAPA_2_programacion_orientada_a_objetos

README.md
```

---

# 💻 Abrir el proyecto en VS Code

Desde Git Bash ejecutar:

```bash
code .
```

El punto:

```text
.
```

significa:

```text
La carpeta actual
```

VS Code abrirá todo el proyecto.

---

# 🧪 Verificar que Git funciona

Abrir la terminal dentro de VS Code.

Ejecutar:

```bash
git status
```

Resultado esperado:

```text
On branch main

Your branch is up to date with 'origin/main'

nothing to commit, working tree clean
```

Esto significa que:

* Git está funcionando.
* El repositorio fue clonado correctamente.
* No hay cambios pendientes.

---

# 📥 Descargar futuras actualizaciones

Si el repositorio recibe nuevos cambios, podés actualizarlos ejecutando:

```bash
git pull
```

Resultado:

```text
Already up to date.
```

o:

```text
Updating...

Fast-forward
```

---

# ⚠ Problemas frecuentes

## El comando `git clone` falla

Verificar:

```bash
git --version
```

Si no funciona, volver a:

```text
03_instalar_git.md
```

---

## El comando `code .` no funciona

Ejemplo:

```text
'code' no se reconoce como un comando interno o externo
```

Volver a:

```text
02_instalar_vscode.md
```

y verificar que durante la instalación se marcó:

```text
☑ Add to PATH
```

---

## Ya existe una carpeta con ese nombre

Ejemplo:

```text
fatal: destination path 'Python-Desde-Cero' already exists
```

Significa que el repositorio ya fue descargado.

Podés:

* eliminar la carpeta existente
* renombrarla
* entrar a ella:

```bash
cd Python-Desde-Cero
```

---

# 🎯 Objetivo

Si llegaste hasta acá deberías poder:

✅ Clonar el repositorio.

✅ Entrar a la carpeta.

✅ Abrirlo con:

```bash
code .
```

✅ Ejecutar:

```bash
git status
```

y obtener:

```text
working tree clean
```

---

# 🎉 ¡Felicitaciones!

Terminaste:

```text
ETAPA 0

Preparación del entorno
```

Ya tenés:

✅ Python

✅ VS Code

✅ Git

✅ GitHub

✅ Extensiones

✅ Configuración de VS Code

✅ Tu primer programa

✅ El repositorio clonado

---

# 🚀 Próximo paso

Continuar con:

```text
ETAPA 1

Programación Secuencial
```

donde comenzarás a aprender Python desde cero.
