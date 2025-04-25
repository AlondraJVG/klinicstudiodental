from app import db

class CondicionesDentales(db.Model):
    __tablename__ = 'condiciones_dentales'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<CondicionDental {self.nombre}>'

    