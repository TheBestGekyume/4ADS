from flask import jsonify, request
from config import get_db_connection

def authenticate_user():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        data = request.get_json()
        
        if not data or 'email' not in data or 'senha' not in data:
            return jsonify({
                "status": 400,
                "mensagem": "Dados de autenticação incompletos"
            }), 400
        
        email = data['email']
        senha = data['senha']
        
        query = "SELECT id_usuario, nome, tipo FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        user = cursor.fetchone()
        
        if user:
            return jsonify({
                "status": 200,
                "mensagem": "Autenticação bem-sucedida",
                "id_usuario": user['id_usuario'],
                "nome": user['nome'],
                "tipo": user['tipo']
            })
        else:
            return jsonify({
                "status": 404,
                "mensagem": "Usuário não encontrado ou senha incorreta"
            }), 404
    
    cursor.close()
    conn.close()