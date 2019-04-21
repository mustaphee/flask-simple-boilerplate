from app.app import create_app, register_extensions
from app.config.config import StagingConfig

if __name__ == '__main__':
    app = create_app(StagingConfig)
    register_extensions(app)
