__author__ = 'ariel'

import os
import unittest

from views import app, db
from models import User
from config import basedir


TEST_DB = 'test.db'

class Users(unittest.TestCase):

    # this is a especial method that is executed prior each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # This is a special metho that is executed after each test
    def tearDown(self):
        db.drop_all()

    # Each test should start with a 'test'
    def test_users_can_register(self):
        new_user = User("aberman", "arielito@gmail.com", "arielberman")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "aberman"

if __name__ == "__main__":
    unittest.main()
