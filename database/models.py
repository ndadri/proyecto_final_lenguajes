# En este archivo definimos los modelos de datos para la aplicación, 
# utilizando SQLAlchemy para mapear las tablas de la base de datos a clases de Python.

from database.db import db
from datetime import datetime

# 1. USUARIOS
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='cliente')
    
    ventas = db.relationship('Venta', backref='cliente', lazy=True)
    resenas = db.relationship('Resena', backref='autor', lazy=True)

# 2. CATEGORÍAS
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
    juegos = db.relationship('Videojuego', backref='categoria', lazy=True)

# 3. PLATAFORMAS
class Plataforma(db.Model):
    __tablename__ = 'plataformas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
    juegos = db.relationship('Videojuego', backref='plataforma', lazy=True)

# 4. SERVICIOS 
class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    
    detalles_venta = db.relationship('DetalleVentaServicio', backref='servicio', lazy=True)

# 5. VIDEOJUEGOS
class Videojuego(db.Model):
    __tablename__ = 'videojuegos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    
    # Llaves foráneas para relacionar el juego con su categoría y plataforma
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=True)
    plataforma_id = db.Column(db.Integer, db.ForeignKey('plataformas.id'), nullable=True)
    
    detalles_venta = db.relationship('DetalleVentaJuego', backref='videojuego', lazy=True)
    resenas = db.relationship('Resena', backref='videojuego', lazy=True)

# 6. RESEÑAS
class Resena(db.Model):
    __tablename__ = 'resenas'
    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Integer, nullable=False) # Ej: 1 al 5
    comentario = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    videojuego_id = db.Column(db.Integer, db.ForeignKey('videojuegos.id'), nullable=False)

# 7. VENTAS (Cabecera de la factura)
class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False, default=0.0)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    detalles_juegos = db.relationship('DetalleVentaJuego', backref='venta', lazy=True, cascade="all, delete-orphan")
    detalles_servicios = db.relationship('DetalleVentaServicio', backref='venta', lazy=True, cascade="all, delete-orphan")

# 8. DETALLES DE VENTA - JUEGOS
class DetalleVentaJuego(db.Model):
    __tablename__ = 'detalles_venta_juegos'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    videojuego_id = db.Column(db.Integer, db.ForeignKey('videojuegos.id'), nullable=False)

# 9. DETALLES DE VENTA - SERVICIOS
class DetalleVentaServicio(db.Model):
    __tablename__ = 'detalles_venta_servicios'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)