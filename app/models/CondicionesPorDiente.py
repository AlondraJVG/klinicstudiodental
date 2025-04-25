from app import db

class CondicionesPorDiente(db.Model):
    __tablename__ = 'Condiciones_por_Diente'

    id = db.Column(db.Integer, primary_key=True)
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('Condiciones_por_Diente.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    # Relación de los modelos
    diente = db.relationship('Diente', backref='Condiciones_por_Diente')
    condicion = db.relationship('CondicionesDentales', backref='Condiciones_por_Diente')

    def __repr__(self):
        return f'<CondicionPorDiente {self.diente.numero_diente} - {self.condicion.nombre}>'
