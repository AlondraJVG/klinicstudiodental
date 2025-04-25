from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Diente import Diente

diente_bp = Blueprint('diente', __name__, template_folder='templates')

@diente_bp.route('/dientes')
def lista_dientes():
    dientes = Diente.query.all()
    return render_template('dientes/lista.html', dientes=dientes)

@diente_bp.route('/dientes/nuevo', methods=['GET', 'POST'])
def nuevo_diente():
    if request.method == 'POST':
        numero_diente = request.form['numero_diente']
        ubicacion = request.form['ubicacion']
        tipo = request.form['tipo']
        nuevo = Diente(numero_diente=numero_diente, ubicacion=ubicacion, tipo=tipo)
        db.session.add(nuevo)
        db.session.commit()
        flash('Diente agregado exitosamente.')
        return redirect(url_for('diente.lista_dientes'))
    return render_template('dientes/nuevo.html')
