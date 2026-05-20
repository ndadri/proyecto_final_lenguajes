from database.models import Videojuego
from database.db import db

class VideojuegoRepository:
    @staticmethod
    def obtener_todos():
        return Videojuego.query.all()
    
    @staticmethod
    def obtener_por_id(id):
        return Videojuego.query.get(id)
    
    @staticmethod
    def crear(titulo, descripcion, precio, stock, categoria_id=None, plataforma_id=None):
        nuevo_juego = Videojuego(
            titulo=titulo, 
            descripcion=descripcion, 
            precio=precio, 
            stock=stock,
            categoria_id=categoria_id,
            plataforma_id=plataforma_id
        )
        db.session.add(nuevo_juego)
        db.session.commit()
        return nuevo_juego

    @staticmethod
    def actualizar(juego, datos):
        # Actualizamos solo los campos que vengan en el JSON
        if 'titulo' in datos: juego.titulo = datos['titulo']
        if 'descripcion' in datos: juego.descripcion = datos['descripcion']
        if 'precio' in datos: juego.precio = datos['precio']
        if 'stock' in datos: juego.stock = datos['stock']
        if 'categoria_id' in datos: juego.categoria_id = datos['categoria_id']
        if 'plataforma_id' in datos: juego.plataforma_id = datos['plataforma_id']
        
        db.session.commit()
        return juego

    @staticmethod
    def eliminar(juego):
        db.session.delete(juego)
        db.session.commit()