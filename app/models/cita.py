# app/models/cita.py

from datetime import datetime
from app import db

class Cita(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    motivo = db.Column(db.String(255))
    
    # Relación con Paciente
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)

    def __repr__(self):
        return f'<Cita {self.motivo} para {self.paciente_id}>'
