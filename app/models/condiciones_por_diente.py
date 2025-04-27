# app/models/condiciones_por_diente.py
from app import db
from app.models.Diente import Diente
from app.models.CondicionesDentales import CondicionesDentales

class CondicionesPorDiente(db.Model):
    __tablename__ = 'condiciones_por_diente'
    id = db.Column(db.Integer, primary_key=True)
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'))
    condicion_id = db.Column(db.Integer, db.ForeignKey('condiciones_dentales.id'))  # Corregido para referencia correcta
    descripcion = db.Column(db.String(255))  # Asegúrate de que este campo esté definido correctamente

    # Relaciones
    diente = db.relationship('Diente', backref='condiciones')
    condicion = db.relationship('CondicionesDentales', backref='condiciones_por_diente')
