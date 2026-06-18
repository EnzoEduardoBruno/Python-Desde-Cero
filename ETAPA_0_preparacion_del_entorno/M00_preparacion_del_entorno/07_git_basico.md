# 🌿 07 - Git básico

En este curso utilizaremos Git para guardar y versionar nuestros proyectos.

No es necesario aprender todos los comandos desde el principio.

Con unos pocos comandos ya podemos trabajar cómodamente.

---

# 📌 ¿Qué es Git?

Git es un sistema de control de versiones.

Permite:

* guardar cambios
* recuperar versiones anteriores
* trabajar con GitHub
* mantener un historial del proyecto

---

# 🧪 Verificar Git

Abrir:

```text id="wgw25u"
Git Bash
```

Ejecutar:

```bash id="nlr7h6"
git --version
```

Resultado esperado:

```text id="0j7q4r"
git version 2.xx.x.windows.x
```

---

# 👤 Configurar nombre

Git necesita saber quién realiza los cambios.

Ejecutar:

```bash id="bq3u2z"
git config --global user.name "Tu Nombre"
```

Ejemplo:

```bash id="sjw8wt"
git config --global user.name "Enzo Bruno"
```

---

# 📧 Configurar correo

Ejecutar:

```bash id="fwfqln"
git config --global user.email "tu@email.com"
```

Ejemplo:

```bash id="0mgp9l"
git config --global user.email "enzo@gmail.com"
```

---

# 🧪 Ver configuración

Ejecutar:

```bash id="fwkzh4"
git config --list
```

Resultado:

```text id="8r7v4g"
user.name=Enzo Bruno

user.email=enzo@gmail.com
```

---

# 📁 Crear un repositorio

Entrar a una carpeta:

```bash id="3nkls3"
cd MiProyecto
```

Crear el repositorio:

```bash id="7kh36v"
git init
```

Resultado:

```text id="0w5bsy"
Initialized empty Git repository
```

---

# 📄 Ver estado

Ejecutar:

```bash id="tw4h7z"
git status
```

Git mostrará:

* archivos nuevos
* archivos modificados
* archivos listos para guardar

---

# ➕ Agregar archivos

Agregar todos los archivos:

```bash id="olb28n"
git add .
```

El punto:

```text id="htfrw4"
.
```

significa:

```text id="bh66em"
Todos los archivos de la carpeta actual
```

---

# 💾 Crear un commit

Guardar cambios:

```bash id="tup0b6"
git commit -m "Primer commit"
```

Ejemplo:

```bash id="m7u0kh"
git commit -m "Add M01 variables module"
```

El mensaje debe describir qué cambió.

---

# 📌 Flujo básico

Durante este curso utilizaremos siempre:

```bash id="q57s2v"
git add .

git commit -m "mensaje"

git push origin main
```

---

# ☁️ Enviar cambios a GitHub

Ejecutar:

```bash id="7q8q3t"
git push origin main
```

Esto enviará los cambios al repositorio remoto.

---

# 📥 Descargar cambios

Si trabajás desde otra computadora:

```bash id="4syqto"
git pull
```

Descarga los cambios más recientes.

---

# 📜 Ver historial

Ejecutar:

```bash id="0pbny0"
git log
```

Muestra todos los commits realizados.

Ejemplo:

```text id="c1zn7f"
commit xxxxxxxxx

Author: Enzo Bruno

Add M01 variables module
```

---

# 📌 Comandos que más usaremos

| Comando                   | Función           |
| ------------------------- | ----------------- |
| `git init`                | Crear repositorio |
| `git status`              | Ver cambios       |
| `git add .`               | Agregar archivos  |
| `git commit -m "mensaje"` | Guardar cambios   |
| `git push origin main`    | Enviar a GitHub   |
| `git pull`                | Descargar cambios |
| `git log`                 | Ver historial     |

---

# ⚠ Problemas frecuentes

## "Author identity unknown"

Ejemplo:

```text id="1agjlwm"
Please tell me who you are
```

Solución:

Ejecutar:

```bash id="wbn1x4"
git config --global user.name "Tu Nombre"

git config --global user.email "tu@email.com"
```

---

## "nothing to commit"

Ejemplo:

```text id="n40iqd"
nothing to commit, working tree clean
```

Significa:

```text id="k0xvhv"
No hay cambios para guardar.
```

No es un error.

---

## "fatal: not a git repository"

Ejemplo:

```text id="4ih6tx"
fatal: not a git repository
```

Significa que todavía no ejecutaste:

```bash id="6rjlwm"
git init
```

---

# 🎯 Objetivo

Si llegaste hasta acá deberías poder:

✅ Configurar Git.

✅ Crear un repositorio.

✅ Ejecutar:

```bash id="jj3r6a"
git init

git add .

git commit -m "Primer commit"
```

✅ Ver tus commits con:

```bash id="hl7khm"
git log
```

---

# 🚀 Próximo paso

Continuar con:

```text id="uw3bhf"
08_primer_programa.md
```