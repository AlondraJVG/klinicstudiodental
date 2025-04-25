from app import db

class Diente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_diente = db.Column(db.Integer)
    ubicacion = db.Column(db.String(50))
    tipo = db.Column(db.String(50))