from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from ..models.usuario import Usuario
from .. import db

bp = Blueprint('auth', __name__)

@bp.route('/', methods=['GET', 'POST'])
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

@bp.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f'Bienvenido, {session["usuario"]}!'
    else:
        return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))
