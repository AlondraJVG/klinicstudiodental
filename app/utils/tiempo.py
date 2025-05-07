from datetime import datetime
import pytz

def ahora_gdl():
    tz = pytz.timezone('America/Mexico_City')
    return datetime.now(tz)
