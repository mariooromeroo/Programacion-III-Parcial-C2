# Programacion-III-Parcial-C2

El repositorio de Faker para Python es una biblioteca que genera datos falsos pero realistas para propósitos de prueba y desarrollo. Su función principal es crear información ficticia como nombres, direcciones, emails, textos, números de teléfono, fechas y muchos otros tipos de datos de manera rápida y sencilla. Una de sus características más destacadas es el soporte para múltiples localizaciones e idiomas, lo que permite generar datos específicos de diferentes regiones y países.

## Integrantes 

- Yoselin Andrea Linares Hernandez
- Katerinne Alejandra Mendez Garcia
- Mario Antonio Salamanca Romero

## Script 1: Generador de Estudiantes Universitarios

Este script genera datos ficticios de 8 estudiantes universitarios con información completa que incluye:

- **Datos personales**: nombre y apellido generados en español
- **Información académica**: carrera universitaria seleccionada aleatoriamente de una lista predefinida
- **Contacto**: email universitario generado automáticamente con el formato "nombre.apellido@universidad.edu"
- **Datos de matrícula**: número de matrícula de 8 dígitos
- **Rendimiento académico**: promedio entre 6.0 y 10.0, y semestre actual entre 1 y 10
- **Dirección**: dirección completa generada automáticamente

**Carreras universitarias incluidas:**
- Ingeniería Informática
- Medicina
- Derecho
- Administración de Empresas
- Psicología
- Arquitectura
- Biología
- Periodismo

## Script 2: Sistema de Gestión Clínica

Este script simula un sistema de gestión clínica generando datos ficticios de 4 pacientes con:

- **Datos personales**: nombre, apellido y edad entre 1 y 90 años
- **Características físicas**: peso entre 45-120 kg y altura entre 1.50-1.95 m
- **Información médica**: especialidad médica seleccionada aleatoriamente
- **Datos de seguro**: indica si tiene o no seguro médico
- **Información de contacto**: número de teléfono y dirección completa

**Especialidades médicas incluidas:**
- Medicina General
- Pediatría
- Cardiología
- Dermatología
- Oftalmología

## Instalación y Uso

Para ejecutar los scripts, instale la librería Faker con:
```bash
pip install faker
```

Luego ejecute cada script individualmente:
```bash
python generador_estudiantes.py
python sistema_clinico.py
```
