import sys
import os

# Ruta a la carpeta de tu aplicación Flask
sys.path.insert(0, '/home/Klinical/klinicstudiodental')

# Si usas un entorno virtual, actívalo
venv_path = '/home/Klinical/klinicstudiodental/venv/bin/activate_this.py'
if os.path.exists(venv_path):
    exec(open(venv_path).read(), {'__file__': venv_path})

# Importa la aplicación Flask desde app.py
from app import app as application
