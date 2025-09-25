from decouple import config

from flask import Flask
from flask_restful import Api

environment: str = config(
    "FLASK_ENV", "development"
)  # pyright: ignore[reportAssignmentType]

api = Api()


def create_app():
    app = Flask(__name__)

    from app.config import Config, ConfigBuilder

    config: Config = (
        ConfigBuilder.set_app(app).set_environment(environment).get_instance()
    )
    config.initialize()

    return app
