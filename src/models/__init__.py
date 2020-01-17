from flask_sqlalchemy import SQLAlchemy


# initialize db
session_options = {'expire_on_commit': False}
db = SQLAlchemy(session_options=session_options)
