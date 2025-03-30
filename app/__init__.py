from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Klinical:chocoLATE.21@Klinical.mysql.pythonanywhere-services.com/Klinical$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Aquí puedes importar tus rutas
from app import routes

