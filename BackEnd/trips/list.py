from flask import jsonify
from config import get_db_connection
import json

def list_trips():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM viagem ORDER BY id_viagem DESC")
        trips = cursor.fetchall()
        
        formatted_trips = []
        for trip in trips:
            assentos = json.loads(trip['assentos']) if trip['assentos'] else []
            
            formatted_trips.append({
                'id_viagem': trip['id_viagem'],
                'origem': trip['origem'],
                'destino': trip['destino'],
                'horario_de_partida': trip['horario_de_partida'],
                'data_de_partida': trip['data_de_partida'],
                'assentos': assentos,
                'preco': trip['preco'],
                'status': trip['status'],
                'imgUrl': trip.get('imgUrl', None)
            })
        
        return jsonify(formatted_trips)
    except Exception as e:
        return jsonify({"error": f"Erro ao listar viagens: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()