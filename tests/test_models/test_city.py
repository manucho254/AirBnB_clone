#!/usr/bin/python3
""" City class test module
"""

import unittest

from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ class TestCity
    """
    def setUp(self):
        """ initialize class
        """
        self.city = City()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_city_subclass_of_base_model(self):
        """ check if City inherits from BaseModel
        """
        assert issubclass(type(self.city), (BaseModel,))

    def test_save_city(self):
        """ test save method
        """
        new_size = self.size
        city = City()
        city.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.city = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
