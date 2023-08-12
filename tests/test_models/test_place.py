#!/usr/bin/python3
""" Place class test module
"""

import unittest

from models import storage
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ class TestPlace
    """
    def setUp(self):
        """ initialize class
        """
        self.place = Place()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_subclass_of_base_model(self):
        """ check if Place inherits from BaseModel
        """
        assert issubclass(type(self.place), (BaseModel,))

    def test_save_place(self):
        """ test save method
        """
        new_size = self.size
        place = Place()
        place.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.place = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
