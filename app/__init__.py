from flask import Flask
from flask_migrate import Migrate
from config import DevelopmentConfig
from app.models import db
from app.routers.questions import questions_bp
from app.routers.response import response_bp
from app.routers.categories import categories_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)
    app.register_blueprint(categories_bp)

    return app
