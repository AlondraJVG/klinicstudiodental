from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

# Se mantiene el Blueprint
auth_bp = Blueprint('auth', __name__)

# Ruta de login
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            session['usuario_id'] = usuario.id
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('auth.menu'))  
        else:
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# Ruta para el menú principal
@auth_bp.route('/menu')
def menu():
    # Recupera el usuario desde la sesión
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash('Por favor, inicia sesión primero.', 'error')
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get_or_404(usuario_id)
    return render_template('menu.html', paciente=usuario)
