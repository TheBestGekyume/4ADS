from flask import jsonify, request
from models.trip import Trip

class TripController:
    @staticmethod
    def create():
        if request.method == 'POST':
            data = request.get_json()
            
            required_fields = ['origem', 'destino', 'horario_de_partida', 
                            'data_de_partida', 'preco', 'assentos', 'imgUrl']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Campos obrigatórios ausentes."}), 400
            
            try:
                if Trip.create(
                    data['origem'],
                    data['destino'],
                    data['horario_de_partida'],
                    data['data_de_partida'],
                    data['preco'],
                    data['assentos'],
                    data['imgUrl']
                ):
                    return jsonify({"success": "Nova viagem inserida com sucesso!"}), 201
                else:
                    return jsonify({"error": "Falha ao criar viagem"}), 500
            except Exception as e:
                return jsonify({"error": f"Erro ao inserir a viagem: {str(e)}"}), 500

    @staticmethod
    def list():
        try:
            trips = Trip.get_all()
            return jsonify(trips)
        except Exception as e:
            return jsonify({"error": f"Erro ao listar viagens: {str(e)}"}), 500

    @staticmethod
    def get_by_id(trip_id):
        try:
            trip = Trip.get_by_id(trip_id)
            if trip:
                return jsonify(trip)
            else:
                return jsonify({"error": "Viagem não encontrada."}), 404
        except Exception as e:
            return jsonify({"error": f"Falha ao buscar viagem: {str(e)}"}), 500

    @staticmethod
    def update():
        if request.method == 'PUT':
            data = request.get_json()
            
            required_fields = ['id_viagem', 'origem', 'destino', 
                            'horario_de_partida', 'data_de_partida', 'preco']
            if not all(field in data for field in required_fields):
                return jsonify({
                    "error": "Dados incompletos. Certifique-se de enviar todos os dados necessários."
                }), 400
            
            try:
                if Trip.update(
                    data['id_viagem'],
                    data['origem'],
                    data['destino'],
                    data['horario_de_partida'],
                    data['data_de_partida'],
                    data['preco']
                ):
                    return jsonify({"success": "Viagem atualizada com sucesso!"})
                else:
                    return jsonify({"error": "Viagem não encontrada."}), 404
            except Exception as e:
                return jsonify({"error": f"Erro ao atualizar a viagem: {str(e)}"}), 500

    @staticmethod
    def delete():
        if request.method == 'DELETE':
            data = request.get_json()
            
            if not data or 'id_viagem' not in data:
                return jsonify({
                    "status": "error", 
                    "message": "ID da viagem não fornecido."
                }), 400
            
            try:
                if Trip.delete(data['id_viagem']):
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
                return jsonify({
                    "status": "error",
                    "message": f"Erro ao excluir a viagem: {str(e)}"
                }), 500

    @staticmethod
    def purchase_seat():
        if request.method == 'PUT':
            data = request.get_json()

            if not all(key in data for key in ['id_viagem', 'assentos_indisponiveis', 'usuario_id']):
                return jsonify({
                    "erro": "Dados incompletos. Certifique-se de enviar 'id_viagem', 'assentos_indisponiveis' e 'usuario_id'."
                }), 400

            try:
                result = Trip.purchase_seats(
                    data['id_viagem'],
                    data['assentos_indisponiveis'],
                    data['usuario_id']
                )
                
                if result is not None:
                    return jsonify({
                        "mensagem": "Assentos comprados com sucesso e registrados!",
                        "assentos_comprados": result
                    }), 200
                else:
                    return jsonify({"erro": "Viagem não encontrada!"}), 404
            except Exception as e:
                return jsonify({"erro": f"Erro ao processar compra: {str(e)}"}), 500

    @staticmethod
    def list_user_trips():
        if request.method == 'POST':
            data = request.get_json()
            
            if not data or 'usuario_id' not in data:
                return jsonify({
                    "status": 400,
                    "mensagem": "ID do usuário não enviado"
                }), 400
            
            try:
                trips = Trip.get_user_trips(data['usuario_id'])
                return jsonify({'viagens': trips})
            except Exception as e:
                return jsonify({
                    "error": f"Erro ao buscar viagens: {str(e)}"
                }), 500