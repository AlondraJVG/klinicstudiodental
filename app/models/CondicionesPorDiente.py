from app import db

class CondicionesPorDiente(db.Model):
    __tablename__ = 'condiciones_por_diente'

    id = db.Column(db.Integer, primary_key=True)
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('condiciones_dentales.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    # Relación de los modelos
    diente = db.relationship('Diente', backref='condiciones_por_diente')
    condicion = db.relationship('CondicionesDentales', backref='condiciones_por_diente')

    def __repr__(self):
        return f'<CondicionPorDiente {self.diente.numero_diente} - {self.condicion.nombre}>'
