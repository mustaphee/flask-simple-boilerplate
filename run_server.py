#!/usr/bin/python
from app.app import create_app, register_extensions
from app.config.config import DevelopmentConfig

# Create an app instance and run
if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    register_extensions(app)
    PORT = int(app.config['PORT'])
    app.run(port=PORT)
