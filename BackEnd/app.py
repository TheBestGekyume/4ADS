from flask import Flask
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
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Rotas de Usuário
@app.route('/autenticar', methods=['POST', 'OPTIONS'])
def auth_route():
    if request.method == 'OPTIONS':
        return '', 200
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