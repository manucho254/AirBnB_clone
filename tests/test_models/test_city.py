#!/usr/bin/python3
""" City class test module
"""

import unittest
from datetime import datetime, timedelta
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ class TestCity
    """
    def setUp(self):
        """ initialize class
        """
        self.city_no_kwargs = City()
        self.city_with_kwargs = None
        self.yesterday = datetime.now() - timedelta(days=1)
        self.city_no_kwargs.updated_at = self.yesterday
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """
        self.assertTrue(hasattr(self.city_no_kwargs, "id"))
        self.assertTrue(hasattr(self.city_no_kwargs, "state_id"))
        self.assertTrue(hasattr(self.city_no_kwargs, "name"))
        self.assertTrue(hasattr(self.city_no_kwargs, "created_at"))
        self.assertTrue(hasattr(self.city_no_kwargs, "updated_at"))

    def test_city_subclass_of_base_model(self):
        """ check if City inherits from BaseModel
        """
        assert issubclass(type(self.city_no_kwargs), (BaseModel,))

    def test_save_city(self):
        """ test save method
        """
        new_size = self.size
        city = City()
        city.updated_at = self.yesterday
        previous_date = city.updated_at
        city.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertNotEqual(previous_date, city.updated_at)
        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def test_create_city_no_kwargs(self):
        """ create City with no **kwargs
        """
        self.city_no_kwargs.updated_at = self.yesterday
        to_dict = self.city_no_kwargs.to_dict()

        self.assertIsInstance(self.city_no_kwargs, City)
        self.assertIsInstance(to_dict, dict)
        self.assertIsNotNone(to_dict.get("__class__"))

    def test_create_city_with_kwargs(self):
        """ create City with **kwargs
        """
        self.city_with_kwargs = City(**self.city_no_kwargs.to_dict())
        self.city_with_kwargs.updated_at = self.yesterday
        to_dict = self.city_with_kwargs.to_dict()

        self.assertIsInstance(self.city_with_kwargs, City)
        self.assertIsInstance(to_dict, dict)
        self.assertIsNotNone(to_dict.get("__class__"))

    def test_id_is_string(self):
        """ check if id attribute contains a string.
        """
        self.assertIsInstance(self.city_no_kwargs.id, str)

    def test_dates_are_datetime_object(self):
        """ check if all dates in BaseModel object are datetime objects
        """
        self.assertIsInstance(self.city_no_kwargs.created_at, datetime)
        self.assertIsInstance(self.city_no_kwargs.updated_at, datetime)

    def test_to_dict_method(self):
        """ tests on to_dict method.
        """
        new_dict = self.city_no_kwargs.to_dict()
        self.assertIsInstance(new_dict, dict)
        # check of all the dates objects have been converted to string format
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertIsNotNone(new_dict["__class__"])
        self.assertIsInstance(new_dict["__class__"], str)

    def test_city_to_string(self):
        """ test if City can be represented as a string
        """
        self.assertIsInstance(str(self.city_no_kwargs), str)

    def tearDown(self):
        """ teardown function """
        self.city_no_kwargs = None
        self.city_with_kwargs = None
        self.yesterday = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
