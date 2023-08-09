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
        self.model = BaseModel()

    def test_all_method(self):
        """ test getting all objects
        """
        self.assertIsInstance(self.all_objs)


if __name__ == "__main__":
    unittest.main()
