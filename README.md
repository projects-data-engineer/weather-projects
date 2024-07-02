# weather-projects

0. [Entorno Virtual](#schema0)
1. [Archivo .env](#schema1)
2. [Claves de AWS](#schema2)
3. [Esctructura del proyecto](#schema3)
4. [Limpieza de Datos utilizando AWS Lambda](#schema4)
5. [Almacenamiento en Amazon RDS](#schema5)
6. [Unable to import module 'lambda_function': No module named 'pymysql'](#schema6)

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

## 2. Claves de AWS

1. Crear cuenta de amazon
2. Crear usuario no root.
3. Si ya se han usado el usario anterior y no te acuerdad de las claves `aws_access_key_id` y `aws_secret_access_key` usar el siguiente comando para buscar la configuración de AWS
```bash
ls ~/.aws
```
Deberían aparecer las siguientes carpetas
```bash
config  credentials
```
4. Abrir el visual con en esa ruta
```bash
code ~/.aws
```
5. Copiar las crendeciales a un archivo `.env`


<hr>

<a name="schema3"></a>

## 3. Esctructura del proyecto

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


<hr>

<a name="schema4"></a>

## 4. Limpieza de Datos utilizando AWS Lambda

### **Paso 0: Crear un bucket s3 para guardar los datos limpios

- **A. Crear un Bucket en Amazon S3**
    1. Navegar a la Consola de Amazon S3:

    2. Crear un Nuevo Bucket:

        Haz clic en "Create bucket".
Asigna un nombre único a tu bucket (por ejemplo, my-weather-data-bucket-clean).
Configura las opciones necesarias y crea el bucket.


### **Paso 1: Crear la Función Lambda**
- **A. Crear la Función Lambda en AWS**
    1. Navegar a la Consola de AWS Lambda:
    2. Crear una Nueva Función:
        Haz clic en "Create function".
        - Selecciona "Author from scratch".
        - Asigna un nombre a tu función (por ejemplo, `WeatherDataCleaner`).
        - Selecciona el runtime como `Python 3.8` (o la versión que prefieras).
        - Selecciona o crea un rol de ejecución con permisos necesarios (ver sección de permisos más abajo).
    3. Configurar el Código de la Función:

        - En la sección de "Function code", copia y pega el código proporcionado en el editor de código de Lambda.[Este código](./data-cleaning-lambda/lambda_function.py)
### **Paso 2: Configurar Permisos y Roles**
- **A. Crear un Rol de IAM para la Función Lambda**
    1. Navegar a la Consola de IAM:

    2. Crear un Nuevo Rol:

        - Haz clic en "Roles" y luego en "Create role".
        - Selecciona "Lambda" como el tipo de entidad de confianza.
        - Adjunta las políticas gestionadas por AWS: `AmazonS3FullAccess` y `AWSLambdaBasicExecutionRole`.
        ![S3](./img/l_s3_role.png)
    3. Asignar el Rol a la Función Lambda:

        - Regresa a la consola de Lambda y asigna este rol a tu función Lambda en la sección "Execution role".

### **Paso 4: Configurar un Trigger en S3**
1. Agregar un Trigger en la Función Lambda:
    - En la consola de Lambda, en la configuración de tu función, haz clic en "Add trigger".
    - Selecciona "S3" como la fuente del trigger.
    - Selecciona el bucket que contenga los datos `weather-bucket-data-project`.
    - Configura el evento para que se active en "ObjectCreated (All)".
    - Crear una **variable de entorno** en la lambda con el bucket donde se va a guardar los datos `my-weather-data-bucket-clean`
    - Guarda la configuración.



Bucket `weather-bucket-data-project`

![Data](./img/s3_data.png)
![Data](./img/s3_data_2.png)

Bucket `my-weather-data-bucket-clean`

![Data clean](./img/s3_clean.png)
![Data clean](./img/s3_clean_data.png)


<hr>

<a name="schema5"></a>

## 5. Almacenamiento en Amazon RDS 

### **Paso 1: Crear una Instancia de Amazon RDS**
1. Abrir la Consola de RDS:

    - Ve a la consola de administración de AWS y selecciona "RDS" en la sección "Database".
2. Crear una Nueva Instancia de RDS:

    - Haz clic en "Create database".
    - Selecciona "Standard Create".
    - Elige "MySQL" como el motor de base de datos.
    - Configura la versión de MySQL y el tipo de instancia que prefieras (por ejemplo, `db.t2.micro` para el plan gratuito).
3. Configurar la Autenticación:

    - Ingresa un nombre de usuario y contraseña para el administrador de la base de datos.
    - Nota: Guarda estos detalles porque los necesitarás para la configuración de la función Lambda.
4. Configurar la Red:

    - Selecciona la VPC y las subnets donde deseas que se implemente la base de datos.
    - Asegúrate de que "Public accessibility" esté habilitado si necesitas acceder a la base de datos desde fuera de la VPC.
5. Configuraciones Adicionales:

    - Configura parámetros adicionales según tus necesidades (por ejemplo, grupo de seguridad, parámetros de backup, etc.).
    - Haz clic en "Create database".
6. Obtener el Endpoint de la Base de Datos:

    - Una vez creada la instancia, ve a la sección "Databases" y selecciona tu nueva base de datos.
    - Copia el "Endpoint" que se mostrará, porque lo necesitarás para la función Lambda.

## **Paso 2: Crear la Función Lambda para Insertar Datos en RDS**
1. Crear una Nueva Función Lambda:

    - Ve a la consola de Lambda y haz clic en "Create function".
    - Selecciona "Author from scratch".
    - Ingresa un nombre para la función y selecciona el entorno de ejecución (por ejemplo, Python 3.8).
2. Configurar el Rol de Ejecución:

    - Crea un nuevo rol con permisos básicos de Lambda y añade permisos adicionales para conectarse a RDS.
    - Puedes usar una política administrada como `AmazonRDSFullAccess` para este propósito.
    ![Role](./img/l_rds_role.png)
3. Subir el Código de la Función:

    - Usa el siguiente código para insertar datos en la base de datos RDS:
    [Code](./rds-lambda/rds_lambda_function.py)
4. Agregar Triggers a la Función Lambda:

    - Configura un trigger de S3 para que la función Lambda se ejecute cuando se cree un nuevo archivo en el bucket de S3.

<hr>

<a name="schema6"></a>

## 6. Unable to import module 'lambda_function': No module named 'pymysql'

El error `Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'pymysql'` indica que la función Lambda no puede encontrar el módulo `pymysql` porque no está incluido en el entorno de ejecución de Lambda por defecto.

Para solucionar este problema, debes incluir `pymysql` en un paquete de implementación (deployment package) y luego subir ese paquete a Lambda. 

### **Paso 1: Preparar el Entorno Virtual**
1. Activar el Entorno Virtual:
```bash 
cd /ruta/a/tu/proyecto
source weather-projects/bin/activate  
```

### **Paso 2: Instalar Dependencias en la Carpeta `rds_lambda`**
Dentro de tu entorno virtual, instala pymysql en la carpeta `rds_lambda`.
```bash
pip install pymysql -t rds_lambda/
```

### **Paso 3: Crear el Paquete de Implementación**
1. Navegar a la Carpeta `rds_lambda`:

```bash
cd rds_lambda
```
2. Crear el Archivo ZIP:
Comprime todo el contenido de la carpeta rds_lambda en un archivo ZIP.

```bash
zip -r ../lambda_package.zip .
```
### **Paso 4: Subir el Paquete a Lambda**
1. Subir el Paquete a Lambda:

    - Ve a la consola de AWS Lambda.
    - Selecciona tu función Lambda.
    - En la pestaña "Code", selecciona "Upload from" y luego ".zip file".
    - Sube el archivo `lambda_package.zip`.
### **Paso 5: Configurar la Función Lambda**
1. Asignar el Rol Correcto:
Asegúrate de que la función Lambda tenga el rol con los permisos adecuados (S3 y RDS).

2. Configurar Variables de Entorno:
En la consola de Lambda, configura las variables de entorno necesarias, como las credenciales de la base de datos RDS.

### **Paso 6: Prueba la Función Lambda**
1. Configura un Evento de Prueba:
En la consola de Lambda, crea un evento de prueba que simule un evento S3.

2. Ejecuta la Función y Verifica los Logs:
Ejecuta la función Lambda y verifica los logs en CloudWatch para asegurarte de que la función se está ejecutando correctamente y que los datos se insertan en RDS como se espera.

