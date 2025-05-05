from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Obtener las credenciales del archivo .env
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Función para enviar el correo
def enviar_correo(destinatario, asunto, cuerpo):
    remitente = EMAIL_USER
    contraseña = EMAIL_PASS

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        # Configuración del servidor SMTP (para Gmail)
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()  # Iniciar conexión segura
        servidor.login(remitente, contraseña)  # Iniciar sesión en el servidor
        servidor.sendmail(remitente, destinatario, mensaje.as_string())  # Enviar correo
        servidor.quit()  # Cerrar la conexión
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    destinatario = "destinatario@example.com"
    asunto = "Cita para mañana"
    cuerpo = "Este es un recordatorio de la cita para mañana."
    enviar_correo(destinatario, asunto, cuerpo)
