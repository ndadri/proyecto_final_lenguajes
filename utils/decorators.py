# utils/decorators.py
from functools import wraps
from flask import request, jsonify, current_app
import jwt

def token_requerido(roles_permitidos=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            
            # 1. Buscar el token en los Headers de la petición
            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']
                # El formato estándar es "Bearer el_super_token_largo"
                if auth_header.startswith('Bearer '):
                    token = auth_header.split(" ")[1]
            
            if not token:
                return {"error": "Falta el token de acceso. ¡Inicia sesión!"}, 401
            
            try:
                # 2. Desencriptar el token con nuestra llave secreta
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
                
                # 3. Verificar si el usuario tiene el rol necesario
                if roles_permitidos and data['rol'] not in roles_permitidos:
                    return {"error": f"Acceso denegado. Tu rol es '{data['rol']}' y necesitas ser {roles_permitidos}"}, 403
                    
            except jwt.ExpiredSignatureError:
                return {"error": "El token ha expirado. Vuelve a iniciar sesión"}, 401
            except jwt.InvalidTokenError:
                return {"error": "Token inválido o corrupto"}, 401
                
            # Si todo está bien, lo dejamos pasar a la ruta original
            return f(*args, **kwargs)
        return decorated
    return decorator