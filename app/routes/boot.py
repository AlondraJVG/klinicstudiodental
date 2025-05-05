# boot.py
from app import create_app, db
from app.models.Citas import Cita
from app.models.Paciente import Paciente
from app.models.Tratamiento import Tratamiento
from datetime import datetime, timedelta
import requests

# Tu token de bot de Telegram y tu ID de chat
TOKEN = '7583213357:AAEgmoGtBcKFQdw8J7Q3pG8f4h17GoQiu2k'
CHAT_ID = '5256594645'

def enviar_mensaje_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)
    
def revisar_citas():
    app = create_app()
    with app.app_context():
        mañana = datetime.now().date() + timedelta(days=1)
        citas = Cita.query.filter_by(fecha=mañana).all()

        for cita in citas:
            paciente = Paciente.query.get(cita.paciente_id)
            tratamiento = Tratamiento.query.get(cita.tratamiento_id)

            mensaje = f"""
📅 <b>Cita para mañana</b>
👤 Paciente: {paciente.nombre} {paciente.apellido}
📧 Correo: {paciente.correo}
🦷 Tratamiento: {tratamiento.nombre if tratamiento else "N/A"}
🕐 Hora: {cita.hora.strftime('%H:%M')}
📝 Motivo: {cita.motivo}
"""
            enviar_mensaje_telegram(mensaje)

if __name__ == '__main__':
    revisar_citas()
