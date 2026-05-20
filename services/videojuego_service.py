from repositories.videojuego_repository import VideojuegoRepository

class VideojuegoService:
    @staticmethod
    def obtener_juegos():
        juegos = VideojuegoRepository.obtener_todos()
        return [
            {
                "id": j.id, 
                "titulo": j.titulo, 
                "descripcion": j.descripcion, 
                "precio": j.precio, 
                "stock": j.stock
            } for j in juegos
        ]
    
    @staticmethod
    def crear_juego(datos):
        nuevo_juego = VideojuegoRepository.crear(
            titulo=datos['titulo'],
            descripcion=datos.get('descripcion', ''),
            precio=datos['precio'],
            stock=datos.get('stock', 0),
            categoria_id=datos.get('categoria_id'),
            plataforma_id=datos.get('plataforma_id')
        )
        return {"mensaje": "¡Juego agregado a la tienda!", "id": nuevo_juego.id}, 201

    @staticmethod
    def actualizar_juego(id, datos):
        juego = VideojuegoRepository.obtener_por_id(id)
        if not juego:
            return {"error": "Videojuego no encontrado"}, 404
            
        VideojuegoRepository.actualizar(juego, datos)
        return {"mensaje": "Videojuego actualizado correctamente"}, 200

    @staticmethod
    def eliminar_juego(id):
        juego = VideojuegoRepository.obtener_por_id(id)
        if not juego:
            return {"error": "Videojuego no encontrado"}, 404
            
        VideojuegoRepository.eliminar(juego)
        return {"mensaje": "Videojuego eliminado del catálogo"}, 200