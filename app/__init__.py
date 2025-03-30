# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# Inicialización de las extensiones
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@example.com'
    app.config['MAIL_PASSWORD'] = 'your_email_password'
    
    