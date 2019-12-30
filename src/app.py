import os
from flask import Flask
from .models import db
from .views.makerview import maker_api


def create_app():

    # Init ap
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Database
    db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(maker_api, url_prefix='/makers')

    return app
