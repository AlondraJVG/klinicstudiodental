from app import db

class CondicionesDentales(db.Model):
    __tablename__ = 'Condiciones_Dentales'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
