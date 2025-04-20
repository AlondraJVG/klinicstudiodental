from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from sqlalchemy import and_
from app import db
from app.models.Paciente import Paciente

paciente_bp = Blueprint('paciente', __name__, template_folder='templates')

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))


@paciente_bp.route('/pacientes')
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
def nuevo_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip().lower()
        apellido = request.form['apellido'].strip().lower()
        fecha_nacimiento_str = request.form['fecha_nacimiento']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        edad = calcular_edad(fecha_nacimiento)
        sexo = request.form['sexo']
        tipo_sangre = request.form['tipo_sangre']
        correo = request.form['correo'].strip().lower()
        telefono = request.form['telefono']
        contacto_emergencia = request.form['contacto_emergencia']
        nombre_contacto = request.form['nombre_contacto']

        paciente_existente = Paciente.query.filter_by(
            nombre=nombre,
            apellido=apellido,
            correo=correo
        ).first()

        if paciente_existente:
            flash('Ya existe un paciente con ese nombre, apellido y correo.', 'warning')
            return redirect(url_for('paciente.nuevo_paciente'))

        nuevo = Paciente(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            sexo=sexo,
            tipo_sangre=tipo_sangre,
            correo=correo,
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
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado exitosamente')
    return redirect(url_for('paciente.lista_pacientes'))
