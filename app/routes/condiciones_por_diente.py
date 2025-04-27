from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.condiciones_por_diente import CondicionesPorDiente
from app.models.Diente import Diente
from app.models.CondicionesDentales import CondicionesDentales

condiciones_por_diente_bp = Blueprint('condiciones_por_diente', __name__, template_folder='templates')

@condiciones_por_diente_bp.route('/condiciones_por_diente')
def lista_condiciones_por_diente():
    condiciones_dientes = CondicionesPorDiente.query.all()
    return render_template('condiciones_por_diente/lista.html', condiciones_dientes=condiciones_dientes)

@condiciones_por_diente_bp.route('/condiciones_por_diente/nuevo', methods=['GET', 'POST'])
def nueva_condicion_por_diente():
    dientes = Diente.query.all()
    condiciones = CondicionesDentales.query.all()

    if request.method == 'POST':
        diente_id = request.form['diente_id']
        condicion_id = request.form['condicion_id']
        descripcion = request.form['descripcion']
        
        nueva_condicion_por_diente = CondicionesPorDiente(
            diente_id=diente_id, 
            condicion_id=condicion_id, 
            descripcion=descripcion
        )
        db.session.add(nueva_condicion_por_diente)
        db.session.commit()
        flash('Condición por diente agregada exitosamente.')
        return redirect(url_for('condiciones_por_diente.lista_condiciones_por_diente'))

    return render_template('condiciones_por_diente/nueva.html', dientes=dientes, condiciones=condiciones)
