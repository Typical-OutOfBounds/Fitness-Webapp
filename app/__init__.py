import os

from flask import Flask

from app.routes import main_bp 
from app.sheets_service import SheetsService

def create_app():
    app = Flask(__name__)
    config_name = os.getenv("FLASK_CONFIG", "config.DevelopmentConfig")
    app.config.from_object(config_name)

    with app.app_context():
        app.sheets_service = SheetsService(app.config["SPREADSHEET_ID"])

    app.register_blueprint(main_bp)

    return app