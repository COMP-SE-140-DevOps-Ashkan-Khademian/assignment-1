from typing import Dict, Optional, Type
from flask import Flask

from .configs import (
    Config,
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig,
)

class ConfigBuilder:
    __instance: Optional["Config"] = None
    __app: Optional["Flask"] = None
    __environment: Optional["str"] = None

    __environment_to_config: Dict[str, Type[Config]] = {
        DevelopmentConfig.ENV: DevelopmentConfig,
        ProductionConfig.ENV: ProductionConfig,
        TestingConfig.ENV: TestingConfig,
    }

    def __new__(cls, *args, **kwargs):
        raise ValueError("Cannot instantiate ConfigBuilder")

    @classmethod
    def set_app(cls, app: "Flask"):
        cls.__app = app
        return cls

    @classmethod
    def set_environment(cls, environment: str):
        cls.__environment = environment
        return cls

    @classmethod
    def get_instance(cls) -> "Config":
        assert cls.__app is not None, "app must be set before getting instance"
        assert (
            cls.__environment is not None
        ), "environment must be set before getting instance"

        if not cls.__instance:
            config_class = cls.__environment_to_config.get(cls.__environment)
            assert config_class is not None, f"Invalid environment: {cls.__environment}"
            cls.__instance = config_class(cls.__app)
        return cls.__instance
