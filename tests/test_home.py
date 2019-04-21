import unittest

from app.app import create_app, register_extensions
from app.db import db
from app.config.config import TestingConfig


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        db.db.init_app(self.app)
        register_extensions(self.app)
        self.client = self.app.test_client
        with self.app.app_context():
            # create all tables
            db.db.create_all()

    def test_home(self):
        rv = self.client().get('/')
        self.assertEqual(rv.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.db.session.remove()
            db.db.drop_all()



if __name__ == '__main__':
    unittest.main()