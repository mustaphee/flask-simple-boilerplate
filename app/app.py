from flask import Flask
from app.db.db import db
from .router import routes

def create_app(config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)
    return app


def register_extensions(app):
    db.init_app(app)
    routes(app)

