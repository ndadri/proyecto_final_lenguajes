# services/venta_service.py
from repositories.venta_repository import VentaRepository
from repositories.videojuego_repository import VideojuegoRepository

class VentaService:
    @staticmethod
    def procesar_compra(usuario_id, items):
        carrito = []
        
        # Validar cada item que el cliente quiere comprar
        for item in items:
            juego = VideojuegoRepository.obtener_por_id(item['videojuego_id'])
            
            if not juego:
                return {"error": f"El juego con ID {item['videojuego_id']} no existe en el catálogo"}, 404
                
            if juego.stock < item['cantidad']:
                return {"error": f"Stock insuficiente para {juego.titulo}. Solo nos quedan {juego.stock} unidades"}, 400
            
            # Si todo está bien, lo preparamos para el repositorio
            carrito.append({
                'videojuego_id': juego.id,
                'cantidad': item['cantidad'],
                'precio_unitario': juego.precio # Tomamos el precio real de la BD, no del cliente
            })
            
        # Enviar al repositorio para guardar en base de datos
        nueva_venta = VentaRepository.registrar_compra(usuario_id, carrito)
        
        return {
            "mensaje": "¡Compra realizada con éxito!", 
            "venta_id": nueva_venta.id, 
            "total_pagado": round(nueva_venta.total, 2)
        }, 201