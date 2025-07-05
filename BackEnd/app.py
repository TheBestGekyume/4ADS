from flask import Flask, request, jsonify
from flask_cors import CORS

# Import das rotas de usuário
from users.auth import authenticate_user
from users.create import create_user
from users.delete import delete_user
from users.edit import edit_user
from users.list import list_users
from users.trips import list_user_trips

# Import das rotas de viagem
from trips.create import create_trip
from trips.delete import delete_trip
from trips.edit import edit_trip
from trips.get_by_id import get_trip_by_id
from trips.list import list_trips

app = Flask(__name__)
CORS(app, resources={
    r"/autenticar": {
        "origins": "http://localhost:3000",  # Apenas um valor string
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True,
        "expose_headers": ["Content-Type"]
    }
})


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# Rotas de Usuário
@app.route('/autenticar', methods=['POST', 'OPTIONS'])
def auth_route():
    if request.method == 'OPTIONS':
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    return authenticate_user()

@app.route('/usuarios', methods=['GET'])
def list_users_route():
    return list_users()

@app.route('/usuarios/criar', methods=['POST'])
def create_user_route():
    return create_user()

@app.route('/usuarios/editar', methods=['PUT'])
def edit_user_route():
    return edit_user()

@app.route('/usuarios/excluir', methods=['DELETE'])
def delete_user_route():
    return delete_user()

@app.route('/usuarios/viagens', methods=['POST'])
def list_user_trips_route():
    return list_user_trips()

# Rotas de Viagem
@app.route('/viagens', methods=['GET'])
def list_trips_route():
    return list_trips()

@app.route('/viagens/criar', methods=['POST'])
def create_trip_route():
    return create_trip()

@app.route('/viagens/editar', methods=['PUT'])
def edit_trip_route():
    return edit_trip()

@app.route('/viagens/excluir', methods=['DELETE'])
def delete_trip_route():
    return delete_trip()

@app.route('/viagens/<int:trip_id>', methods=['GET'])
def get_trip_by_id_route(trip_id):
    return get_trip_by_id(trip_id)

if __name__ == '__main__':
    app.run(debug=True)