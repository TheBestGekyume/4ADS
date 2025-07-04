from flask import jsonify, request
from config import get_db_connection

def edit_trip():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'PUT':
        data = request.get_json()
        
        required_fields = ['id_viagem', 'origem', 'destino', 
                          'horario_de_partida', 'data_de_partida', 'preco']
        if not all(field in data for field in required_fields):
            return jsonify({
                "error": "Dados incompletos. Certifique-se de enviar todos os dados necessários."
            }), 400
        
        try:
            # Verificar se a viagem existe
            cursor.execute("SELECT id_viagem FROM viagem WHERE id_viagem = %s", 
                          (data['id_viagem'],))
            if not cursor.fetchone():
                return jsonify({"error": "Viagem não encontrada."}), 404
            
            query = """
                UPDATE viagem 
                SET origem = %s, 
                    destino = %s, 
                    horario_de_partida = %s, 
                    data_de_partida = %s, 
                    preco = %s
                WHERE id_viagem = %s
            """
            cursor.execute(query, (
                data['origem'],
                data['destino'],
                data['horario_de_partida'],
                data['data_de_partida'],
                data['preco'],
                data['id_viagem']
            ))
            conn.commit()
            
            return jsonify({"success": "Viagem atualizada com sucesso!"})
        except Exception as e:
            conn.rollback()
            return jsonify({"error": f"Erro ao atualizar a viagem: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()