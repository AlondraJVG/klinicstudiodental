from flask_mail import Message
from flask import current_app
from app import mail

def enviar_correo(destinatario, asunto, cuerpo):
    msg = Message(
        subject=asunto,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[destinatario],
        body=cuerpo
    )

    try:
        mail.send(msg)
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")
