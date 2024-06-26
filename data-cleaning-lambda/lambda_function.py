import json
import boto3

def lambda_handler(event, context):
    # Obtener el nombre del archivo desde el evento
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Descargar el archivo de S3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response['Body'].read())
    
    # Limpieza de datos (ejemplo: extraer solo algunos campos)
    cleaned_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description'],
        'timestamp': data['dt']
    }
    
    # Guardar los datos limpios en un nuevo archivo
    cleaned_filename = f'cleaned_{key}'
    s3.put_object(Bucket=bucket, Key=cleaned_filename, Body=json.dumps(cleaned_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Limpieza de datos completada')
    }
