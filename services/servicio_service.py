from repositories.servicio_repository import ServicioRepository

class ServicioService:
    @staticmethod
    def obtener_servicios():
        servicios = ServicioRepository.obtener_todos()
        return [
            {
                "id": s.id, 
                "nombre": s.nombre, 
                "descripcion": s.descripcion, 
                "precio": s.precio
            } for s in servicios
        ]
    
    @staticmethod
    def crear_servicio(datos):
        nuevo_servicio = ServicioRepository.crear(
            nombre=datos['nombre'],
            descripcion=datos.get('descripcion', ''),
            precio=datos['precio']
        )
        return {"mensaje": "¡Servicio agregado al catálogo!", "id": nuevo_servicio.id}, 201

    @staticmethod
    def actualizar_servicio(id, datos):
        servicio = ServicioRepository.obtener_por_id(id)
        if not servicio:
            return {"error": "Servicio no encontrado"}, 404
            
        ServicioRepository.actualizar(servicio, datos)
        return {"mensaje": "Servicio actualizado correctamente"}, 200

    @staticmethod
    def eliminar_servicio(id):
        servicio = ServicioRepository.obtener_por_id(id)
        if not servicio:
            return {"error": "Servicio no encontrado"}, 404
            
        ServicioRepository.eliminar(servicio)
        return {"mensaje": "Servicio eliminado del catálogo"}, 200