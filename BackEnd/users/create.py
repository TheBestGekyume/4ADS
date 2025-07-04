from flask import jsonify, request
from config import get_db_connection

def create_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        data = request.get_json()
        
        required_fields = ['nome', 'senha', 'email', 'tipo']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Campos obrigatórios ausentes."}), 400
        
        try:
            query = """
                INSERT INTO usuario (nome, senha, email, tipo) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                data['nome'],
                data['senha'],
                data['email'],
                data['tipo']
            ))
            conn.commit()
            
            return jsonify({"success": "Novo usuario inserido com sucesso!"}), 201
        except Exception as e:
            conn.rollback()
            return jsonify({"error": f"Erro ao inserir o usuario: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()