from flask import Blueprint, request, jsonify
from services.categoria_service import CategoriaService
from utils.decorators import token_requerido

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def get_categorias():
    return jsonify(CategoriaService.obtener_categorias()), 200

@categoria_bp.route('/categorias', methods=['POST'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def post_categoria():
    datos = request.get_json()
    respuesta, status = CategoriaService.crear_categoria(datos)
    return jsonify(respuesta), status

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
@token_requerido(roles_permitidos=['admin', 'vendedor'])
def update_categoria(id):
    datos = request.get_json()
    respuesta, status = CategoriaService.actualizar_categoria(id, datos)
    return jsonify(respuesta), status

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
@token_requerido(roles_permitidos=['admin'])
def delete_categoria(id):
    respuesta, status = CategoriaService.eliminar_categoria(id)
    return jsonify(respuesta), status