from app import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamientos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255))