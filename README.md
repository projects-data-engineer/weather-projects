# weather-projects

0. [Entorno Virtual](#schema0)
1. [Esctructura del proyecto](#schema1)


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

## 1- Esctructura del proyecto

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