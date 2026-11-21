# Python · 2º SMR

Ejercicios, prácticas y exámenes de Python del segundo curso del Grado Medio de Sistemas Microinformáticos y Redes (curso 2025-2026), organizados por temas.

## Requisitos

- **Python 3.10** o superior (algunos programas usan `match`/`case`).
- Muchos programas limpian la pantalla con `os.system("cls")`, que es de Windows. En Linux o macOS no da error, pero no limpia la pantalla.

## Cómo ejecutar

```bash
python 02-Bucles/ejercicios-for/1.py
```

En los proyectos con varios archivos, como el examen de POO, hay que ejecutar el programa principal desde su carpeta:

```bash
cd 05-POO/examen-poo
python examen.py
```

## Contenido

### [01 · Introducción](01-Introduccion)
Variables, operadores, entrada y salida, y condicionales.

| Carpeta | Contenido |
|---|---|
| [primeros-programas](01-Introduccion/primeros-programas) | Primeras pruebas y ejercicios sueltos (incluye Fibonacci) |
| [ejemplos-clase](01-Introduccion/ejemplos-clase) | Ejemplos hechos en clase |
| [examen-condicionales](01-Introduccion/examen-condicionales) | Examen de `if` / `else` |

### [02 · Bucles](02-Bucles)

| Carpeta | Contenido |
|---|---|
| [ejercicios-for](02-Bucles/ejercicios-for) | Relación de ejercicios con `for` |
| [ejercicios-while](02-Bucles/ejercicios-while) | Relación de ejercicios con `while` |
| [relacion-bucles](02-Bucles/relacion-bucles) | 20 ejercicios de bucles |
| [bucles-anidados](02-Bucles/bucles-anidados) | Bucles anidados |
| [control-de-errores](02-Bucles/control-de-errores) | Validación de entrada con `try` / `except` |
| [otros](02-Bucles/otros) | Detector de números primos |
| [examen-bucles](02-Bucles/examen-bucles) · [examen-bucles-c](02-Bucles/examen-bucles-c) | Exámenes de bucles |

### [03 · Funciones](03-Funciones)

| Carpeta | Contenido |
|---|---|
| [ejercicios](03-Funciones/ejercicios) | Áreas de figuras, ejercicios con dinero… |
| [ejercicios-clase](03-Funciones/ejercicios-clase) | Ejercicios de clase (depósito, alumnos…) |
| [examen-a](03-Funciones/examen-a) · [examen-b](03-Funciones/examen-b) · [examen-c](03-Funciones/examen-c) · [examen-d](03-Funciones/examen-d) | Modelos de examen de funciones |

### [04 · Colecciones de datos](04-Colecciones-de-datos)
Listas, tuplas y diccionarios.

| Carpeta | Contenido |
|---|---|
| [listas](04-Colecciones-de-datos/listas) | Ejercicios con listas |
| [relacion-ejercicios](04-Colecciones-de-datos/relacion-ejercicios) | Relación de 14 ejercicios |
| [ejercicio-clase](04-Colecciones-de-datos/ejercicio-clase) | Ejercicio de clase |

### [05 · Programación orientada a objetos](05-POO)

| Carpeta | Contenido |
|---|---|
| [objetos](05-POO/objetos) | Primeras clases y objetos |
| [relacion-1](05-POO/relacion-1) · [relacion-2](05-POO/relacion-2) | Relaciones de ejercicios de POO |
| [examen-poo](05-POO/examen-poo) | Gestión de alumnos y notas cargados desde un fichero |
| [fase-2](05-POO/fase-2) | Clases `Coche`, `CuentaBancaria`… |

> El fichero `2A.txt` del examen de POO contiene alumnos inventados, para que el programa se pueda probar sin datos reales.
