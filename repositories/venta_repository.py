# repositories/venta_repository.py
from database.models import Venta, DetalleVentaJuego, Videojuego
from database.db import db

class VentaRepository:
    @staticmethod
    def registrar_compra(usuario_id, carrito):
        # 1. Calcular el total a pagar
        total = sum(item['cantidad'] * item['precio_unitario'] for item in carrito)
        
        # 2. Crear la factura (Venta)
        nueva_venta = Venta(usuario_id=usuario_id, total=total)
        db.session.add(nueva_venta)
        db.session.flush() # Guarda temporalmente para generar el ID de la venta
        
        # 3. Crear los detalles y descontar stock
        for item in carrito:
            detalle = DetalleVentaJuego(
                venta_id=nueva_venta.id,
                videojuego_id=item['videojuego_id'],
                cantidad=item['cantidad'],
                precio_unitario=item['precio_unitario']
            )
            db.session.add(detalle)
            
            # Descontar el stock en la base de datos
            juego = Videojuego.query.get(item['videojuego_id'])
            juego.stock -= item['cantidad']
            
        db.session.commit()
        return nueva_venta