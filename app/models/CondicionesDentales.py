from app import db

class CondicionesDentales(db.Model):
    __tablename__ = 'condiciones_dentales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)

class Diente(db.Model):
    __tablename__ = 'dientes'
    id = db.Column(db.Integer, primary_key=True)
    numero_diente = db.Column(db.Integer)
    ubicacion = db.Column(db.String(50))
    tipo = db.Column(db.String(50))

class CondicionesPorDiente(db.Model):
    __tablename__ = 'condiciones_por_diente'
    id = db.Column(db.Integer, primary_key=True)
    odontograma_id = db.Column(db.Integer, db.ForeignKey('odontogramas.id'))
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'))
    condicion_id = db.Column(db.Integer, db.ForeignKey('condiciones_dentales.id'))
    fecha_diagnostico = db.Column(db.Date)
    comentarios = db.Column(db.Text)

    # Relaciones
    diente = db.relationship('Diente', backref='condiciones_dentales')
    condicion = db.relationship('CondicionesDentales', backref='condiciones_por_diente')
    odontograma = db.relationship('Odontograma', backref='condiciones_por_diente')
