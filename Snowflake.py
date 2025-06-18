import snowflake.connector

# Configura tus credenciales de Snowflake
conn = snowflake.connector.connect(
    user='SF47575@stellantis.com',
    password='QAZ97qaz',
    account='rr67688.north-europe.azure.snowflakecomputing.com',  # ejemplo: 'abc12345.us-east-1'
    warehouse='WH_DVZ_SCM_CLUSTER'
)

try:
    # Crear un cursor
    cur = conn.cursor()
    # Ejecutar la consulta para listar las tablas
    cur.execute("SHOW TABLES")
    # Obtener los resultados
    for row in cur.fetchall():
        print(row)
finally:
    cur.close()
    conn.close()