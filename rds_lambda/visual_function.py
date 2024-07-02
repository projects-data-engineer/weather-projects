import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros de conexión a la RDS
host = 'weather-db.crko62g8qujh.us-east-1.rds.amazonaws.com'
port = 3306  # Puerto predeterminado de MySQL
user = 'admin'
password = 'nanuk102'
database = 'weather-db'

# Conexión a la base de datos
conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
    connect_timeout=10 
)

# Consulta SQL
sql_query = "SELECT * FROM tabla_de_datos;"

# Ejecutar consulta y cargar datos en un DataFrame de pandas
df = pd.read_sql(sql_query, conn)

# Cerrar conexión
conn.close()

print(df.head())