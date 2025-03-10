
# Snowflake Connection Utility

Este proyecto proporciona una función en Python para establecer una conexión a una base de datos de Snowflake utilizando credenciales almacenadas en un archivo de configuración de SnowSQL.

## Descripción

La función `conecction_snowflake` permite conectarse a una base de datos de Snowflake de manera sencilla, utilizando las credenciales configuradas en el archivo de configuración de SnowSQL. Esta función es útil para automatizar tareas que requieren acceso a bases de datos en Snowflake.

## Requisitos

- Python 3.x
- Paquete `snowflake-connector-python`
- Archivo de configuración de SnowSQL con las credenciales necesarias

## Instalación

1. **Instalar el conector de Snowflake para Python**:

   ```bash
   pip install snowflake-connector-python

2. **Configurar SnowSQL**:
Asegúrate de tener un archivo de configuración de SnowSQL en la ruta

~/.snowsql/config

## Uso

   ```bash
from your_module import conecction_snowflake

 #Establecer conexión a Snowflake

cursor = conecction_snowflake('nombre_conexion', 'nombre_base_de_datos')

#Usar el cursor para ejecutar consultas
 
 cursor.execute("SELECT * FROM your_table")
