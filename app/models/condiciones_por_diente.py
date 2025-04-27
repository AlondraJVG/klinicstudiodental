from app import db


class CondicionesPorDiente(db.Model):
    __tablename__ = 'condiciones_por_diente'
    id = db.Column(db.Integer, primary_key=True)
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'))
    condicion = db.Column(db.String(255))

    diente = db.relationship('Diente', backref='condiciones')