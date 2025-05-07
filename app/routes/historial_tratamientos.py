from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Paciente import Paciente
from app.models.Citas import Cita
from app.models.Tratamiento import Tratamiento
from app.models.Historial_Tratamientos import HistorialTratamientos

historial_tratamientos_bp = Blueprint('historial_tratamientos', __name__, url_prefix='/historial')

@historial_tratamientos_bp.route('/<int:paciente_id>')
def ver_historial(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)
    historial = HistorialTratamientos.query.filter_by(paciente_id=paciente_id).all()
    return render_template('historial/ver_historial.html', paciente=paciente, historial=historial)

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

@historial_tratamientos_bp.route('/eliminar/<int:historial_id>', methods=['POST'])
def eliminar_tratamiento(historial_id):
    historial = HistorialTratamientos.query.get_or_404(historial_id)
    paciente_id = historial.paciente_id
    db.session.delete(historial)
    db.session.commit()
    flash('Tratamiento eliminado con éxito.', 'success')
    return redirect(url_for('historial_tratamientos.ver_historial', paciente_id=paciente_id))

@historial_tratamientos_bp.route('/pacientes')
def seleccionar_paciente():
    pacientes = Paciente.query.all()
    return render_template('historial/seleccionar_paciente.html', pacientes=pacientes)
