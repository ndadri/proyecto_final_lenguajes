from repositories.plataforma_repository import PlataformaRepository

class PlataformaService:
    @staticmethod
    def obtener_plataformas():
        plataformas = PlataformaRepository.obtener_todas()
        return [{"id": p.id, "nombre": p.nombre} for p in plataformas]
    
    @staticmethod
    def crear_plataforma(datos):
        nueva = PlataformaRepository.crear(nombre=datos['nombre'])
        return {"mensaje": "Plataforma creada", "id": nueva.id}, 201

    @staticmethod
    def actualizar_plataforma(id, datos):
        plataforma = PlataformaRepository.obtener_por_id(id)
        if not plataforma:
            return {"error": "Plataforma no encontrada"}, 404
        PlataformaRepository.actualizar(plataforma, datos.get('nombre'))
        return {"mensaje": "Plataforma actualizada"}, 200

    @staticmethod
    def eliminar_plataforma(id):
        plataforma = PlataformaRepository.obtener_por_id(id)
        if not plataforma:
            return {"error": "Plataforma no encontrada"}, 404
        PlataformaRepository.eliminar(plataforma)
        return {"mensaje": "Plataforma eliminada"}, 200