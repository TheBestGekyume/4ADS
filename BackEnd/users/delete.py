from flask import jsonify, request
from config import get_db_connection

def delete_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'DELETE':
        data = request.get_json()
        
        if not data or 'id_usuario' not in data:
            return jsonify({
                "status": "error", 
                "message": "ID do usuário não fornecido."
            }), 400
        
        try:
            query = "DELETE FROM usuario WHERE id_usuario = %s"
            cursor.execute(query, (data['id_usuario'],))
            conn.commit()
            
            if cursor.rowcount > 0:
                return jsonify({
                    "status": "success",
                    "message": "Usuário excluído com sucesso!"
                })
            else:
                return jsonify({
                    "status": "error",
                    "message": "Usuário não encontrado."
                }), 404
        except Exception as e:
            conn.rollback()
            return jsonify({
                "status": "error",
                "message": f"Erro ao excluir o usuário: {str(e)}"
            }), 500
        finally:
            cursor.close()
            conn.close()