from abc import ABC

from decouple import config
from flask import Flask


class Config(ABC):
    ENV: str
    DEBUG: bool
    TESTING: bool
    FILE_DB_PATH: str = config("FILE_DB_PATH")  # pyright: ignore[reportAssignmentType]

    def __init__(self, app: Flask):
        self.app = app

    def initialize(self):
        self.app.config.from_object(self)
        self._initialize_api()

    def _initialize_api(self):
        from app import api
        from app.resources import url_mapping

        for resource, url in url_mapping:
            api.add_resource(resource, url)

        api.init_app(self.app)


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    ENV = "testing"
    DEBUG = True
    TESTING = True
