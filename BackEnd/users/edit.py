from flask import jsonify, request
from config import get_db_connection

def edit_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'PUT':
        data = request.get_json()
        
        required_fields = ['id_usuario', 'nome', 'senha', 'email', 'tipo']
        if not all(field in data for field in required_fields):
            return jsonify({
                "error": "Campos obrigatórios ausentes. Certifique-se de enviar 'id_usuario', 'nome', 'senha', 'email', 'tipo'."
            }), 400
        
        try:
            query = """
                UPDATE usuario 
                SET nome = %s, senha = %s, email = %s, tipo = %s 
                WHERE id_usuario = %s
            """
            cursor.execute(query, (
                data['nome'],
                data['senha'],
                data['email'],
                data['tipo'],
                data['id_usuario']
            ))
            conn.commit()
            
            if cursor.rowcount > 0:
                return jsonify({"success": "Usuário atualizado com sucesso!"})
            else:
                return jsonify({"error": "Usuário não encontrado."}), 404
        except Exception as e:
            conn.rollback()
            return jsonify({"error": f"Erro ao atualizar o usuário: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()