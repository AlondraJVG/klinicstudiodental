from datetime import datetime
import pytz

def ahora_gdl():
    zona_horaria_gdl = pytz.timezone('America/Mexico_City')
    return datetime.now(zona_horaria_gdl)
