# weather-projects

0. [Entorno Virtual](#schema0)
1. [Archivo .env](#schema1)
2. [Esctructura del proyecto](#schema2)


<hr>

<a name="schema0"></a>

## 1. Creación y Activación del Entorno Virtual
### **Crear un Entorno Virtual:**

Abre tu terminal y navega hasta el directorio de tu proyecto (donde deseas crear el entorno virtual).

```bash

cd /ruta/a/tu/proyecto
```
Luego, ejecuta el siguiente comando para crear un nuevo entorno virtual con virtualenv. Puedes reemplazar nombre_del_entorno con el nombre que desees para tu entorno virtual:

```bash
virtualenv weather-projects // nombre de ejemplo
```
Esto creará un directorio llamado weather-projects que contiene todo lo necesario para funcionar como un entorno virtual de Python.

### **Activar el Entorno Virtual:**

Una vez que hayas creado el entorno virtual, necesitas activarlo. La forma de activar el entorno virtual depende del sistema operativo:

En macOS y Linux:

En la carpeta de tu proyecto, ejecuta:

```bash

source weather-projectsl/bin/activate
```

### **Verificación:**

Cuando el entorno virtual se active correctamente, verás que el nombre del entorno virtual aparece antes del prompt en tu terminal. Por ejemplo:

```bash

(weather-projects) usuario@hostname:/ruta/a/tu/proyecto$
```

<hr>

<a name="schema1"></a>

## 1. Crear archivo .env

### Paso 1: Instalar python-dotenv
Primero, asegúrate de tener activado tu entorno virtual. Luego, instala la biblioteca python-dotenv:

```bash
pip install python-dotenv
```
### Paso 2: Crear el Archivo .env
En el directorio raíz de tu proyecto, crea un archivo llamado .env. Este archivo contendrá tus variables de entorno. Por ejemplo:

```makefile
API_KEY=tu_api_key_aqui
DB_HOST=tu_host_de_base_de_datos
DB_USER=tu_usuario_de_base_de_datos
DB_PASSWORD=tu_contraseña_de_base_de_datos
```
### Paso 3: Cargar el Archivo .env en Tu Script Python
Dentro de tu script Python, utiliza python-dotenv para cargar las variables de entorno desde el archivo .env. Aquí tienes un ejemplo de cómo hacerlo:

```python
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
api_key = os.getenv('API_KEY')
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Usar las variables de entorno en tu código
print(f"API Key: {api_key}")
print(f"Database Host: {db_host}")
print(f"Database User: {db_user}")
```
### Paso 4: Ocultar el archivo .env a git

Añadir al archivo `.gitignore` el archivo `.env` para tener protegidas las claves y no subirlas a git

<hr>

<a name="schema2"></a>

## 2. Esctructura del proyecto

1. Requisitos del Proyecto
- Lenguaje de programación: Python
- Proveedor de nube: AWS
- Tareas principales:
    - Extracción de datos desde una API
    - Limpieza de datos
    - Almacenamiento y exposición de resultados en AWS
2. Arquitectura del Proyecto
- Extracción de Datos:
    - Utilizaremos la API pública de OpenWeatherMap para obtener datos meteorológicos.

- Limpieza de Datos:

    - Implementaremos una función Lambda en AWS para la limpieza y transformación de datos.
- Almacenamiento y Exposición de Resultados:
    - Guardaremos los datos limpios en una base de datos gestionada por AWS (por ejemplo, Amazon RDS) y utilizaremos Amazon QuickSight para la visualización de datos.