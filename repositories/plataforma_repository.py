from database.models import Plataforma
from database.db import db

class PlataformaRepository:
    @staticmethod
    def obtener_todas():
        return Plataforma.query.all()
    
    @staticmethod
    def obtener_por_id(id):
        return Plataforma.query.get(id)
    
    @staticmethod
    def crear(nombre):
        nueva = Plataforma(nombre=nombre)
        db.session.add(nueva)
        db.session.commit()
        return nueva

    @staticmethod
    def actualizar(plataforma, nombre):
        if nombre: 
            plataforma.nombre = nombre
        db.session.commit()
        return plataforma

    @staticmethod
    def eliminar(plataforma):
        db.session.delete(plataforma)
        db.session.commit()