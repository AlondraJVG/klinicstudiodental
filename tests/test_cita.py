from app.models.Citas import Cita
from app import db
from datetime import datetime

def test_create_cita(app):
    cita = Cita(
        fecha_hora=datetime(2025, 5, 20, 10, 0),
        paciente_id=1,
        tratamiento_id=1,
        motivo="Control",
        notas="Seguimiento de ortodoncia",
        estado="Programada"
    )
    db.session.add(cita)
    db.session.commit()

    assert cita.id is not None
    assert cita.paciente_id == 1
    assert cita.tratamiento_id == 1
    assert cita.motivo == "Control"
