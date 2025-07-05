from flask import jsonify, request
from config import get_db_connection

def get_trip_by_id(trip_id):  # Adicione o parâmetro trip_id aqui
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM viagem WHERE id_viagem = %s", (trip_id,))
        trip = cursor.fetchone()
        
        if trip:
            if 'assentos' in trip and trip['assentos']:
                import json
                trip['assentos'] = json.loads(trip['assentos'])
            return jsonify(trip)
        else:
            return jsonify({"error": "Viagem não encontrada."}), 404
    except Exception as e:
        return jsonify({"error": f"Falha ao buscar viagem: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()