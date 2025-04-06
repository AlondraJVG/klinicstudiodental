from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario:
            print(f"Usuario encontrado: {usuario.nombre}")  
            print(f"Contraseña ingresada: {contrasena}") 
            print(f"Contraseña en la base de datos (hashed): {usuario.contrasena}")  
            
            # Verificar la contraseña usando el hash
            if check_password_hash(usuario.contrasena, contrasena):
                return 'La información es correcta'
            else:
                return 'Contraseña incorrecta'
        else:
            return 'Correo no encontrado'
    
    return render_template('login.html')

# Ruta para crear un nuevo usuario (para demostración)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Hashear la contraseña antes de guardarla
        contrasena_hash = generate_password_hash(contrasena)
        
        # Crear un nuevo usuario con la contraseña hasheada
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellidos=apellidos,
            correo=correo,
            contrasena=contrasena_hash
        )

        db.session.add(nuevo_usuario)
        db.session.commit()
        return 'Usuario creado con éxito'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

#ola