from flask import Blueprint, request, jsonify
from services.videojuego_service import VideojuegoService
from utils.decorators import token_requerido

videojuego_bp = Blueprint('videojuego_bp', __name__)

# PÚBLICA: Todos pueden ver el catálogo (no pide token)
@videojuego_bp.route('/juegos', methods=['GET'])
def get_juegos():
    lista = VideojuegoService.obtener_juegos()
    return jsonify(lista), 200

# PROTEGIDA: Solo Admin y Vendedor pueden agregar
@videojuego_bp.route('/juegos', methods=['POST'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def post_juego():
    datos = request.get_json()
    respuesta, status_code = VideojuegoService.crear_juego(datos)
    return jsonify(respuesta), status_code

# PROTEGIDA: Solo Admin y Vendedor pueden actualizar (ej. subir o bajar stock)
@videojuego_bp.route('/juegos/<int:id>', methods=['PUT'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def update_juego(id):
    datos = request.get_json()
    respuesta, status_code = VideojuegoService.actualizar_juego(id, datos)
    return jsonify(respuesta), status_code

# MUY PROTEGIDA: SOLO el Admin puede eliminar juegos
@videojuego_bp.route('/juegos/<int:id>', methods=['DELETE'])
@token_requerido(roles_permitidos=['admin'])
def delete_juego(id):
    respuesta, status_code = VideojuegoService.eliminar_juego(id)
    return jsonify(respuesta), status_code