from app import db

class Cita(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    tratamiento_id = db.Column(db.Integer, db.ForeignKey('tratamientos.id'))

    paciente = db.relationship('Paciente', backref='citas')
    tratamiento = db.relationship('Tratamiento', backref='citas')
