from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from app.utils.config import Config

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register blueprints
    from app.routes.order import orders_bp
    from app.routes.product import products_bp
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(products_bp, url_prefix="/products")

    return app
