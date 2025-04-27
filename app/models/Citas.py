from app import db

class Cita(db.Model):
    __tablename__ = 'citas'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    tratamiento_id = db.Column(db.Integer, db.ForeignKey('tratamientos.id'), nullable=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    notas = db.Column(db.Text)
    estado = db.Column(db.String(50), default="Programada")
    
    paciente = db.relationship('Paciente', backref=db.backref('citas', lazy=True))
    tratamiento = db.relationship('Tratamiento', backref=db.backref('citas', lazy=True))