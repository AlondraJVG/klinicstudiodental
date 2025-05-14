from app.models.Tratamiento import Tratamiento
from app import db

def test_create_tratamiento(app):
    tratamiento = Tratamiento(
        nombre="Ortodoncia",
        descripcion="Corrección dental"
    )
    db.session.add(tratamiento)
    db.session.commit()

    assert tratamiento.id is not None
    assert tratamiento.nombre == "Ortodoncia"
