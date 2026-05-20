# routes/venta_routes.py
from flask import Blueprint, request, jsonify
from services.venta_service import VentaService
from utils.decorators import token_requerido

venta_bp = Blueprint('venta_bp', __name__)

# PROTEGIDA: Solo Clientes (o Admins haciendo pruebas) pueden comprar
@venta_bp.route('/compras', methods=['POST'])
@token_requerido(roles_permitidos=['cliente', 'admin'])
def realizar_compra():
    datos = request.get_json()
    # Sacamos el ID del usuario directamente del token
    usuario_id = request.usuario_actual['usuario_id'] 
    items = datos.get('items', [])
    
    if not items:
        return jsonify({"error": "El carrito está vacío"}), 400
        
    respuesta, status_code = VentaService.procesar_compra(usuario_id, items)
    return jsonify(respuesta), status_code