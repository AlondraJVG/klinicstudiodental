from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
CORS(app)


app = Flask(__name__)

# Conexión a MySQL en PythonAnywhere
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Klinical:chocoLATE.21@Klinical.mysql.pythonanywhere-services.com/Klinical$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

# Ruta principal de login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data['correo']
    contrasena = data['contrasena']
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and check_password_hash(usuario.contrasena, contrasena):
        return jsonify({'mensaje': 'Login exitoso', 'usuario': usuario.nombre}), 200
    elif usuario:
        return jsonify({'mensaje': 'Contraseña incorrecta'}), 401
    else:
        return jsonify({'mensaje': 'Correo no encontrado'}), 404


# Ruta para crear un nuevo usuario (para demostración)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data['nombre']
    apellidos = data['apellidos']
    correo = data['correo']
    contrasena = generate_password_hash(data['contrasena'])

    nuevo_usuario = Usuario(
        nombre=nombre,
        apellidos=apellidos,
        correo=correo,
        contrasena=contrasena
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado con éxito'}), 201


if __name__ == '__main__':
    app.run(debug=True)