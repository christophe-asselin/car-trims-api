from src.app import create_app
from flask_cors import CORS
from src.models import db

if __name__ == "__main__":
    app = create_app()
    CORS(app)
    db.create_all(app=app)
    app.run()
