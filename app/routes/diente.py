@diente_bp.route('/dientes')
def lista_dientes():
    dientes = Diente.query.all()
    return render_template('dientes.html', dientes=dientes)