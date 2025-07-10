# from flask import Flask, jsonify
# from flask_cors import CORS

# # Import das rotas de usuário
# from users.auth import authenticate_user
# from users.create import create_user
# from users.delete import delete_user
# from users.edit import edit_user
# from users.list import list_users
# from users.trips import list_user_trips

# # Import das rotas de viagem
# from trips.create import create_trip
# from trips.delete import delete_trip
# from trips.edit import edit_trip
# from trips.get_by_id import get_trip_by_id
# from trips.list import list_trips
# from trips.purchase_seat import purchase_seat

# app = Flask(__name__)
# CORS(app, resources={
#     r"/*": {
#         "origins": ["http://localhost:3000", "http://localhost:5173"],
#         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#         "allow_headers": ["Content-Type", "Authorization"],
#         "supports_credentials": True,
#         "expose_headers": ["Content-Type"]
#     }
# })


# # Rotas de Usuário
# @app.route('/autenticar', methods=['POST'])
# def auth_route():
#     return authenticate_user()

# @app.route('/usuarios', methods=['GET'])
# def list_users_route():
#     return list_users()

# @app.route('/usuarios/criar', methods=['POST'])
# def create_user_route():
#     return create_user()

# @app.route('/usuarios/editar', methods=['PUT'])
# def edit_user_route():
#     return edit_user()

# @app.route('/usuarios/excluir', methods=['DELETE'])
# def delete_user_route():
#     return delete_user()

# @app.route('/usuarios/viagens', methods=['POST'])
# def list_user_trips_route():
#     return list_user_trips()



# # Rotas de Viagem
# @app.route('/viagens', methods=['GET'])
# def list_trips_route():
#     return list_trips()

# @app.route('/viagens/criar', methods=['POST'])
# def create_trip_route():
#     return create_trip()

# @app.route('/viagens/editar', methods=['PUT'])
# def edit_trip_route():
#     return edit_trip()

# @app.route('/viagens/excluir', methods=['DELETE'])
# def delete_trip_route():
#     return delete_trip()

# @app.route('/viagens/<int:trip_id>', methods=['GET'])
# def get_trip_by_id_route(trip_id):
#     return get_trip_by_id(trip_id)

# @app.route('/viagens/comprar-assento', methods=['PUT'])
# def purchase_seat_route():
#     return purchase_seat()

# if __name__ == '__main__':
#     app.run(debug=True)






# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.user_controller import UserController
from controllers.trip_controller import TripController

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "http://localhost:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True,
        "expose_headers": ["Content-Type"]
    }
})

# Rotas de Usuário
@app.route('/autenticar', methods=['POST'])
def auth_route():
    return UserController.authenticate()

@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_user_by_id_route(user_id):
    return UserController.get_by_id(user_id)

@app.route('/usuarios', methods=['GET'])
def list_users_route():
    return UserController.list()

@app.route('/usuarios/criar', methods=['POST'])
def create_user_route():
    return UserController.create()

@app.route('/usuarios/editar', methods=['PUT'])
def edit_user_route():
    return UserController.update()

@app.route('/usuarios/excluir', methods=['DELETE'])
def delete_user_route():
    return UserController.delete()

# Rotas de Viagem
@app.route('/viagens', methods=['GET'])
def list_trips_route():
    return TripController.list()

@app.route('/viagens/criar', methods=['POST'])
def create_trip_route():
    return TripController.create()

@app.route('/viagens/editar', methods=['PUT'])
def edit_trip_route():
    return TripController.update()

@app.route('/viagens/excluir', methods=['DELETE'])
def delete_trip_route():
    return TripController.delete()

@app.route('/viagens/<int:trip_id>', methods=['GET'])
def get_trip_by_id_route(trip_id):
    return TripController.get_by_id(trip_id)

@app.route('/viagens/comprar-assento', methods=['PUT'])
def purchase_seat_route():
    return TripController.purchase_seat()

@app.route('/usuarios/viagens', methods=['POST'])
def list_user_trips_route():
    return TripController.list_user_trips()

if __name__ == '__main__':
    app.run(debug=True)