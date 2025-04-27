from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importar y registrar las rutas
    from app.routes.auth import auth_bp
    from app.routes.paciente import paciente_bp
    from app.routes.odontograma import odontograma_bp
    from app.routes.diente import diente_bp
    from app.routes.condiciones_dentales import condicion_bp
    from app.routes.condiciones_por_diente import condiciones_por_diente_bp
    from app.routes.cita import citas_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(odontograma_bp)
    app.register_blueprint(diente_bp)
    app.register_blueprint(condicion_bp)
    app.register_blueprint(condiciones_por_diente_bp)
    app.register_blueprint(citas_bp)

    return app
