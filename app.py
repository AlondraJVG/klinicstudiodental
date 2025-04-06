from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Conexión a MySQL en PythonAnywhere
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Klinical:chocoLATE.21@Klinical.mysql.pythonanywhere-services.com/Klinical$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(100), unique=True)
    contrasena = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime)

# Ruta principal de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario:
            print(f"Usuario encontrado: {usuario.nombre}")  # Verificamos si el usuario está en la base de datos
            if check_password_hash(usuario.contrasena, contrasena):
                return 'La información es correcta'
            else:
                return 'Contraseña incorrecta'
        else:
            return 'Correo no encontrado'
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
