from flask import Flask
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from config import get_config
from datetime import timedelta
from app.models.usuario import Usuario


db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    """Crea una instancia de la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(get_config())  # Cargar la configuración según el entorno

    app.secret_key = 'clave-secreta'
    app.permanent_session_lifetime = timedelta(minutes=5)  # <-- duración de sesión
    login_manager.init_app(app)

    db.init_app(app)
    mail.init_app(app)


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
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
