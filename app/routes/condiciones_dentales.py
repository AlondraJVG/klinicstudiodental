from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.CondicionesDentales import CondicionesDentales

condicion_bp = Blueprint('condicion', __name__, template_folder='templates')

@condicion_bp.route('/condiciones')
def lista_condiciones():
    condiciones = CondicionesDentales.query.all()
    return render_template('condiciones/lista.html', condiciones=condiciones)

@condicion_bp.route('/condiciones/nueva', methods=['GET', 'POST'])
def nueva_condicion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        nueva = CondicionesDentales(nombre=nombre, descripcion=descripcion)
        db.session.add(nueva)
        db.session.commit()
        flash('Condición dental agregada exitosamente.')
        return redirect(url_for('condicion.lista_condiciones'))
    return render_template('condiciones/nueva.html')
