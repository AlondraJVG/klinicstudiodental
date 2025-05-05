from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Paciente import Paciente
from app.models.Citas import Cita
from app.models.Tratamiento import Tratamiento 
from datetime import datetime, date
import yagmail

cita_bp = Blueprint('citas', __name__, url_prefix='/citas')

# Función para enviar un correo usando Gmail
def send_email(subject: str, body: str, destinatario: str):
    yag = yagmail.SMTP(user="tu_correo@gmail.com", password="tu_contraseña")
    yag.send(to=destinatario, subject=subject, contents=body)

# Función para crear una cita y enviar un correo
def crear_cita_db(paciente_id: int, tratamiento_id: int, fecha: str, hora: str, motivo: str, notas: str, estado: str, correo_paciente: str):
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    hora_obj = datetime.strptime(hora, '%H:%M').time()
    
    # Verifica que la cita no sea en el pasado
    if datetime.combine(fecha_obj, hora_obj) < datetime.now():
        return None  # Error, no puedes crear una cita en el pasado

    nueva_cita = Cita(
        paciente_id=paciente_id,
        tratamiento_id=tratamiento_id,
        fecha=fecha_obj,
        hora=hora_obj,
        motivo=motivo,
        notas=notas,
        estado=estado
    )

    db.session.add(nueva_cita)
    db.session.commit()

    # Enviar el correo de confirmación
    subject = f"Confirmación de cita para {correo_paciente}"
    body = f"Hola {correo_paciente},\n\nTu cita está confirmada para el {fecha} a las {hora}.\n\nSaludos,\nTu clínica dental."
    send_email(subject, body, correo_paciente)

    return nueva_cita  # Devuelve la cita creada

# Ruta para crear una nueva cita
@cita_bp.route('/nueva', methods=['GET', 'POST'])
def crear_cita():
    pacientes = Paciente.query.all()
    tratamientos = Tratamiento.query.all()

    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        tratamiento_id = request.form.get('tratamiento_id') or None
        fecha_str = request.form['fecha']
        hora_str = request.form['hora']
        motivo = request.form['motivo']
        notas = request.form.get('notas', '')
        estado = request.form['estado']
        correo_paciente = request.form['correo']

        # Validaciones: verifica si la cita ya existe en ese horario
        citas_dia = Cita.query.filter_by(fecha=fecha_str).all()
        for cita in citas_dia:
            cita_datetime = datetime.combine(cita.fecha, cita.hora)
            diferencia = abs((datetime.combine(fecha_str, hora_str) - cita_datetime).total_seconds()) / 60

            if diferencia < 15:
                flash('Ya hay una cita en ese rango de hora. Debe haber al menos 15 minutos de separación.', 'danger')
                return render_template('citas/crear_cita.html', pacientes=pacientes, tratamientos=tratamientos)

        # Crear la cita y enviar correo
        nueva_cita = crear_cita_db(paciente_id, tratamiento_id, fecha_str, hora_str, motivo, notas, estado, correo_paciente)

        if nueva_cita:
            flash('Cita creada exitosamente y correo de confirmación enviado.', 'success')
        else:
            flash('No se pudo crear la cita, la fecha y hora son inválidas.', 'danger')

        return redirect(url_for('citas.listar_citas'))

    return render_template('citas/crear_cita.html', pacientes=pacientes, tratamientos=tratamientos)

# Comando /crear_cita para el bot de Telegram
def crear_cita_telegram(update, context):
    if len(context.args) < 5:
        update.message.reply_text("Por favor, proporciona los detalles completos: paciente_id, tratamiento_id, fecha, hora, correo.")
        return

    paciente_id = context.args[0]
    tratamiento_id = context.args[1]
    fecha = context.args[2]
    hora = context.args[3]
    correo_paciente = context.args[4]

    # Crear la cita y enviar correo
    nueva_cita = crear_cita_db(paciente_id, tratamiento_id, fecha, hora, "", "", "Pendiente", correo_paciente)

    if nueva_cita:
        update.message.reply_text(f"Cita creada con éxito para {correo_paciente} el {fecha} a las {hora}. Correo de confirmación enviado.")
    else:
        update.message.reply_text(f"No se pudo crear la cita para {correo_paciente}. La fecha y hora son inválidas.")

def main():
    updater = Updater("TU_TOKEN_DE_API_AQUI")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("crear_cita", crear_cita_telegram))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
