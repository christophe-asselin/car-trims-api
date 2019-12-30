from src.app import create_app
# from src.models import db

if __name__ == "__main__":
    app = create_app()
    # db.create_all(app=app)
    app.run(debug=True)
