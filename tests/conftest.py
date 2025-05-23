import os
import pytest
from app import create_app, db

@pytest.fixture
def app():
    # Establecer el entorno de prueba
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
