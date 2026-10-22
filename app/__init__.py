from flask import Flask
from flask_mail import Mail
from config import Config

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)

    from app.routes.main import main_bp
    from app.routes.menu import menu_bp
    from app.routes.registration import registration_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(registration_bp)

    return app
