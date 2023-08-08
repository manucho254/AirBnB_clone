#!/usr/bin/python3
""" class TEST_BASE_MODEL module
"""

from models.base_model import BaseModel

import unittest
from datetime import datetime, timedelta


class TestBaseModelNoKwargs(unittest.TestCase):
    """ Class to test BaseModel with no **kwargs
    """
    def setUp(self):
        """ initialize class
        """
        self.base_no_kwargs = BaseModel()
        self.yesterday = datetime.now() - timedelta(days=1)
        self.base_no_kwargs.updated_at = self.yesterday
        #  pass key word argument to BaseModel

    def test_all_default_attributes_exist(self):
        """ check if all BaseModel attributes are present..
        """
        self.assertIsNotNone(self.base_no_kwargs.id)
        self.assertIsNotNone(self.base_no_kwargs.created_at)
        self.assertIsNotNone(self.base_no_kwargs.updated_at)

    def test_id_is_string(self):
        """ check if id attribute contains a string.
        """
        self.assertIsInstance(self.base_no_kwargs.id, str)

    def test_dates_are_datetime_object(self):
        """ check if all dates in BaseModel object are datetime objects
        """
        self.assertIsInstance(self.base_no_kwargs.created_at, datetime)
        self.assertIsInstance(self.base_no_kwargs.updated_at, datetime)

    def test_save_method(self):
        """ test save method in BaseModel
        """
        previous_date = self.base_no_kwargs.updated_at
        self.base_no_kwargs.save()

        self.assertNotEqual(previous_date, self.base_no_kwargs.updated_at)

    def test_to_dict_method(self):
        """ tests on to_dict method.
        """
        new_dict = self.base_no_kwargs.to_dict()
        self.assertIsInstance(new_dict, dict)
        # check of all the dates objects have been converted to string format
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertIsNotNone(new_dict["__class__"])
        self.assertIsInstance(new_dict["__class__"], str)


class TestBaseModelWithKwargs(unittest.TestCase):
    """ Class to test BaseModel with **kwargs
    """

    def setUp(self):
        """ Initialize class
        """
        self.tmp = BaseModel()
        self.base_with_kwargs = BaseModel(**self.tmp.to_dict())

    def test_all_default_attributes_exist(self):
        """ check if all dates in BaseModel object are datetime objects.
        """
        self.assertIsNotNone(self.base_with_kwargs.id)
        self.assertIsNotNone(self.base_with_kwargs.created_at)
        self.assertIsNotNone(self.base_with_kwargs.updated_at)

    def test_to_dict_method(self):
        """ tests on to_dict method.
        """

        """ we call method to_dict below to confirm that attribute __class__
        """
        new_dict = self.base_with_kwargs.to_dict()
        self.assertIsNotNone(new_dict.get("__class__"))

    def test_empty_dict_passed_in_kwargs(self):
        """ check for empty dict passed as Kwargs
        """
        tmp = {}
        self.base_with_kwargs = BaseModel(**tmp)
        """
          we call method to_dict below to confirm that attribute __class__ ,
          is in response..
        """
        new_dict = self.base_with_kwargs.to_dict()
        self.assertIsNotNone(new_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
