import os
from dotenv import load_dotenv

import requests
import boto3
import json
from datetime import datetime
import pandas as pd
import glob


load_dotenv()

# Parámetros de la API
api_key = os.getenv('API_KEY')

city = 'Madrid'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


# Solicitud a la API
response = requests.get(url)
print("response", response)

# Verificar si la solicitud fue exitosa
if response.status_code != 200:
    raise Exception(f"Error en la solicitud a la API: {response.status_code}, {response.text}")


data = response.json()

# # Guardar los datos en un archivo JSON
filename = f'data/weather_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.json'

# Convertir el diccionario a una cadena JSON
json_data = json.dumps(data)


# Subir el archivo a S3
s3 = boto3.client('s3')
bucket_name = 'weather-bucket-data-project'

s3.put_object(Bucket=bucket_name, Key=filename, Body=json_data)

print(f'Datos guardados en S3: {filename}')
