# Variables para Windows
PYTHON = venv\Scripts\python.exe
PIP = venv\Scripts\pip.exe

# 1. Levantar el servidor con un solo comando
run:
	$(PYTHON) app.py

# 2. Instalar todas las dependencias base del proyecto
install:
	$(PIP) install Flask Flask-SQLAlchemy pyodbc python-dotenv PyJWT flask-cors

# 3. Guardar las dependencias en un archivo (excelente práctica)
freeze:
	$(PIP) freeze > requirements.txt

# 4. Limpiar la basura (archivos caché de Python)
clean:
	FOR /d /r . %d in (__pycache__) DO @IF EXIST "%d" rd /s /q "%d"