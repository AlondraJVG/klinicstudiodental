from datetime import datetime
import pytz

def ahora_gdl():
    zona = pytz.timezone('America/Mexico_City')
    return datetime.now(zona)