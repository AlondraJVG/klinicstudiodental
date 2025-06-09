from flask import Blueprint, render_template, jsonify
from app.models.Citas import Cita
from flask_login import login_required

calendario_bp = Blueprint('calendario', __name__, url_prefix='/calendario')

@calendario_bp.route('/')
@login_required
def ver_calendario():
    return render_template('calendario/calendario.html')

@calendario_bp.route('/eventos')
@login_required
def obtener_eventos():
    citas = Cita.query.all()
    eventos = []

    for cita in citas:
        eventos.append({
            'title': f'Cita: {cita.paciente.nombre} {cita.paciente.apellido}',
            'start': cita.fecha_hora.isoformat(),
            'end': cita.fecha_hora.isoformat(),
            'url': f'/citas/editar/{cita.id}'
        })

    return jsonify(eventos)
