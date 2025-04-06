from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)

# Configuración
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Klinical:chocoLATE.21@Klinical.mysql.pythonanywhere-services.com/Klinical$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Habilita CORS

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and check_password_hash(usuario.contrasena, contrasena):
        return jsonify({'message': 'Login exitoso', 'usuario': usuario.nombre})
    return jsonify({'message': 'Correo o contraseña incorrectos'}), 400

if __name__ == '__main__':
    app.run(debug=True)
