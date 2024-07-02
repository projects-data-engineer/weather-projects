import boto3
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurar el cliente de Athena
athena_client = boto3.client('athena', region_name='us-east-1')

# Configurar los parámetros de la consulta
query = "SELECT * FROM weather_data LIMIT 10;"
database = "default"
output_location = 's3://my-athena-queries-bucket/queries/'

# Ejecutar la consulta
response = athena_client.start_query_execution(
    QueryString=query,
    QueryExecutionContext={'Database': database},
    ResultConfiguration={'OutputLocation': output_location}
)

# Obtener el ID de la ejecución de la consulta
query_execution_id = response['QueryExecutionId']

# Esperar a que la consulta se complete
status = 'QUEUED'
while status in ['QUEUED', 'RUNNING']:
    response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
    status = response['QueryExecution']['Status']['State']
    if status in ['FAILED', 'CANCELLED']:
        raise Exception(f"Query failed or was cancelled with status: {status}")
    time.sleep(5)  # Espera 5 segundos antes de volver a verificar el estado

# Obtener los resultados de la consulta
response = athena_client.get_query_results(QueryExecutionId=query_execution_id)

# Procesar los resultados en un DataFrame de Pandas
rows = [row['Data'] for row in response['ResultSet']['Rows']]
header = [col['VarCharValue'] for col in rows[0]]
data = [[col.get('VarCharValue', None) for col in row] for row in rows[1:]]

df = pd.DataFrame(data, columns=header)


df['temperature'] = df['temperature'].astype(float)

#Convertir 'timestamp' a tipo int64 (timestamp Unix)
df['timestamp'] = df['timestamp'].astype('int64')

# Convertir timestamp Unix a datetime
df['timestamp'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

# # Visualizar los datos con Seaborn
# sns.set(style="whitegrid")
# plt.figure(figsize=(10, 6))
# sns.barplot(x='city', y='temperature', data=df)
# plt.title('Temperaturas por Ciudad')
# plt.xlabel('Ciudad')
# plt.ylabel('Temperatura')
# plt.show()

#scatter
plt.figure(figsize=(10, 6))
sns.scatterplot(x='timestamp', y='temperature', data=df)
plt.title('Temperature Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# plt.figure(figsize=(10, 6))
# sns.boxplot(x='city', y='temperature', data=df)
# plt.title('Temperature Distribution by City')
# plt.xlabel('City')
# plt.ylabel('Temperature')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Gráfico de líneas
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='timestamp', y='temperature', data=df, marker='o')
# plt.title('Temperature Over Time')
# plt.xlabel('Timestamp')
# plt.ylabel('Temperature')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()