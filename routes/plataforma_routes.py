from flask import Blueprint, request, jsonify
from services.plataforma_service import PlataformaService
from utils.decorators import token_requerido

plataforma_bp = Blueprint('plataforma_bp', __name__)

@plataforma_bp.route('/plataformas', methods=['GET'])
def get_plataformas():
    return jsonify(PlataformaService.obtener_plataformas()), 200

@plataforma_bp.route('/plataformas', methods=['POST'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def post_plataforma():
    datos = request.get_json()
    respuesta, status = PlataformaService.crear_plataforma(datos)
    return jsonify(respuesta), status

@plataforma_bp.route('/plataformas/<int:id>', methods=['PUT'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def update_plataforma(id):
    datos = request.get_json()
    respuesta, status = PlataformaService.actualizar_plataforma(id, datos)
    return jsonify(respuesta), status

@plataforma_bp.route('/plataformas/<int:id>', methods=['DELETE'])
@token_requerido(roles_permitidos=['admin'])
def delete_plataforma(id):
    respuesta, status = PlataformaService.eliminar_plataforma(id)
    return jsonify(respuesta), status