from flask import Flask
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from config import get_config
from datetime import timedelta

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    """Crea una instancia de la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(get_config()) 

    app.secret_key = 'clave-secreta'
    app.permanent_session_lifetime = timedelta(minutes=5)
    login_manager.init_app(app)

    db.init_app(app)
    mail.init_app(app)

    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if not isinstance(s, str):
            return ''
        return Markup(s.replace('\n', '<br>\n'))

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

    from app.models import usuario

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models.usuario import Usuario 
    return Usuario.query.get(int(user_id)