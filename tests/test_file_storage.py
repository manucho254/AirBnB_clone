#!/usr/bin/python3
""" module to test FileStorage class
"""

from models import storage
from models.base_model import BaseModel

import unittest


class TestFileStorage(unittest.TestCase):
    """ Class to test FileStorage
    """

    def setUp(self):
        """ initialize tests
        """
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

    def test_all_method(self):
        """ test getting all objects
        """
        self.assertIsInstance(self.all_objs, dict)

    def test_new_method_valid_data(self):
        """ test adding a new Object
        """
        new_size = self.size
        base_model = BaseModel()
        storage.new(base_model)
        self.all_objs = storage.all()
        self.size = len(self.all_objs)
        self.assertGreater(self.size, new_size)

    def test_new_method_invalid_data(self):
        """ test adding invalid object
        """
        new_size = self.size
        storage.new("test")
        self.all_objs = storage.all()
        self.size = len(self.all_objs)
        self.assertEqual(self.size, new_size)

    def test_save_method(self):
        """ test save method
        """
        new_size = self.size
        base_model = BaseModel()
        base_model.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        """ teardown function
        """
        self.all_objs = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
