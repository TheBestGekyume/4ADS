from flask import jsonify, request
from config import get_db_connection

def get_trip_by_id():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    trip_id = request.args.get('id_viagem')
    if not trip_id:
        return jsonify({"error": "Parâmetro 'id_viagem' é obrigatório."}), 400
    
    try:
        cursor.execute("SELECT * FROM viagem WHERE id_viagem = %s", (trip_id,))
        trip = cursor.fetchone()
        
        if trip:
            return jsonify(trip)
        else:
            return jsonify({"error": "Viagem não encontrada."}), 404
    except Exception as e:
        return jsonify({"error": f"Falha ao buscar viagem: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()