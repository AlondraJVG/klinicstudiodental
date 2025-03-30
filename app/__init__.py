from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

def create_app(config_filename='config.py'):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)
    mail.init_app(app)

    # Registrar las rutas
    from .routes import auth, pacientes, citas, tratamientos, reportes
    app.register_blueprint(auth.bp)
    app.register_blueprint(pacientes.bp)
    app.register_blueprint(citas.bp)
    app.register_blueprint(tratamientos.bp)
    app.register_blueprint(reportes.bp)

    return app
