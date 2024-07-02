import json
import pymysql
import boto3

def lambda_handler(event, context):
    # Conexión a RDS
    connection = pymysql.connect(
        host='tu-rds-endpoint',
        user='tu-usuario',
        password='tu-contraseña',
        database='tu-base-de-datos'
    )
    
    cursor = connection.cursor()
    
    # Obtener el nombre del archivo desde el evento
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Descargar el archivo de S3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response['Body'].read())
    
    # Insertar datos en la base de datos
    sql = """
    INSERT INTO weather (city, temperature, weather, timestamp)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (data['city'], data['temperature'], data['weather'], data['timestamp']))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Datos insertados en RDS')
    }
