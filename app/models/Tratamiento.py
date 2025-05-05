from app import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamientos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)

    def __repr__(self):
        return f'<Tratamiento {self.nombre}>'
