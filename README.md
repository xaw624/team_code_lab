# Team Code Lab 🧪🐍

Repositorio de ejercicios para practicar **Python**, debugging y resolución de problemas.

La idea es que cada integrante del equipo pueda trabajar en ejercicios pequeños enfocados en habilidades específicas.

---

# 📦 Clonar el repositorio

```bash
git clone https://github.com/xaw624/team_code_lab.git
cd team_code_lab
```

---

# ⚙️ Instalar dependencias

Se recomienda trabajar dentro de un **entorno virtual**.

## Crear entorno virtual

Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 📁 Estructura del proyecto

```
team_code_lab
│
├─ debug
│   ├─ exercise1
│   │   ├─ exercise1.py
│   │   └─ solutions
│   └─ exercise2
│       ├─ exercise2.py
│       └─ solutions
│
├─ solver
│   ├─ exercise1
│   │   ├─ exercise1.py
│   │   └─ solutions
│   └─ exercise2
│       ├─ exercise2.py
│       └─ solutions
│
└─ README.md
```

## Tipos de ejercicios

**debug/**
Ejercicios donde el código tiene errores y deben ser encontrados y corregidos.

**solver/**
Ejercicios donde se debe implementar la solución desde cero.

---

# 🧠 Cómo trabajar los ejercicios

1. Abrir el archivo del ejercicio:

```
exerciseX.md
```

2. Resolver el problema solicitado en el archivo.

3. Guardar tu solución dentro de la carpeta:

```
solutions/
```

---

# 🏷️ Nomenclatura de las soluciones

Cada solución debe seguir el siguiente formato:

```
solution_<nombre>_<apellido>.py
```

Ejemplo:

```
solution_juan_perez.py
solution_maria_garcia.py
```

Esto permite que varias personas entreguen soluciones al mismo ejercicio sin conflictos.

---

# 💡 Recomendaciones

* No modificar los archivos originales de los ejercicios.
* Colocar **solo tu solución** dentro de `solutions/`.
* Intenta primero resolver el problema sin buscar o usar IA, se puede buscar documentación de sintaxis del lenguaje o metodos.

---

# 🚀 Objetivo

El objetivo de este repositorio es:

* Practicar **Python**
* Mejorar habilidades de **debugging**
* Ejercitar **pensamiento algorítmico**
* Comparar diferentes enfoques de solución
