from flask import Flask, Markup
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 
from config import Config

db = SQLAlchemy()
mail = Mail()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)  #

    # Filtro personalizado para saltos de línea
    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if not isinstance(s, str):
            return ''
        return Markup(s.replace('\n', '<br>\n'))

    # Importar y registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.paciente import paciente_bp
    from app.routes.cita import cita_bp
    from app.routes.tratamiento import tratamiento_bp
    from app.routes.historial_tratamientos import historial_tratamientos_bp



    app.register_blueprint(auth_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(cita_bp)
    app.register_blueprint(tratamiento_bp)
    app.register_blueprint(historial_tratamientos_bp)


    return app
