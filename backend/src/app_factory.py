import logging

from flask import Flask
from flask_cors import CORS

from src.api.texts import texts_bp
from src.db.connection import db, migrate
from src.services import nlp_service


def create_app(config: dict) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(config)

    with app.app_context():
        CORS(app)
        db.init_app(app)
        migrate.init_app(app, db)

        app.register_blueprint(texts_bp)
        logging.info('NLP model initialization ...')
        nlp_service.init()
        logging.info('NLP model initialized')

    @app.route('/ping')
    def ping():
        return 'pong'

    return app
