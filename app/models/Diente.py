from app import db

class Diente(db.Model):
    __tablename__ = 'dientes'

    id = db.Column(db.Integer, primary_key=True)
    numero_diente = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Diente {self.numero_diente} - {self.ubicacion}>'
