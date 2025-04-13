from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from app import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash


# Se mantiene el Blueprint
auth_bp = Blueprint('auth', __name__)

auth_bp.config['SECRET_KEY'] = 'mi_clave_secreta_segura'

# Ruta de login
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            return render_template('menu.html')
        else:
            if usuario:
                flash('Contraseña incorrecta', 'error')
            else:
                flash('Correo no encontrado', 'error')
            return redirect(url_for('auth.login')) 

    return render_template('login.html')

# Ruta de registro dentro del Blueprint
@auth_bp.route('/register', methods=['GET', 'POST'])  
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        contrasena_hash = generate_password_hash(contrasena)

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
