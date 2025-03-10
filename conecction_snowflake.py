def conecction_snowflake(name_connection,name_database):
    """
    Establece una conexión a una base de datos de Snowflake utilizando las credenciales almacenadas
    en un archivo de configuración de SnowSQL y selecciona una base de datos específica.

    Parámetros:
    - name_connection (str): El nombre de la conexión que se utilizará para obtener las credenciales
      del archivo de configuración de SnowSQL.
    - name_database (str): El nombre de la base de datos de Snowflake a la que se desea conectar.

    Retorna:
    - cursor: Un objeto cursor de Snowflake que se puede utilizar para ejecutar consultas SQL.

    Ejemplo de uso:

    cursor = conecction_snowflake('mi_conexion', 'mi_base_de_datos')
    """
    import snowflake.connector
    import os
    import configparser
        
    # Obtener la ruta del archivo de configuración de SnowSQL
    config_path = os.path.join(os.environ['USERPROFILE'], '.snowsql', 'config')

    # Leer el archivo de configuración
    config = configparser.ConfigParser()
    config.read(config_path)
    
    # Obtener las credenciales de la sección [connections.example]
    try:
        section_name=f'connections.{name_connection}'
        account = config[section_name]['accountname']
        user = config[section_name]['username']
        password = config[section_name]['password']
    except KeyError as e:
        print(f"Error: No se encontraron las credenciales en el archivo de configuración: {e}")
        exit()

    # Conexión a Snowflake
    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account
        )
        print("Conexión exitosa a Snowflake")

    except Exception as e:
        print(f"Error de conexión: {e}")

  # Seleccionar la base de datos
    try:
        cursor = conn.cursor()
        cursor.execute(f'USE DATABASE {name_database}')
        print(f'Conexión exitosa a la base de datos: {name_database}')
    except Exception as e:
        print(f"Error al seleccionar la base de datos: {e}")


    return cursor  
        