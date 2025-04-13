from app import db
from sqlalchemy import Date

class Paciente(db.Model):
    __tablename__ = 'Pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100) , nullable=False)
    apellido = db.Column(db.String(100) , nullable=False)
    fecha_nacimiento = db.Column(Date, nullable=False)
    correo = db.Column(db.String(100), nullable=False) 
    telefono = db.Column(db.String(20), nullable=False) 