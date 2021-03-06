from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from eventmanager.config import Config

import atexit
from flask_apscheduler import APScheduler

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
scheduler = APScheduler()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    db.app = app
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from eventmanager.users.routes import users
    from eventmanager.events.routes import events
    from eventmanager.main.routes import main
    from eventmanager.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(events)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    scheduler.init_app(app)
    scheduler.start()
    return app
