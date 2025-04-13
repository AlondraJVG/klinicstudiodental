from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Paciente import Paciente

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/pacientes')
def lista_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)

@paciente_bp.route('/pacientes/nuevo', methods=['GET', 'POST'])
def nuevo_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        correo = request.form['correo']
        telefono = request.form['telefono']

        nuevo = Paciente(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
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
        paciente.fecha_nacimiento = request.form['fecha_nacimiento']
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
