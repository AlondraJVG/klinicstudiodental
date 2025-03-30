# app/models/usuario.py

from datetime import datetime
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(100), unique=True)
    contrasena = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con Paciente (si es necesario)
    pacientes = db.relationship('Paciente', backref='usuario', lazy=True)
    
    def __repr__(self):
        return f'<Usuario {self.nombre}>'
