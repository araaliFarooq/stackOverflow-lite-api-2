import os
from configparser import ConfigParser


class BaseConfig(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = "sec-def-oscar-zulu-3-zero-niner"


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/tstackoverflow_tests'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/stackoverflow'
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
