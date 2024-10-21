# 🧩 Proyecto Compilador para Lenguaje Reducido de C

## 📚 Desarrollo de Herramientas de Software (DHS)

### 👤 Alumnos Responsables

- 🧑‍🎓 Agustin Sepulveda
- 🧑‍🎓 Agustin Sanguesa

### 📖 Introducción

Este proyecto es un trabajo práctico para la materia DHS. El objetivo es desarrollar un compilador para una versión reducida del lenguaje C, realizando análisis léxico, sintáctico y semántico, además de generar una tabla de símbolos y un reporte de errores.

### ✅ Requisitos

El proyecto debe:

- Implementar análisis léxico, sintáctico y semántico.
- Generar un árbol sintáctico con ANTLR.
- Mostrar la tabla de símbolos cuando el archivo de entrada sea correcto.
- Reportar errores léxicos, sintácticos y semánticos por consola o archivo.

### 🚨 Tipos de Errores a Detectar

El compilador debe detectar los siguientes errores:

#### Errores Sintácticos:

- Falta de punto y coma ;
- Falta de apertura de paréntesis (
- Formato incorrecto en declaración de variables

#### Errores Semánticos:

- Doble declaración de identificador
- Uso de identificador no declarado
- Uso de identificador sin inicializar
- Identificador no utilizado
- Tipos de datos incompatibles

Cada error debe indicarse como **sintáctico** o **semántico**.

### 🛠️ Tecnologías Utilizadas

- ANTLR
- Python

### Instrucciones de Uso

1. Clonar el repositorio desde GitHub.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Entrar al directorio src con `cd src`.
4. Levantar el archivo del compilador con `antlr4 compilador.g4 -Dlanguage=Python3`.
5. Ejecutar `python main.py` para generar la tabla de valores.

### 💻 Entorno de Desarrollo

- Python 3.12.4
- ANTLR 4.13.2
- Git

### 📅 Fecha de Entrega

📆 Lunes 4 de Noviembre de 2024.
