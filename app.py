from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Conexión a MySQL en PythonAnywhere
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@usuario.mysql.pythonanywhere-services.com/usuario$nombre_basedatos'
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
            return redirect(url_for('dashboard'))
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
