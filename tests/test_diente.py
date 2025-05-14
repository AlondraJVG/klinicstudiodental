from app.models.Diente import Diente
from app import db

def test_create_diente(app):
    diente = Diente(
        numero_diente=11,
        ubicacion="Superior izquierdo",
        tipo="Incisivo"
    )
    db.session.add(diente)
    db.session.commit()

    assert diente.id is not None
    assert diente.numero_diente == 11
