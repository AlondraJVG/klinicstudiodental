# 🦷 KLINIC STUDIO DENTAL

Sistema web desarrollado con Flask para la gestión integral de un consultorio dental. Permite el registro de pacientes, manejo de historial clínico, agenda de citas, tratamientos odontológicos y control de usuarios con autenticación.

    🚨 Este proyecto fue creado por Alondra Janett Vázquez Gutiérrez. Todos los derechos reservados.
    Cualquier reproducción, uso o distribución sin autorización está prohibida. Este trabajo fue registrado como parte del curso de Programación Web impartido por el Profesor LEON MIGUEL RAMOS para el cliente Dr. César Gutiérrez Ríos (Tecnologico de Mario Molina y Pasquel, Unidad Academica Zapopan 2025).

---

## 📚 Tecnologías utilizadas

* Python 3.11
* Flask
* SQLAlchemy
* Jinja2
* HTML y CSS
* PythonAnywhere (producción)
* MySQL (base de datos: `Klinical$default`)

---

## ⚙️ Requisitos del sistema

* Python 3.10 o superior
* pip
* Cuenta en PythonAnywhere (opcional, para despliegue en nube)

---

## 🚀 Características

* Login y registro de usuarios
* CRUD completo: Pacientes, Citas, Tratamientos, Usuario
* Base de datos relacional con SQLAlchemy
* Rutas separadas por Blueprints
* Plantillas HTML con Jinja2
* Estilos personalizados con CSS

---

## ⚡ Instalación rápida

```bash
# Clona el repositorio
$ git clone https://github.com/AlondraJVG/klinicstudiodental.git
$ cd KLINICSTUDIODENTAL

# Crea entorno virtual (opcional pero recomendado)
$ python -m venv venv
$ source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
$ pip install -r requirements.txt

# Ejecuta localmente (si se desea probar)
$ flask run
```

> Para configuración completa del despliegue, consulta `INSTALL.md`

---

## 🔍 Estructura del proyecto

```
KLINICSTUDIODENTAL/
├── app/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── __init__.py
├── config.py
├── .env.example
├── README.md
├── INSTALL.md
├── API.md
├── CHANGELOG.md
└── tests/
```

---

## 📩 Contacto
📧 klinical30@gmail.com
👩‍💻 Autora: Alondra Janett Vázquez Gutiérrez
📘 Tecnologico de Mario Molina y Pasquel, Unidad Academica Zapopan 2025