from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from app import db
from app.models.Paciente import Paciente
from sqlalchemy import or_, and_
from app import login_manager
from flask_login import login_required, current_user  



login_manager.login_view = 'auth.login'
paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes', template_folder='templates')

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))


@paciente_bp.route('/pacientes')
@login_required
def lista_pacientes():
    busqueda = request.args.get('busqueda', '')  
    if busqueda:
        pacientes = Paciente.query.filter(
            (Paciente.nombre.ilike(f"%{busqueda}%")) |
            (Paciente.apellido.ilike(f"%{busqueda}%")) |
            (Paciente.correo.ilike(f"%{busqueda}%"))
        ).all()
    else:
        pacientes = Paciente.query.all()

    return render_template('pacientes.html', pacientes=pacientes)

@paciente_bp.route('/pacientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        correo = request.form['correo'].strip()

        # Convertir a minúsculas para comparar
        nombre_lower = nombre.lower()
        apellido_lower = apellido.lower()
        correo_lower = correo.lower()

        # Buscar si ya existe un paciente con esos datos (ignorando mayúsculas/minúsculas)
        paciente_existente = Paciente.query.filter(
            or_(
                and_(
                    db.func.lower(Paciente.correo) == correo_lower,
                    db.func.lower(Paciente.apellido) == apellido_lower
                ),
                and_(
                    db.func.lower(Paciente.nombre) == nombre_lower,
                    db.func.lower(Paciente.apellido) == apellido_lower
                ),
                and_(
                    db.func.lower(Paciente.correo) == correo_lower,
                    db.func.lower(Paciente.nombre) == nombre_lower
                )
            )
        ).first()

        if paciente_existente:
            flash('Ya existe un paciente con ese nombre, apellido y correo.', 'error')
            return render_template('nuevo_paciente.html', form_data=request.form)

        # Procesar el resto de datos
        fecha_nacimiento_str = request.form['fecha_nacimiento']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        edad = calcular_edad(fecha_nacimiento)
        sexo = request.form['sexo']
        tipo_sangre = request.form['tipo_sangre']
        telefono = request.form['telefono']
        contacto_emergencia = request.form['contacto_emergencia']
        nombre_contacto = request.form['nombre_contacto']

        nuevo = Paciente(
            nombre=nombre_lower,
            apellido=apellido_lower,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            sexo=sexo,
            tipo_sangre=tipo_sangre,
            correo=correo_lower,
            telefono=telefono,
            contacto_emergencia=contacto_emergencia,
            nombre_contacto=nombre_contacto
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Paciente creado exitosamente', 'success')
        return redirect(url_for('paciente.lista_pacientes'))
    
    return render_template('nuevo_paciente.html')

    

@paciente_bp.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.apellido = request.form['apellido']
        fecha_nacimiento_str = request.form['fecha_nacimiento']
        paciente.fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        paciente.edad = calcular_edad(paciente.fecha_nacimiento)
        paciente.sexo = request.form['sexo']
        paciente.tipo_sangre = request.form['tipo_sangre']
        paciente.correo = request.form['correo']
        paciente.telefono = request.form['telefono']
        paciente.contacto_emergencia = request.form['contacto_emergencia']
        paciente.nombre_contacto = request.form['nombre_contacto']

        db.session.commit()
        flash('Paciente actualizado exitosamente')
        return redirect(url_for('paciente.lista_pacientes'))
    
    return render_template('editar_paciente.html', paciente=paciente)

@paciente_bp.route('/pacientes/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado exitosamente')
    return redirect(url_for('paciente.lista_pacientes'))