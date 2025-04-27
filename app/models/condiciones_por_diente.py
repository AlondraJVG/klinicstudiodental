from app import db
from app.models.Diente import Diente  # Importa la clase Diente correctamente
from app.models.CondicionesDentales import CondicionesDentales  # Si lo necesitas

class CondicionesPorDiente(db.Model):
    __tablename__ = 'condiciones_por_diente'
    id = db.Column(db.Integer, primary_key=True)
    diente_id = db.Column(db.Integer, db.ForeignKey('dientes.id'))  # Referencia correcta a la tabla dientes
    condicion_id = db.Column(db.Integer, db.ForeignKey('condiciones_dentales.id'))
    descripcion = db.Column(db.String(255))

    # Relación con la clase Diente
    diente = db.relationship('Diente', backref='condiciones')
    # Si tienes una relación con CondicionesDentales
    condicion = db.relationship('CondicionesDentales', backref='condiciones_por_diente')
