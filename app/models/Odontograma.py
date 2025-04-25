from app import db
from datetime import datetime
class Odontograma(db.Model):
    __tablename__ = 'odontograma'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, paciente_id, fecha_creacion=None):
        self.paciente_id = paciente_id
        self.fecha_creacion = fecha_creacion or datetime.utcnow()