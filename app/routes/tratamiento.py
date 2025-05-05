from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Tratamiento import Tratamiento

tratamiento_bp = Blueprint('tratamientos', __name__, url_prefix='/tratamientos')

# Listar tratamientos
@tratamiento_bp.route('/')
def listar_tratamientos():
    tratamientos = Tratamiento.query.all()
    return render_template('tratamientos/listar_tratamientos.html', tratamientos=tratamientos)

# Crear nuevo tratamiento
@tratamiento_bp.route('/nuevo', methods=['GET', 'POST'])
def crear_tratamiento():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form.get('descripcion', '')

        nuevo_tratamiento = Tratamiento(nombre=nombre, descripcion=descripcion)
        db.session.add(nuevo_tratamiento)
        db.session.commit()

        flash('Tratamiento creado exitosamente.', 'success')
        return redirect(url_for('tratamientos.listar_tratamientos'))

    return render_template('tratamientos/crear_tratamiento.html')

# Editar tratamiento
@tratamiento_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tratamiento(id):
    tratamiento = Tratamiento.query.get_or_404(id)

    if request.method == 'POST':
        tratamiento.nombre = request.form['nombre']
        tratamiento.descripcion = request.form.get('descripcion', '')
        db.session.commit()

        flash('Tratamiento actualizado correctamente.', 'success')
        return redirect(url_for('tratamientos.listar_tratamientos'))

    return render_template('tratamientos/editar_tratamiento.html', tratamiento=tratamiento)

# Eliminar tratamiento
@tratamiento_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_tratamiento(id):
    tratamiento = Tratamiento.query.get_or_404(id)
    db.session.delete(tratamiento)
    db.session.commit()
    flash('Tratamiento eliminado correctamente.', 'success')
    return redirect(url_for('tratamientos.listar_tratamientos'))
