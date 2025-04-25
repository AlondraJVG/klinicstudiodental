from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from app.models.Odontograma import Odontograma
from app.models.Paciente import Paciente
from app.models.Diente import Diente
from app.models.CondicionesDentales import CondicionesDentales
from app.models.CondicionesPorDiente import CondicionesPorDiente

odontograma_bp = Blueprint('odontograma', __name__, template_folder='templates')

@odontograma_bp.route('/odontograma/seleccionar', methods=['GET'])
def seleccionar_paciente():
    pacientes = Paciente.query.all()
    return render_template('seleccionar_paciente.html', pacientes=pacientes)


@odontograma_bp.route('/odontograma/crear/<int:paciente_id>', methods=['GET', 'POST'])
def crear_odontograma(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)

    if request.method == 'POST':
        nuevo_odontograma = Odontograma(
            paciente_id=paciente.id,
            fecha_creacion=datetime.now().date()
        )
        db.session.add(nuevo_odontograma)
        db.session.commit()
        flash('Odontograma creado exitosamente.', 'success')
        return redirect(url_for('odontograma.ver_odontograma', paciente_id=paciente.id))
    
    return render_template('odontograma/crear_odontograma.html', paciente=paciente)

@odontograma_bp.route('/odontograma/<int:paciente_id>')
def ver_odontograma(paciente_id):
    paciente = Paciente.query.get_or_404(paciente_id)
    odontograma = Odontograma.query.filter_by(paciente_id=paciente_id).first()
    
    if not odontograma:
        flash("El paciente no tiene un odontograma. Crea uno primero.", "warning")
        return redirect(url_for('odontograma.crear_odontograma', paciente_id=paciente_id))

    dientes = Diente.query.all()
    condiciones = CondicionesDentales.query.all()


    condiciones_dientes = CondicionesPorDiente.query.filter_by(odontograma_id=odontograma.id).all()

    return render_template('ver_odontograma.html',
                           paciente=paciente,
                           odontograma=odontograma,
                           dientes=dientes,
                           condiciones=condiciones,
                           condiciones_dientes=condiciones_dientes)

@odontograma_bp.route('/odontograma/asignar_condicion', methods=['POST'])
def asignar_condicion():
    odontograma_id = request.form['odontograma_id']
    diente_id = request.form['diente_id']
    condicion_id = request.form['condicion_id']
    comentarios = request.form.get('comentarios', '')
    fecha = datetime.now().date()

    nueva_condicion = CondicionesPorDiente(
        odontograma_id=odontograma_id,
        diente_id=diente_id,
        condicion_id=condicion_id,
        fecha_diagnostico=fecha,
        comentarios=comentarios
    )

    db.session.add(nueva_condicion)
    db.session.commit()

    odontograma = Odontograma.query.get(odontograma_id)
    flash('Condición asignada exitosamente.', 'success')
    return redirect(url_for('odontograma.ver_odontograma', paciente_id=odontograma.paciente_id))
