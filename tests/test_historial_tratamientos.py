from app.models.Historial_Tratamientos import HistorialTratamientos
from app import db
from datetime import date 

def test_create_historial_tratamiento(app):
    historial = HistorialTratamientos(
        paciente_id=1,
        cita_id=1,
        tratamiento_id=1,
        fecha=date(2025, 5, 14),
        observaciones="Tratamiento exitoso"
    )
    db.session.add(historial)
    db.session.commit()

    assert historial.id is not None
    assert historial.cita_id == 1
