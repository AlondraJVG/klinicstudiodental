from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Citas import Cita
from app.models.Paciente import Paciente
from app.models.Tratamiento import Tratamiento
from datetime import datetime

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

# Mostrar todas las citas
@citas_bp.route('/')
def listar_citas():
    busqueda = request.args.get('busqueda', '')
    if busqueda:
        citas = Cita.query.join(Paciente).filter(
            (Paciente.nombre.like(f'%{busqueda}%')) | (Paciente.apellido.like(f'%{busqueda}%'))
        ).all()
    else:
        citas = Cita.query.all()
    return render_template('listar_citas.html', citas=citas)

# Crear nueva cita
@citas_bp.route('/nueva', methods=['GET', 'POST'])
def crear_cita():
    pacientes = Paciente.query.all()
    tratamientos = Tratamiento.query.all()

    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        tratamiento_id = request.form.get('tratamiento_id') or None
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        notas = request.form.get('notas', '')
        estado = request.form['estado']

        nueva_cita = Cita(
            paciente_id=paciente_id,
            tratamiento_id=tratamiento_id,
            fecha=datetime.strptime(fecha, '%Y-%m-%d').date(),
            hora=datetime.strptime(hora, '%H:%M').time(),
            motivo=motivo,
            notas=notas,
            estado=estado
        )

        db.session.add(nueva_cita)
        db.session.commit()

        flash('Cita creada exitosamente.', 'success')
        return redirect(url_for('citas.listar_citas'))

    return render_template('crear_cita.html', pacientes=pacientes, tratamientos=tratamientos)

# Editar cita
@citas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    cita = Cita.query.get_or_404(id)
    pacientes = Paciente.query.all()
    tratamientos = Tratamiento.query.all()

    if request.method == 'POST':
        cita.paciente_id = request.form['paciente_id']
        cita.tratamiento_id = request.form.get('tratamiento_id') or None
        cita.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        cita.hora = datetime.strptime(request.form['hora'], '%H:%M').time()
        cita.motivo = request.form['motivo']
        cita.notas = request.form.get('notas', '')
        cita.estado = request.form['estado']

        db.session.commit()
        flash('Cita actualizada correctamente.', 'success')
        return redirect(url_for('citas.listar_citas'))

    return render_template('editar_cita.html', cita=cita, pacientes=pacientes, tratamientos=tratamientos)

# Eliminar cita
@citas_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_cita(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    flash('Cita eliminada exitosamente.', 'success')
    return redirect(url_for('citas.listar_citas'))
