# services/usuario_service.py
import jwt
import datetime
from flask import current_app
from repositories.usuario_repository import UsuarioRepository
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioService:
    @staticmethod
    def registrar_usuario(datos):
        if UsuarioRepository.obtener_por_correo(datos['correo']):
            return {"error": "Este correo ya está registrado"}, 400
        
        password_hash = generate_password_hash(datos['password'])
        rol = datos.get('rol', 'cliente')
        
        nuevo_usuario = UsuarioRepository.crear(
            nombre=datos['nombre'],
            correo=datos['correo'],
            password_hash=password_hash,
            rol=rol
        )
        return {"mensaje": f"¡Éxito! Usuario {nuevo_usuario.nombre} creado como {nuevo_usuario.rol}"}, 201

    @staticmethod
    def login_usuario(datos):
        correo = datos.get('correo')
        password = datos.get('password')

        # 1. Buscar al usuario en la BD
        usuario = UsuarioRepository.obtener_por_correo(correo)

        # 2. Verificar que exista y que la contraseña encriptada coincida
        if not usuario or not check_password_hash(usuario.password, password):
            return {"error": "Correo o contraseña incorrectos"}, 401

        # 3. Si todo está bien, armamos el Token (payload)
        payload = {
            'usuario_id': usuario.id,
            'rol': usuario.rol,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2) # El token expira en 2 horas
        }
        
        # 4. Generamos el token firmado con nuestra clave secreta
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

        return {
            "mensaje": "Login exitoso",
            "token": token,
            "usuario": {
                "nombre": usuario.nombre,
                "rol": usuario.rol
            }
        }, 200
    
    @staticmethod
    def obtener_usuarios():
        usuarios = UsuarioRepository.obtener_todos()
        # No devolvemos la contraseña por seguridad
        return [
            {
                "id": u.id, 
                "nombre": u.nombre, 
                "correo": u.correo, 
                "rol": u.rol
            } for u in usuarios
        ]

    @staticmethod
    def actualizar_usuario(id, datos):
        usuario = UsuarioRepository.obtener_por_id(id)
        if not usuario:
            return {"error": "Usuario no encontrado"}, 404
            
        UsuarioRepository.actualizar(usuario, datos.get('nombre'), datos.get('rol'))
        return {"mensaje": "Usuario actualizado con éxito"}, 200

    @staticmethod
    def eliminar_usuario(id):
        usuario = UsuarioRepository.obtener_por_id(id)
        if not usuario:
            return {"error": "Usuario no encontrado"}, 404
            
        UsuarioRepository.eliminar(usuario)
        return {"mensaje": "Usuario eliminado permanentemente"}, 200