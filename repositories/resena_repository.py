from database.models import Resena
from database.db import db

class ResenaRepository:
    @staticmethod
    def obtener_por_juego(videojuego_id):
        # Traemos todas las reseñas asociadas a un ID de juego
        return Resena.query.filter_by(videojuego_id=videojuego_id).all()
    
    @staticmethod
    def obtener_por_id(id):
        return Resena.query.get(id)
    
    @staticmethod
    def crear(calificacion, comentario, usuario_id, videojuego_id):
        nueva = Resena(
            calificacion=calificacion, 
            comentario=comentario, 
            usuario_id=usuario_id,
            videojuego_id=videojuego_id
        )
        db.session.add(nueva)
        db.session.commit()
        return nueva

    @staticmethod
    def eliminar(resena):
        db.session.delete(resena)
        db.session.commit()