from flask import Blueprint, request, jsonify
from services.servicio_service import ServicioService
from utils.decorators import token_requerido

servicio_bp = Blueprint('servicio_bp', __name__)

@servicio_bp.route('/servicios', methods=['GET'])
def get_servicios():
    lista = ServicioService.obtener_servicios()
    return jsonify(lista), 200

@servicio_bp.route('/servicios', methods=['POST'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def post_servicio():
    datos = request.get_json()
    respuesta, status_code = ServicioService.crear_servicio(datos)
    return jsonify(respuesta), status_code

@servicio_bp.route('/servicios/<int:id>', methods=['PUT'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def update_servicio(id):
    datos = request.get_json()
    respuesta, status_code = ServicioService.actualizar_servicio(id, datos)
    return jsonify(respuesta), status_code

@servicio_bp.route('/servicios/<int:id>', methods=['DELETE'])
@token_requerido(roles_permitidos=['admin'])
def delete_servicio(id):
    respuesta, status_code = ServicioService.eliminar_servicio(id)
    return jsonify(respuesta), status_code