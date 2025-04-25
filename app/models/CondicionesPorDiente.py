from app import db
from datetime import datetime

class CondicionesPorDiente(db.Model):
    __tablename__ = 'Condiciones_por_Diente'

    id = db.Column(db.Integer, primary_key=True)
    odontograma_id = db.Column(db.Integer, db.ForeignKey('Odontogramas.id'), nullable=False)
    diente_id = db.Column(db.Integer, db.ForeignKey('Dientes.id'), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('Condiciones_Dentales.id'), nullable=False)
    fecha_diagnostico = db.Column(db.Date, default=datetime.utcnow)
    comentarios = db.Column(db.String(255))

    odontograma = db.relationship('Odontograma', backref=db.backref('condiciones_dientes', lazy=True))
    diente = db.relationship('Diente')
    condicion = db.relationship('CondicionesDentales')  
