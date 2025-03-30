# app/models/paciente.py

from datetime import datetime
from app import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    correo = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con Cita (si es necesario)
    citas = db.relationship('Cita', backref='paciente', lazy=True)

    # Relación con Tratamiento (si es necesario)
    tratamientos = db.relationship('Tratamiento', backref='paciente', lazy=True)
    
    def __repr__(self):
        return f'<Paciente {self.nombre}>'
