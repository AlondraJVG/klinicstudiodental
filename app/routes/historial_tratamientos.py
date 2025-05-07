from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Paciente import Paciente
from app.models.Historial_Tratamientos import HistorialTratamientos

historial_tratamientos_bp = Blueprint('historial_tratamientos', __name__, url_prefix='/historial')

# Ver historial de tratamientos de un paciente
@historial_tratamientos_bp.route('/<int:paciente_id>')
def ver_historial(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)
    historial = HistorialTratamientos.query.filter_by(paciente_id=paciente_id).all()
    return render_template('historial/ver_historial.html', paciente=paciente, historial=historial)

# Editar un tratamiento del historial
@historial_tratamientos_bp.route('/editar/<int:historial_id>', methods=['GET', 'POST'])
def editar_tratamiento(historial_id):
    historial = HistorialTratamientos.query.get_or_404(historial_id)
    if request.method == 'POST':
        historial.fecha = request.form['fecha']
        historial.observaciones = request.form['observaciones']
        db.session.commit()
        flash('Tratamiento actualizado con éxito.', 'success')
        return redirect(url_for('historial_tratamientos.ver_historial', paciente_id=historial.paciente_id))
    return render_template('historial/editar_tratamiento.html', historial=historial)

# Eliminar un tratamiento
@historial_tratamientos_bp.route('/eliminar/<int:historial_id>', methods=['POST'])
def eliminar_tratamiento(historial_id):
    historial = HistorialTratamientos.query.get_or_404(historial_id)
    paciente_id = historial.paciente_id
    db.session.delete(historial)
    db.session.commit()
    flash('Tratamiento eliminado con éxito.', 'success')
    return redirect(url_for('historial_tratamientos.ver_historial', paciente_id=paciente_id))

@historial_tratamientos_bp.route('/nuevo/<int:paciente_id>', methods=['GET', 'POST'])
def nuevo_tratamiento(paciente_id):
    if request.method == 'POST':
        nuevo = HistorialTratamientos(
            fecha=request.form['fecha'],
            observaciones=request.form['observaciones'],
            paciente_id=paciente_id
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Tratamiento agregado con éxito.', 'success')
        return redirect(url_for('historial_tratamientos.ver_historial', paciente_id=paciente_id))
    return render_template('historial/nuevo_tratamiento.html', paciente_id=paciente_id)

@historial_tratamientos_bp.route('/seleccionar', methods=['GET'])
def seleccionar_paciente():
    pacientes = Paciente.query.all()
    return render_template('historial/seleccionar_paciente.html', pacientes=pacientes)
