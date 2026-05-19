# En este archivo configuramos la conexión a la base de datos utilizando SQLAlchemy, 
# y creamos una instancia de la clase SQLAlchemy que se usará para definir los modelos de datos.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()