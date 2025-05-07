from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from app import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

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

        flash('Usuario creado con éxito', 'success')
        return redirect(url_for('auth.login'))  

    return render_template('usuarios/registrar_usuario.html')

@auth_bp.route('/usuarios')
def listar_usuarios():
    busqueda = request.args.get('busqueda', '')
    if busqueda:
        usuarios = Usuario.query.filter(
            or_(
                Usuario.nombre.ilike(f"%{busqueda}%"),
                Usuario.apellidos.ilike(f"%{busqueda}%"),
                Usuario.correo.ilike(f"%{busqueda}%")
            )
        ).all()
    else:
        usuarios = Usuario.query.all()
    return render_template('usuarios/lista_usuarios.html', usuarios=usuarios)

@auth_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apellidos = request.form['apellidos']
        usuario.correo = request.form['correo']

        if request.form.get('contrasena'):
            usuario.contrasena = generate_password_hash(request.form['contrasena'])

        db.session.commit()
        flash('Usuario actualizado exitosamente')
        return redirect(url_for('auth.listar_usuarios'))

    return render_template('usuarios/editar_usuario.html', usuario=usuario)

@auth_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente')
    return redirect(url_for('auth.listar_usuarios'))