from app import db

class CondicionesDentales(db.Model):
    __tablename__ = 'condiciones_dentales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)


