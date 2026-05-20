from flask import Blueprint, request, jsonify
from services.resena_service import ResenaService
from utils.decorators import token_requerido

resena_bp = Blueprint('resena_bp', __name__)

# PÚBLICA: Ver las reseñas de un juego en específico
@resena_bp.route('/juegos/<int:juego_id>/resenas', methods=['GET'])
def get_resenas(juego_id):
    lista = ResenaService.obtener_resenas_juego(juego_id)
    return jsonify(lista), 200

# PROTEGIDA: Crear una reseña (Sacamos el ID de usuario del token oculto)
@resena_bp.route('/resenas', methods=['POST'])
@token_requerido(roles_permitidos=['cliente', 'admin', 'vendedor'])
def post_resena():
    datos = request.get_json()
    usuario_id = request.usuario_actual['usuario_id']
    respuesta, status = ResenaService.crear_resena(usuario_id, datos)
    return jsonify(respuesta), status

# PROTEGIDA: Eliminar una reseña
@resena_bp.route('/resenas/<int:id>', methods=['DELETE'])
@token_requerido() # Si lo dejamos vacío, deja pasar a cualquiera logueado. El servicio decide si lo deja borrar.
def delete_resena(id):
    usuario_actual = request.usuario_actual
    respuesta, status = ResenaService.eliminar_resena(id, usuario_actual)
    return jsonify(respuesta), status