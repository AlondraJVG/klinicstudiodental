from app.models.Paciente import Paciente
from app import db
from datetime import date

from app.models.Paciente import Paciente
from app import db
from datetime import date

def test_create_paciente(app):
    with app.app_context():
        paciente = Paciente(
            nombre="Juan",
            apellido="Pérez",
            fecha_nacimiento=date(1993, 1, 1),
            edad=30,
            sexo="Masculino",
            tipo_sangre="O+",
            correo="juan.perez@gmail.com",
            telefono="1234567890",
            contacto_emergencia="0987654321",
            nombre_contacto="Maria Pérez"
        )
        db.session.add(paciente)
        db.session.commit()

        assert paciente.id is not None
        assert paciente.nombre == "Juan"
        assert paciente.apellido == "Pérez"
