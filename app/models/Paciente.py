from app import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    tipo_sangre = db.Column(db.String(10), nullable=False)
    alergias = db.Column(db.Text, nullable=True)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    contacto_emergencia  = db.Column(db.String(20), nullable=False)
    nombre_contacto = db.Column(db.String(100), nullable=False)
    
