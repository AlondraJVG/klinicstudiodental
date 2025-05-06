import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from config import Config  # Importa la clase Config

def enviar_correo(destinatario, asunto, cuerpo):
    
    # Accede a las variables a través de Config
    MAIL_SERVER = Config.MAIL_SERVER
    MAIL_PORT = Config.MAIL_PORT
    MAIL_USE_TLS = Config.MAIL_USE_TLS
    MAIL_USERNAME = Config.MAIL_USERNAME
    MAIL_PASSWORD = Config.MAIL_PASSWORD

    mensaje = MIMEText(cuerpo, "html", "utf-8")
    mensaje["Subject"] = Header(asunto, "utf-8")
    mensaje["From"] = formataddr((str(Header("Klinic Studio Dental", "utf-8")), MAIL_USERNAME))
    mensaje["To"] = destinatario
    with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as servidor:
        if MAIL_USE_TLS:
            servidor.starttls()
        servidor.login(MAIL_USERNAME, MAIL_PASSWORD)
        servidor.sendmail(MAIL_USERNAME, destinatario, mensaje.as_bytes())
