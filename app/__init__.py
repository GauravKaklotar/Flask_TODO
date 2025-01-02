from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
