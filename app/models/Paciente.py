from app import db

class Paciente(db.Model):
    __tablename__ = 'Pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100) , nullable=False)
    apellido = db.Column(db.varchar(100) , nullable=False)
    fecha_nacimiento = db.Column(db.date , nullable=False)
    correo = db.Column(db.varchar(100) , nullable=False)
    telefono = db.Column(db.varchar(20) , nullable=False)