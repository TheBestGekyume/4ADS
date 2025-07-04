from flask import jsonify, request
from config import get_db_connection
import json

def create_trip():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        data = request.get_json()
        
        required_fields = ['origem', 'destino', 'horario_de_partida', 
                          'data_de_partida', 'preco', 'assentos', 'imgUrl']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Campos obrigatórios ausentes."}), 400
        
        try:
            # Gerar assentos
            total_assentos = int(data['assentos'])
            assentos = []
            metade = total_assentos / 2
            
            for i in range(1, total_assentos + 1):
                letra = "A" if i <= metade else "B"
                numero = i if i <= metade else i - int(metade)
                
                assentos.append({
                    "nro_assento": f"{letra}{numero}",
                    "disponivel": True
                })
            
            assentos_json = json.dumps(assentos)
            
            query = """
                INSERT INTO viagem 
                (origem, destino, horario_de_partida, data_de_partida, 
                 preco, status, imgUrl, assentos) 
                VALUES (%s, %s, %s, %s, %s, 1, %s, %s)
            """
            cursor.execute(query, (
                data['origem'],
                data['destino'],
                data['horario_de_partida'],
                data['data_de_partida'],
                data['preco'],
                data['imgUrl'],
                assentos_json
            ))
            conn.commit()
            
            return jsonify({"success": "Nova viagem inserida com sucesso!"}), 201
        except Exception as e:
            conn.rollback()
            return jsonify({"error": f"Erro ao inserir a viagem: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()