from flask import jsonify
from config import get_db_connection

def list_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT id_usuario, nome, email, tipo FROM usuario")
        users = cursor.fetchall()
        
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": f"Erro ao listar usuários: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()