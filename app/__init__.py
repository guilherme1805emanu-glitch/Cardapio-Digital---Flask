import os

from flask import Flask
from .config import Config
from .extensions import db, login_manager


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mocks'),
        static_url_path='/static'
    )
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .shared import shared_bp
    app.register_blueprint(shared_bp)

    from .home import home_bp
    app.register_blueprint(home_bp)

    from .auth import auth_bp
    from .auth.models import User
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .pizzas import pizzas_bp
    app.register_blueprint(pizzas_bp, url_prefix='/pizzas')

    from .drinks import drinks_bp
    from .promotion import promotion_bp
    from .score import score_bp
    app.register_blueprint(drinks_bp, url_prefix='/drinks')
    app.register_blueprint(promotion_bp, url_prefix='/promotion')
    app.register_blueprint(score_bp, url_prefix='/score')

    from .categories import categories_bp
    app.register_blueprint(categories_bp, url_prefix='/categories')

    from .dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    with app.app_context():
        db.create_all()

    return app
