# app/models/tratamiento.py

from datetime import datetime
from app import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamientos'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime)
    
    # Relación con Paciente
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)

    def __repr__(self):
        return f'<Tratamiento {self.descripcion} para {self.paciente_id}>'
