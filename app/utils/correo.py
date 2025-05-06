import smtplib
from email.mime.text import MIMEText
from config import MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD

def enviar_correo(destinatario, asunto, cuerpo):
    mensaje = MIMEText(cuerpo, "html")
    mensaje["Subject"] = asunto
    mensaje["From"] = MAIL_USERNAME
    mensaje["To"] = destinatario

    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as servidor:
        if MAIL_USE_TLS:
            servidor.starttls()
        servidor.login(MAIL_USERNAME, MAIL_PASSWORD)
        servidor.sendmail(MAIL_USERNAME, destinatario, mensaje.as_string())