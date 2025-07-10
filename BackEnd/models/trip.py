import json
from config import get_db_connection

class Trip:
    def __init__(self, id_viagem=None, origem=None, destino=None, horario_de_partida=None,
                 data_de_partida=None, preco=None, status=None, imgUrl=None, assentos=None):
        self.id_viagem = id_viagem
        self.origem = origem
        self.destino = destino
        self.horario_de_partida = horario_de_partida
        self.data_de_partida = data_de_partida
        self.preco = preco
        self.status = status
        self.imgUrl = imgUrl
        self.assentos = assentos

    @classmethod
    def create(cls, origem, destino, horario_de_partida, data_de_partida, preco, assentos, imgUrl):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            # Gerar assentos
            total_assentos = int(assentos)
            assentos_list = []
            metade = total_assentos / 2
            
            for i in range(1, total_assentos + 1):
                letra = "A" if i <= metade else "B"
                numero = i if i <= metade else i - int(metade)
                
                assentos_list.append({
                    "nro_assento": f"{letra}{numero}",
                    "disponivel": True
                })
            
            assentos_json = json.dumps(assentos_list)
            
            cursor.execute(
                """INSERT INTO viagem 
                (origem, destino, horario_de_partida, data_de_partida, 
                 preco, status, imgUrl, assentos) 
                VALUES (%s, %s, %s, %s, %s, 1, %s, %s)""",
                (origem, destino, horario_de_partida, data_de_partida, preco, imgUrl, assentos_json)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM viagem ORDER BY id_viagem DESC")
            trips = cursor.fetchall()
            
            for trip in trips:
                if 'assentos' in trip and trip['assentos']:
                    trip['assentos'] = json.loads(trip['assentos'])
            
            return trips
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_by_id(cls, trip_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM viagem WHERE id_viagem = %s", (trip_id,))
            trip = cursor.fetchone()
            
            if trip and 'assentos' in trip and trip['assentos']:
                trip['assentos'] = json.loads(trip['assentos'])
            
            return trip
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def update(cls, id_viagem, origem, destino, horario_de_partida, data_de_partida, preco):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                """UPDATE viagem 
                SET origem = %s, destino = %s, horario_de_partida = %s, 
                    data_de_partida = %s, preco = %s
                WHERE id_viagem = %s""",
                (origem, destino, horario_de_partida, data_de_partida, preco, id_viagem)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete(cls, id_viagem):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM viagem WHERE id_viagem = %s", (id_viagem,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def purchase_seats(cls, id_viagem, assentos_indisponiveis, usuario_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT assentos FROM viagem WHERE id_viagem = %s", (id_viagem,))
            result = cursor.fetchone()

            if not result:
                return None

            assentos = json.loads(result['assentos'])
            assentos_comprados = []

            for assento_indisponivel in assentos_indisponiveis:
                for assento in assentos:
                    if (assento['nro_assento'] == assento_indisponivel['nro_assento'] and 
                        assento['disponivel'] == True):
                        assento['disponivel'] = False
                        assentos_comprados.append(assento['nro_assento'])
                        break

            assentos_json = json.dumps(assentos)

            cursor.execute(
                "UPDATE viagem SET assentos = %s WHERE id_viagem = %s",
                (assentos_json, id_viagem)
            )

            assentos_comprados_json = json.dumps(assentos_comprados)
            cursor.execute(
                "INSERT INTO usuario_viagem (usuario_id, viagem_id, assentos) VALUES (%s, %s, %s)",
                (usuario_id, id_viagem, assentos_comprados_json)
            )

            conn.commit()
            return assentos_comprados
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_user_trips(cls, usuario_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                """SELECT v.id_viagem, v.origem, v.destino, v.horario_de_partida, 
                          v.data_de_partida, v.preco, uv.usuario_viagem_id, uv.assentos
                   FROM viagem v
                   INNER JOIN usuario_viagem uv ON v.id_viagem = uv.viagem_id
                   WHERE uv.usuario_id = %s""",
                (usuario_id,)
            )
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
            
            return formatted_trips
        finally:
            cursor.close()
            conn.close()