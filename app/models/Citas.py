# app/models/Citas.py
from app import db
from app.models.Paciente import Paciente



class Cita(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    tratamiento_id = db.Column(db.Integer, db.ForeignKey('tratamientos.id'), nullable=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    motivo = db.Column(db.String(255))
    notas = db.Column(db.String(255))
    estado = db.Column(db.String(50))

    paciente = db.relationship('Pacientes', backref='citas')
    tratamiento = db.relationship('Tratamiento', backref='citas')
