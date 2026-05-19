import os
import urllib
from flask import Flask
from dotenv import load_dotenv
from database.db import db
from routes.usuario_routes import usuario_bp
# Llamamos a los modelos para que SQLAlchemy los reconozca y pueda crear las tablas
from database.models import Usuario, Videojuego
# Cargar variables del .env
load_dotenv()

app = Flask(__name__)

# Extraer variables (ya no pedimos user ni password)
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
driver = os.getenv('DB_DRIVER')

# Armar la cadena de conexión para Autenticación de Windows
params = urllib.parse.quote_plus(
    f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)

# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Clave secreta para sesiones (puede ser cualquier cadena, pero es mejor tenerla en el .env)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave_respaldo_por_si_acaso')

# Inicializar la base de datos con la app
db.init_app(app)

# Registrar los blueprints de rutas
app.register_blueprint(usuario_bp, url_prefix='/api')

with app.app_context():
    db.create_all()
    print("Conexión exitosa con Autenticación de Windows. ¡El back está vivo!")

# --- RUTAS DE PRUEBA ---
@app.route('/')
def home():
    return {"mensaje": "¡API de la Gaming Store funcionando al 100%!"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)