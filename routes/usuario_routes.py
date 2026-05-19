# En este archivo definimos las rutas relacionadas con los usuarios, 
# como el registro de nuevos usuarios. Estas rutas reciben las solicitudes HTTP, 
# extraen los datos necesarios, y llaman al servicio correspondiente para 
# procesar la lógica de negocio, devolviendo una respuesta adecuada al cliente.

from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService
from utils.decorators import token_requerido

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios/registro', methods=['POST'])
def registrar():
    datos = request.get_json()
    respuesta, status_code = UsuarioService.registrar_usuario(datos)
    return jsonify(respuesta), status_code

@usuario_bp.route('/usuarios/login', methods=['POST'])
def login():
    datos = request.get_json()
    respuesta, status_code = UsuarioService.login_usuario(datos)
    return jsonify(respuesta), status_code

@usuario_bp.route('/usuarios', methods=['GET'])
@token_requerido(roles_permitidos=['admin'])
def get_usuarios():
    lista = UsuarioService.obtener_usuarios()
    return jsonify(lista), 200

# RUTA PARA ACTUALIZAR UN USUARIO (Solo Admin)
@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
@token_requerido(roles_permitidos=['admin'])
def update_usuario(id):
    datos = request.get_json()
    respuesta, status_code = UsuarioService.actualizar_usuario(id, datos)
    return jsonify(respuesta), status_code

# RUTA PARA ELIMINAR UN USUARIO (Solo Admin)
@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
@token_requerido(roles_permitidos=['admin'])
def delete_usuario(id):
    respuesta, status_code = UsuarioService.eliminar_usuario(id)
    return jsonify(respuesta), status_code