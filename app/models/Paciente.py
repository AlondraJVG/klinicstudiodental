from app import db

class Paciente(db.Model):
    __tablename__ = 'Pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    tipo_sangre = db.Column(db.String(10), nullable=False)
    correo = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(20), nullable=False)
    contacto_emergencia  = db.Column(db.String(20), nullable=False)
    nombre_contacto = db.Column(db.String(100), nullable=False)

    __table_args__ = (
    db.UniqueConstraint('nombre', 'apellido', 'correo', name='uq_nombre_apellido_correo'),
    )
@validates('nombre', 'apellido', 'correo')
def convertir_minusculas(self, key, value):
    return value.strip().lower()

