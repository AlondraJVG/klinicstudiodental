from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from ..models import Cita
from datetime import timedelta

calendario_bp = Blueprint('calendario', __name__)

@calendario_bp.route('/calendario/')
@login_required
def ver_calendario():
    citas = Cita.query.all()
    eventos = []
    for cita in citas:
        eventos.append({
            'title': f'Cita con {cita.paciente.nombre} {cita.paciente.apellido}',
            'start': cita.fecha_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': (cita.fecha_hora + timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S'),
        })
    return render_template('calendario/calendario.html', eventos=eventos)

@calendario_bp.route('/calendario/eventos')
@login_required
def obtener_eventos():
    citas = Cita.query.all()
    eventos = []

    for cita in citas:
        eventos.append({
            'title': f'Cita con {cita.paciente.nombre} {cita.paciente.apellido}',
            'start': cita.fecha_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': (cita.fecha_hora + timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S'),
            'url': f'/citas/{cita.id}',  
        })

    return jsonify(eventos)