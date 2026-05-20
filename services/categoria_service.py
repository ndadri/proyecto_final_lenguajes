from repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    @staticmethod
    def obtener_categorias():
        categorias = CategoriaRepository.obtener_todas()
        return [{"id": c.id, "nombre": c.nombre} for c in categorias]
    
    @staticmethod
    def crear_categoria(datos):
        nueva = CategoriaRepository.crear(nombre=datos['nombre'])
        return {"mensaje": "Categoría creada", "id": nueva.id}, 201

    @staticmethod
    def actualizar_categoria(id, datos):
        categoria = CategoriaRepository.obtener_por_id(id)
        if not categoria:
            return {"error": "Categoría no encontrada"}, 404
        CategoriaRepository.actualizar(categoria, datos.get('nombre'))
        return {"mensaje": "Categoría actualizada"}, 200

    @staticmethod
    def eliminar_categoria(id):
        categoria = CategoriaRepository.obtener_por_id(id)
        if not categoria:
            return {"error": "Categoría no encontrada"}, 404
        CategoriaRepository.eliminar(categoria)
        return {"mensaje": "Categoría eliminada"}, 200