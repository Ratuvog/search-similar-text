import logging

from src.app_factory import create_app

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


config = {
    'SQLALCHEMY_DATABASE_URI': 'postgresql+psycopg2://app:app@localhost:5432/text-search',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}
app = create_app(config)
