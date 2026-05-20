from repositories.resena_repository import ResenaRepository
from repositories.videojuego_repository import VideojuegoRepository

class ResenaService:
    @staticmethod
    def obtener_resenas_juego(videojuego_id):
        resenas = ResenaRepository.obtener_por_juego(videojuego_id)
        return [
            {
                "id": r.id, 
                "calificacion": r.calificacion, 
                "comentario": r.comentario, 
                "fecha": r.fecha.strftime("%Y-%m-%d"),
                "usuario": r.autor.nombre # Usamos la relación del modelo para sacar el nombre
            } for r in resenas
        ]
    
    @staticmethod
    def crear_resena(usuario_id, datos):
        # 1. Validar que el juego exista
        juego = VideojuegoRepository.obtener_por_id(datos.get('videojuego_id'))
        if not juego:
            return {"error": "El videojuego no existe"}, 404
            
        # 2. Validar estrellas
        calificacion = datos.get('calificacion', 5)
        if calificacion < 1 or calificacion > 5:
            return {"error": "La calificación debe estar entre 1 y 5 estrellas"}, 400

        nueva = ResenaRepository.crear(
            calificacion=calificacion,
            comentario=datos.get('comentario', ''),
            usuario_id=usuario_id,
            videojuego_id=juego.id
        )
        return {"mensaje": "¡Reseña publicada con éxito!", "id": nueva.id}, 201

    @staticmethod
    def eliminar_resena(id, usuario_actual):
        resena = ResenaRepository.obtener_por_id(id)
        if not resena:
            return {"error": "Reseña no encontrada"}, 404
            
        # Seguridad: Solo el dueño de la reseña o un Admin pueden borrarla
        es_admin = usuario_actual['rol'] == 'admin'
        es_dueno = resena.usuario_id == usuario_actual['usuario_id']
        
        if not (es_admin or es_dueno):
            return {"error": "No tienes permisos para borrar esta reseña"}, 403
            
        ResenaRepository.eliminar(resena)
        return {"mensaje": "Reseña eliminada correctamente"}, 200