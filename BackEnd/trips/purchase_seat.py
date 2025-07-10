from flask import jsonify, request
import json
import mysql.connector
from config import db_config

def purchase_seat():
    if request.method == 'PUT':
        data = request.get_json()

        if not all(key in data for key in ['id_viagem', 'assentos_indisponiveis', 'usuario_id']):
            return jsonify({"erro": "Dados incompletos. Certifique-se de enviar 'id_viagem', 'assentos_indisponiveis' e 'usuario_id'."}), 400

        id_viagem = data['id_viagem']
        assentos_indisponiveis = data['assentos_indisponiveis']
        usuario_id = data['usuario_id']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)

            # Verifica se a viagem existe
            cursor.execute("SELECT assentos FROM viagem WHERE id_viagem = %s", (id_viagem,))
            result = cursor.fetchone()

            if not result:
                return jsonify({"erro": "Viagem não encontrada!"}), 404

            assentos = json.loads(result['assentos'])
            assentos_comprados = []

            # Atualiza os assentos
            for assento_indisponivel in assentos_indisponiveis:
                for assento in assentos:
                    if (assento['nro_assento'] == assento_indisponivel['nro_assento'] and 
                        assento['disponivel'] == True):
                        assento['disponivel'] = False
                        assentos_comprados.append(assento['nro_assento'])
                        break

            assentos_json = json.dumps(assentos)

            # Atualiza a viagem com os novos assentos
            cursor.execute(
                "UPDATE viagem SET assentos = %s WHERE id_viagem = %s",
                (assentos_json, id_viagem)
            )

            # Registra a compra na tabela usuario_viagem
            assentos_comprados_json = json.dumps(assentos_comprados)
            cursor.execute(
                "INSERT INTO usuario_viagem (usuario_id, viagem_id, assentos) VALUES (%s, %s, %s)",
                (usuario_id, id_viagem, assentos_comprados_json)
            )

            conn.commit()
            return jsonify({"mensagem": "Assentos comprados com sucesso e registrados!"}), 200

        except mysql.connector.Error as err:
            return jsonify({"erro": f"Erro de banco de dados: {err}"}), 500
        except Exception as e:
            return jsonify({"erro": f"Erro inesperado: {e}"}), 500
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
    else:
        return jsonify({"erro": "Método não permitido"}), 405