from flask import jsonify, request
from config import get_db_connection
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
        
            required_fields = ['nome', 'senha', 'email']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Campos obrigatórios ausentes."}), 400
        
            user_type = data.get('tipo', '0')
        
            if user_type not in ['0', '1']:
                user_type = '0'
        
            try:
                if User.create(data['nome'], data['senha'], data['email'], user_type):
                    return jsonify({
                        "success": "Novo usuário criado com sucesso!",
                        "tipo": user_type
                    }), 201
                else:
                    return jsonify({"error": "Falha ao criar usuário"}), 500
            except Exception as e:
                return jsonify({"error": f"Erro ao criar usuário: {str(e)}"}), 500
            
    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.get_by_id(user_id)
            if user:
                return jsonify(user)
            else:
                return jsonify({"error": "Usuário não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar usuário: {str(e)}"}), 500

    @staticmethod
    def update():
        if request.method == 'PUT':
            data = request.get_json()
        
            updatable_fields = ['nome', 'email', 'senha', 'tipo']
            if not any(field in data for field in updatable_fields):
                return jsonify({
                    "error": "Pelo menos um campo deve ser enviado para atualização (nome, email, senha ou tipo)"
                }), 400
        
            try:
                conn = get_db_connection()
                cursor = conn.cursor(dictionary=True)
            
                cursor.execute(
                    "SELECT nome, email, senha FROM usuario WHERE id_usuario = %s",
                    (data['id_usuario'],))
                current_data = cursor.fetchone()
            
                if not current_data:
                    return jsonify({"error": "Usuário não encontrado"}), 404
            
                nome = data.get('nome', current_data['nome'])
                email = data.get('email', current_data['email'])
                senha = data.get('senha', current_data['senha'])
            
                query = """
                    UPDATE usuario 
                    SET nome = %s, email = %s, senha = %s
                    WHERE id_usuario = %s
                """
                cursor.execute(query, (
                    nome,
                    email,
                    senha,
                    data['id_usuario']
                ))
                conn.commit()
            
                return jsonify({
                    "success": "Usuário atualizado com sucesso!",
                   "updated_fields": {
                        "nome": 'nome' in data,
                        "email": 'email' in data,
                        "senha": 'senha' in data,
                    }
                })
            
            except Exception as e:
                conn.rollback()
                return jsonify({"error": f"Erro ao atualizar o usuário: {str(e)}"}), 500
            finally:
                cursor.close()
                conn.close()

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