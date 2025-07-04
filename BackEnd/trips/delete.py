from flask import jsonify, request
from config import get_db_connection

def delete_trip():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'DELETE':
        data = request.get_json()
        
        if not data or 'id_viagem' not in data:
            return jsonify({
                "status": "error", 
                "message": "ID da viagem não fornecido."
            }), 400
        
        try:
            query = "DELETE FROM viagem WHERE id_viagem = %s"
            cursor.execute(query, (data['id_viagem'],))
            conn.commit()
            
            if cursor.rowcount > 0:
                return jsonify({
                    "status": "success",
                    "message": "Viagem excluída com sucesso!"
                })
            else:
                return jsonify({
                    "status": "error",
                    "message": "Viagem não encontrada."
                }), 404
        except Exception as e:
            conn.rollback()
            return jsonify({
                "status": "error",
                "message": f"Erro ao excluir a viagem: {str(e)}"
            }), 500
        finally:
            cursor.close()
            conn.close()