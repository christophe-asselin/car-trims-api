import os
from flask import Flask
from .models import db
from .views.makerview import maker_api
from .views.modelview import model_api
from .views.trimview import trim_api
from .views.equipmentview import equipment_api


def create_app():

    # Init app
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Database
    db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Add views
    app.register_blueprint(maker_api, url_prefix='/makers')
    app.register_blueprint(model_api, url_prefix='/models')
    app.register_blueprint(trim_api, url_prefix='/trims')
    app.register_blueprint(equipment_api, url_prefix='/equipment')
    return app
