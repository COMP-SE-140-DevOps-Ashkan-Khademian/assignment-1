import os

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

load_dotenv()

environment = os.getenv("FLASK_ENV", "development")
api = Api()


def create_app():
    app = Flask(__name__)

    from app.config import Config, ConfigBuilder

    config: Config = (
        ConfigBuilder.set_app(app).set_environment(environment).get_instance()
    )
    config.initialize()

    return app
