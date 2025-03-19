from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'  # Reemplaza con tus credenciales
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'  # Cambia por una clave secreta para sesiones

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelo de la tabla usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())

# Ruta para la página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Buscar al usuario en la base de datos
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            # El login es correcto, redirigir a la página principal
            return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta para la página de dashboard (después de iniciar sesión)
@app.route('/dashboard')
def dashboard():
    return '¡Bienvenido al dashboard!'

# Ruta para registrar un nuevo usuario (solo por propósito de eje
