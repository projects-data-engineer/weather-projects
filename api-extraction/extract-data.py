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
#url2=f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

print(url)

# Solicitud a la API
response = requests.get(url)
print("response", response)

# Verificar si la solicitud fue exitosa
if response.status_code != 200:
    raise Exception(f"Error en la solicitud a la API: {response.status_code}, {response.text}")


data = response.json()

# Guardar los datos en un archivo JSON
filename = f'./data/weather_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.json'
with open(filename, 'w') as f:
    json.dump(data, f)


print(json.dumps(data, indent=4))

