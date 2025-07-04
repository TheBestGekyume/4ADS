from flask import jsonify, request
from config import get_db_connection
import json

def list_user_trips():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        data = request.get_json()
        
        if not data or 'usuario_id' not in data:
            return jsonify({
                "status": 400,
                "mensagem": "ID do usuário não enviado"
            }), 400
        
        try:
            query = """
                SELECT v.id_viagem, v.origem, v.destino, v.horario_de_partida, 
                       v.data_de_partida, v.preco, uv.usuario_viagem_id, uv.assentos
                FROM viagem v
                INNER JOIN usuario_viagem uv ON v.id_viagem = uv.viagem_id
                WHERE uv.usuario_id = %s
            """
            cursor.execute(query, (data['usuario_id'],))
            trips = cursor.fetchall()
            
            formatted_trips = []
            for trip in trips:
                assentos_comprados = json.loads(trip['assentos']) if trip['assentos'] else []
                
                formatted_trips.append({
                    'id_viagem': trip['id_viagem'],
                    'origem': trip['origem'],
                    'destino': trip['destino'],
                    'horario_de_partida': trip['horario_de_partida'],
                    'data_de_partida': trip['data_de_partida'],
                    'preco': trip['preco'],
                    'usuario_viagem_id': trip['usuario_viagem_id'],
                    'assentos': assentos_comprados
                })
            
            return jsonify({'viagens': formatted_trips})
        except Exception as e:
            return jsonify({
                "error": f"Erro ao buscar viagens: {str(e)}"
            }), 500
        finally:
            cursor.close()
            conn.close()