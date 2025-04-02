from flask import Flask
from flask_login import LoginManager
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.owner import Owner
from models.pet import Pet
from routes.auth_bp import auth_bp
from routes.main_bp import main_bp
from routes.pet_input_bp import pet_input_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = (  # type: ignore
        "auth_bp.login_page"  # Redirects unauthorized users to the login page
    )

    @login_manager.user_loader
    def load_user(user_id):
        return Owner.query.get(int(user_id))  # Maintain tokens for specific user

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1")).fetchall()
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(pet_input_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
