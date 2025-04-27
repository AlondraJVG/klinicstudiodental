from app import db

class CondicionesDentales(db.Model):
    __tablename__ = 'condiciones_dentales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)

class Diente(db.Model):
    __tablename__ = 'dientes'
    id = db.Column(db.Integer, primary_key=True)
    numero_diente = db.Column(db.Integer)
    ubicacion = db.Column(db.String(50))
    tipo = db.Column(db.String(50))



