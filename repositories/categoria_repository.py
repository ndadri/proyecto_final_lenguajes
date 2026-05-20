from database.models import Categoria
from database.db import db

class CategoriaRepository:
    @staticmethod
    def obtener_todas():
        return Categoria.query.all()
    
    @staticmethod
    def obtener_por_id(id):
        return Categoria.query.get(id)
    
    @staticmethod
    def crear(nombre):
        nueva = Categoria(nombre=nombre)
        db.session.add(nueva)
        db.session.commit()
        return nueva

    @staticmethod
    def actualizar(categoria, nombre):
        if nombre: 
            categoria.nombre = nombre
        db.session.commit()
        return categoria

    @staticmethod
    def eliminar(categoria):
        db.session.delete(categoria)
        db.session.commit()