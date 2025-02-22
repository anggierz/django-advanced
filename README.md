# Django avanzado
Desarrollo de un servidor con Django de temática libre.

## Descripción del proyecto

Este repositorio incluye la actividad 4: Django avanzado del Módulo 2. Fundamentos de Backend con Python del Máster de Desarrollo Web de la UEM.

Se implementa un servidor Django completo para el modelo de una clínica con pacientes y doctores. Los pacientes se consideran
usuarios de la clínica que pueden concertar citas con los doctores.

## Funcionalidades

**Modelo de la clínica**:
   - Existen dos grupos: usuarios y administradores.
   - Los administradores se encargan de gestionar los doctores de la clínica.
   - Los usuarios pueden listar los doctores de la clínica y concertar citas médicas con ellos.

## Instrucciones de uso

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto a tu máquina local

### 2. Instalar dependencias 

Instala las dependencias que se encuentran en el archivo requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Levantar los endpoints

Finalmente, levanta las rutas para poder utilizarlas (debes de estar dentro del directorio myproject)

```bash
python manage.py runserver
```