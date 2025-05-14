# Instalación

```bash
## 1 Clonar el repositorio:

git clone https://github.com/AlondraJVG/klinicstudiodental.git
cd klinicstudiodental

## 2 Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## 3 Instalar las dependencias:

pip install -r requirements.txt

## 4 Configurar las variables de entorno copiando el archivo de ejemplo:

cp .env.example .env

## 5 Ejecutar la aplicación:

flask run
``` 
# Despliegue en Producción

1- Subir el proyecto a un servidor (ej: PythonAnywhere).
2- Instalar dependencias como en el entorno local.
3- Configurar variables de entorno en el servidor.
4- Ejecutar el servidor WSGI (ej: gunicorn).
