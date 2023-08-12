#!/usr/bin/python3
""" User class test module
"""

import unittest

from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ class TestUser
    """
    def setUp(self):
        """ initialize class
        """
        self.user = User()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_user_subclass_of_base_model(self):
        """ check if User inherits from BaseModel
        """
        assert issubclass(type(self.user), (BaseModel,))

    def test_save_user(self):
        """ test save method
        """
        new_size = self.size
        user = User()
        user.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.user = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
