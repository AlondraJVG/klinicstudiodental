from app.utils.timezone import convertir_a_gdl

# Supongamos que tienes una fecha guardada en la base de datos:
fecha_utc = cita.fecha_hora  # datetime almacenado en MySQL (UTC)

fecha_local = convertir_a_gdl(fecha_utc)
print("Fecha en GDL:", fecha_local)
