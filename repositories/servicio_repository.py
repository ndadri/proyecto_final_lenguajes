from database.models import Servicio
from database.db import db

class ServicioRepository:
    @staticmethod
    def obtener_todos():
        return Servicio.query.all()
    
    @staticmethod
    def obtener_por_id(id):
        return Servicio.query.get(id)
    
    @staticmethod
    def crear(nombre, descripcion, precio):
        nuevo_servicio = Servicio(
            nombre=nombre, 
            descripcion=descripcion, 
            precio=precio
        )
        db.session.add(nuevo_servicio)
        db.session.commit()
        return nuevo_servicio

    @staticmethod
    def actualizar(servicio, datos):
        if 'nombre' in datos: servicio.nombre = datos['nombre']
        if 'descripcion' in datos: servicio.descripcion = datos['descripcion']
        if 'precio' in datos: servicio.precio = datos['precio']
        db.session.commit()
        return servicio

    @staticmethod
    def eliminar(servicio):
        db.session.delete(servicio)
        db.session.commit()