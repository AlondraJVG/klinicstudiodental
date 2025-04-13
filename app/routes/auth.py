from flask import request, render_template, redirect, url_for, flash
from app import app, db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

app.config['SECRET_KEY'] = 'tu_clave_secreta'

@app.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('login'))  

    return render_template('login.html')

@app.route('/rUsuario', methods=['GET', 'POST'])
def rUsuario():
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
