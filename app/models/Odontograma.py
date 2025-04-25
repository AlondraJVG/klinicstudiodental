from app import db
class Odontograma(db.Model):
    __tablename__ = 'odontograma'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    fecha_creacion = db.Column(db.DateTime)