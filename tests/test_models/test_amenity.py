#!/usr/bin/python3
""" Amenity class test module
"""

import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ class TestAmenity
    """
    def setUp(self):
        """ initialize class
        """
        self.amenity = Amenity()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_available(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_subclass_of_base_model(self):
        """ check if Amenity inherits from BaseModel
        """
        assert issubclass(type(self.amenity), (BaseModel,))

    def test_save_amenity(self):
        """ test save method
        """
        new_size = self.size
        amenity = Amenity()
        amenity.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.amenity = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
