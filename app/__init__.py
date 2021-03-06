from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate(db=db)
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
# mail = Mail()
bootstrap = Bootstrap()
# moment = Momnet()
# babel = Babel()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)

    # mail.init_app(app)
    bootstrap.init_app(app)
    # moment.init_app(app)
    # babel.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')# all url in auth will be like http://localhost:5000/auth/...

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app