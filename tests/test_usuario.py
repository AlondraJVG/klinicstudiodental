from app.models.usuario import Usuario
from app import db

def test_create_usuario(app):
    usuario = Usuario(
        nombre="Admin", 
        apellidos="Smith", 
        correo="admin@klinical.com", 
        contrasena="admin123"
    )
    db.session.add(usuario)
    db.session.commit()

    assert usuario.id is not None
    assert usuario.nombre == "Admin"