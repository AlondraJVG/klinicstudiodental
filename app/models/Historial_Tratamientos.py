from app import db
from app.models.Paciente import Paciente
from app.models.Citas import Cita
from app.models.Tratamiento import Tratamiento
from datetime import datetime

class HistorialTratamientos(db.Model):
    __tablename__ = 'historial_tratamientos'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    cita_id = db.Column(db.Integer, db.ForeignKey('citas.id'), nullable=False)
    tratamiento_id = db.Column(db.Integer, db.ForeignKey('tratamientos.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    observaciones = db.Column(db.Text, nullable=True)

    paciente = db.relationship('Paciente', backref='historial_tratamientos')
    cita = db.relationship('Cita', backref='historial_tratamientos')
    tratamiento = db.relationship('Tratamiento', backref='historial_tratamientos')

    def __repr__(self):
        return (f"<HistorialTratamientos(id={self.id}, paciente_id={self.paciente_id}, "
                f"cita_id={self.cita_id}, tratamiento_id={self.tratamiento_id}, "
                f"fecha={self.fecha}, observaciones={self.observaciones})>")
