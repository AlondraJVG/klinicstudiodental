from app import db
from datetime import datetime

class Odontograma(db.Model):
    __tablename__ = 'odontogramas'  

    id = db.Column(db.Integer, primary_key=True)
    pacientes_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    fecha_creacion = db.Column(db.Date, default=datetime.utcnow)

    paciente = db.relationship('Paciente', backref=db.backref('odontogramas', lazy=True))
