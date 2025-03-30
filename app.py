from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

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

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(correo=correo).first()
        
        if usuario and check_password_hash(usuario.contrasena, contrasena):
            session['usuario'] = usuario.nombre
            flash('Has iniciado sesión correctamente', 'success')
            return ('la informacion es corresta')
            #return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f'Bienvenido, {session["usuario"]}!'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Generar el hash de la contraseña
        contrasena_hash = generate_password_hash(contrasena, method='pbkdf2:sha256')
        
        # Crear un nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena_hash)
        
        # Guardar el usuario en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))  # Redirigir al login después del registro

    return render_template('register.html')  # Mostrar el formulario de registro
