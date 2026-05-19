# En este archivo definimos el repositorio para la entidad Usuario, 
# que contiene métodos para interactuar con la base de datos relacionados 
# con los usuarios, como crear un nuevo usuario o buscar un usuario por su correo electrónico.

from database.models import Usuario
from database.db import db

class UsuarioRepository:
    @staticmethod
    def crear(nombre, correo, password_hash, rol):
        nuevo_usuario = Usuario(
            nombre=nombre, 
            correo=correo, 
            password=password_hash, 
            rol=rol
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario
    
    @staticmethod
    def obtener_por_correo(correo):
        return Usuario.query.filter_by(correo=correo).first()
    
    @staticmethod
    def obtener_todos():
        return Usuario.query.all()

    @staticmethod
    def obtener_por_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def actualizar(usuario, nombre, rol):
        if nombre: 
            usuario.nombre = nombre
        if rol: 
            usuario.rol = rol
        db.session.commit()
        return usuario

    @staticmethod
    def eliminar(usuario):
        db.session.delete(usuario)
        db.session.commit()