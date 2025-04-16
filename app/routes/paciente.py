from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from app import db
from app.models.Paciente import Paciente

paciente_bp = Blueprint('paciente', __name__)

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))


@paciente_bp.route('/pacientes')
def lista_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)

@paciente_bp.route('/pacientes/nuevo', methods=['GET', 'POST'])
def nuevo_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento_str = request.form['fecha_nacimiento']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        edad = calcular_edad(fecha_nacimiento)
        sexo = request.form['sexo']
        datos_contacto = request.form['datos_contacto']
        tipo_sangre = request.form['tipo_sangre']
        contacto_emergencia = request.form['contacto_emergencia']
        correo = request.form['correo']
        telefono = request.form['telefono']

        nuevo = Paciente(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            sexo=sexo,
            datos_contacto=datos_contacto,
            tipo_sangre=tipo_sangre,
            contacto_emergencia=contacto_emergencia,
            correo=correo,
            telefono=telefono
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Paciente creado exitosamente')
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
        paciente.datos_contacto = request.form['datos_contacto']
        paciente.tipo_sangre = request.form['tipo_sangre']
        paciente.contacto_emergencia = request.form['contacto_emergencia']
        paciente.correo = request.form['correo']
        paciente.telefono = request.form['telefono']

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
