import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')

class ProductionConfig(Config):
    """Production configuration."""
    # SECRET_KEY = os.environ.get('SECRET_KEY')


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True