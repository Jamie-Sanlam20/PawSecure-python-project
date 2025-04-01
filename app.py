from flask import Flask
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.pet import Pet
from routes.main_bp import main_bp
from routes.pet_input_bp import pet_input_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1")).fetchall()
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(pet_input_bp)
    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
