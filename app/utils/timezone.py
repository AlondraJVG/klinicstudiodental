import pytz

def convertir_a_gdl(fecha_utc):
    if fecha_utc.tzinfo is None:
        fecha_utc = pytz.utc.localize(fecha_utc)
    zona_gdl = pytz.timezone('America/Mexico_City')
    return fecha_utc.astimezone(zona_gdl)
