import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'viacaocalango'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        raise