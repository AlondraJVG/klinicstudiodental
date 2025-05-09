from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Paciente import Paciente
from app.models.Citas import Cita
from app.models.Tratamiento import Tratamiento
from datetime import datetime, date
from app.utils.correo import enviar_correo
from app.utils.tiempo import ahora_gdl
import pytz

zona_horaria_gdl = pytz.timezone('America/Mexico_City')

cita_bp = Blueprint('citas', __name__, url_prefix='/citas')

# Mostrar todas las citas
@cita_bp.route('/')
def listar_citas():
    busqueda = request.args.get('busqueda', '')
    if busqueda:
        citas = Cita.query.join(Paciente).filter(
            (Paciente.nombre.like(f'%{busqueda}%')) | (Paciente.apellido.like(f'%{busqueda}%'))
        ).all()
    else:
        citas = Cita.query.all()
    return render_template('citas/listar_citas.html', citas=citas)

# Crear nueva cita
@cita_bp.route('/nueva', methods=['GET', 'POST'])
def crear_cita():
    pacientes = Paciente.query.all()
    tratamientos = Tratamiento.query.all()

    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        tratamiento_id = request.form.get('tratamiento_id') or None
        fecha_hora_str = request.form['fecha']  
        motivo = request.form['motivo']
        notas = request.form.get('notas', '')
        estado = request.form['estado']

        # Convertir fecha y hora
        datetime_cita = datetime.strptime(fecha_hora_str, '%Y-%m-%dT%H:%M')
        datetime_cita = zona_horaria_gdl.localize(datetime_cita)

        fecha = datetime_cita.date()
        hora = datetime_cita.time()
        ahora = ahora_gdl()

        # Validación: no puede estar en el pasado
        if datetime_cita < ahora:
            flash('No puedes crear una cita en el pasado.', 'danger')
            return render_template('citas/crear_cita.html', pacientes=pacientes, tratamientos=tratamientos,
                                   current_date=date.today().isoformat(),
                                   current_time=datetime.now().strftime('%H:%M'))

        # Validación: margen de 15 minutos con otras citas
        citas_dia = Cita.query.filter(Cita.fecha_hora == fecha).all()
        for cita in citas_dia:
            cita_datetime = cita.fecha_hora  # Ya es un datetime con zona horaria
            diferencia = abs((datetime_cita - cita_datetime).total_seconds()) / 60
            if diferencia < 15:
                flash('Ya hay una cita en ese rango de hora. Debe haber al menos 15 minutos de separación.', 'danger')
                return render_template('citas/crear_cita.html', pacientes=pacientes, tratamientos=tratamientos,
                                       current_date=date.today().isoformat(),
                                       current_time=datetime.now().strftime('%H:%M'))
            # Validación: no permitir que el mismo paciente tenga más de una cita el mismo día
            cita_existente_paciente = Cita.query.filter(
                Cita.paciente_id == paciente_id,
                db.func.date(Cita.fecha_hora) == fecha
            ).first()

            if cita_existente_paciente:
                flash('Este paciente ya tiene una cita registrada para este día.', 'danger')
                return render_template('citas/crear_cita.html', pacientes=pacientes, tratamientos=tratamientos,
                                    current_date=date.today().isoformat(),
                                    current_time=datetime.now().strftime('%H:%M'))

        # Crear y guardar la cita con el campo 'fecha_hora'
        nueva_cita = Cita(
            paciente_id=paciente_id,
            tratamiento_id=tratamiento_id,
            fecha_hora=datetime_cita,  # Ahora guardamos la cita con la fecha y hora en un solo campo
            motivo=motivo,
            notas=notas,
            estado=estado
        )
        db.session.add(nueva_cita)
        db.session.commit()

        # Obtener datos del paciente
        paciente = Paciente.query.get(paciente_id)

        # Componer y enviar correo
        destinatario = paciente.correo
        asunto = "Confirmación de cita"
        cuerpo = render_template('correos/cuerpo.html',
            nombre=paciente.nombre,
            fecha=datetime_cita.date(),
            hora=datetime_cita.time(),
            motivo=motivo,
            notas=notas or 'N/A',
            telefono='3318583055',  
            correo='klinical30@gmail.com',  
            remitente='Klinic Studio Dental'
        )

        enviar_correo(destinatario, asunto, cuerpo)

        flash('Cita creada exitosamente y correo enviado.', 'success')
        return redirect(url_for('citas.listar_citas'))

    # Si el método es GET, mostrar formulario
    return render_template(
        'citas/crear_cita.html',
        pacientes=pacientes,
        tratamientos=tratamientos,
        current_date=date.today().isoformat(),
        current_time=datetime.now().strftime('%H:%M')
    )

# Editar cita
@cita_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    cita = Cita.query.get_or_404(id)
    pacientes = Paciente.query.all()
    tratamientos = Tratamiento.query.all()

    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        tratamiento_id = request.form.get('tratamiento_id') or None
        fecha_hora_str = request.form['fecha']
        motivo = request.form['motivo']
        notas = request.form.get('notas', '')
        estado = request.form['estado']

        # Convertir fecha y hora
        datetime_cita = datetime.strptime(fecha_hora_str, '%Y-%m-%dT%H:%M')
        datetime_cita = zona_horaria_gdl.localize(datetime_cita)

        fecha = datetime_cita.date()
        hora = datetime_cita.time()

        ahora = ahora_gdl()

        # Validación 1: No en el pasado
        if datetime_cita < ahora:
            flash('No puedes reprogramar una cita a una fecha y hora en el pasado.', 'danger')
            return render_template('citas/editar_cita.html', cita=cita, pacientes=pacientes, tratamientos=tratamientos)

        # Validación 2: No superponerse con otra cita
        citas_dia = Cita.query.filter(Cita.fecha_hora == fecha, Cita.id != cita.id).all()
        for otra in citas_dia:
            otra_datetime = otra.fecha_hora
            diferencia = abs((datetime_cita - otra_datetime).total_seconds()) / 60
            if diferencia < 15:
                flash('Ya existe otra cita en un rango menor a 15 minutos. Cambia la hora.', 'danger')
                return render_template('citas/editar_cita.html', cita=cita, pacientes=pacientes, tratamientos=tratamientos)

        # Guardar cambios
        cita.paciente_id = paciente_id
        cita.tratamiento_id = tratamiento_id
        cita.fecha_hora = datetime_cita  # Actualizar con nueva fecha y hora
        cita.motivo = motivo
        cita.notas = notas
        cita.estado = estado

        db.session.commit()

        flash('Cita actualizada correctamente.', 'success')
        return redirect(url_for('citas.listar_citas'))

    return render_template('citas/editar_cita.html', cita=cita, pacientes=pacientes, tratamientos=tratamientos)

# Eliminar cita
@cita_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_cita(id):
    cita = Cita.query.get_or_404(id)
    paciente = Paciente.query.get(cita.paciente_id)

    # Preparar el correo
    destinatario = paciente.correo
    asunto = "Cita cancelada"
    cuerpo_html = render_template('correos/cancelacion.html',  
        nombre=paciente.nombre,
        fecha=cita.fecha_hora.strftime('%d/%m/%Y'),
        hora=cita.fecha_hora.strftime('%H:%M'),
        motivo=cita.motivo,
        telefono='3318583055',   
        correo='klinical30@gmail.com', 
        remitente="Clínica Dental"
    )

    enviar_correo(destinatario, asunto, cuerpo_html)

    # Eliminar la cita
    db.session.delete(cita)
    db.session.commit()

    flash('Cita eliminada exitosamente y correo enviado.', 'success')
    return redirect(url_for('citas.listar_citas'))
