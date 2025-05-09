from app import db
from app.models.Paciente import Paciente
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Cita(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    tratamiento_id = db.Column(db.Integer, db.ForeignKey('tratamientos.id'), nullable=True)
    fecha_hora = db.Column(DateTime(timezone=True), nullable=False)  
    motivo = db.Column(db.String(255))
    notas = db.Column(db.String(255))
    estado = db.Column(db.String(50))

    paciente = db.relationship('Paciente', backref='citas')
    tratamiento = db.relationship('Tratamiento', backref='citas')
