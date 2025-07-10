from flask import jsonify, request
from models.user import User

class UserController:
    @staticmethod
    def authenticate():
        if request.method == 'POST':
            data = request.get_json()
            
            if not data or 'email' not in data or 'senha' not in data:
                return jsonify({
                    "status": 400,
                    "mensagem": "Dados de autenticação incompletos"
                }), 400
            
            user = User.authenticate(data['email'], data['senha'])
            
            if user:
                return jsonify({
                    "status": 200,
                    "mensagem": "Autenticação bem-sucedida",
                    "id_usuario": user['id_usuario'],
                    "nome": user['nome'],
                    "tipo": user['tipo']
                })
            else:
                return jsonify({
                    "status": 404,
                    "mensagem": "Usuário não encontrado ou senha incorreta"
                }), 404

    @staticmethod
    def create():
        if request.method == 'POST':
            data = request.get_json()
            
            required_fields = ['nome', 'senha', 'email', 'tipo']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Campos obrigatórios ausentes."}), 400
            
            try:
                if User.create(data['nome'], data['senha'], data['email'], data['tipo']):
                    return jsonify({"success": "Novo usuario inserido com sucesso!"}), 201
                else:
                    return jsonify({"error": "Falha ao criar usuário"}), 500
            except Exception as e:
                return jsonify({"error": f"Erro ao inserir o usuario: {str(e)}"}), 500

    @staticmethod
    def list():
        try:
            users = User.get_all()
            return jsonify(users)
        except Exception as e:
            return jsonify({"error": f"Erro ao listar usuários: {str(e)}"}), 500

    @staticmethod
    def update():
        if request.method == 'PUT':
            data = request.get_json()
            
            required_fields = ['id_usuario', 'nome', 'senha', 'email', 'tipo']
            if not all(field in data for field in required_fields):
                return jsonify({
                    "error": "Campos obrigatórios ausentes."
                }), 400
            
            try:
                if User.update(data['id_usuario'], data['nome'], data['senha'], data['email'], data['tipo']):
                    return jsonify({"success": "Usuário atualizado com sucesso!"})
                else:
                    return jsonify({"error": "Usuário não encontrado."}), 404
            except Exception as e:
                return jsonify({"error": f"Erro ao atualizar o usuário: {str(e)}"}), 500

    @staticmethod
    def delete():
        if request.method == 'DELETE':
            data = request.get_json()
            
            if not data or 'id_usuario' not in data:
                return jsonify({
                    "status": "error", 
                    "message": "ID do usuário não fornecido."
                }), 400
            
            try:
                if User.delete(data['id_usuario']):
                    return jsonify({
                        "status": "success",
                        "message": "Usuário excluído com sucesso!"
                    })
                else:
                    return jsonify({
                        "status": "error",
                        "message": "Usuário não encontrado."
                    }), 404
            except Exception as e:
                return jsonify({
                    "status": "error",
                    "message": f"Erro ao excluir o usuário: {str(e)}"
                }), 500