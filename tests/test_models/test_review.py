#!/usr/bin/python3
""" Review class test module
"""

import unittest

from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ class TestReview
    """
    def setUp(self):
        """ initialize class
        """
        self.review = Review()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_subclass_of_base_model(self):
        """ check if Review inherits from BaseModel
        """
        assert issubclass(type(self.review), (BaseModel,))

    def test_save_review(self):
        """ test save method
        """
        new_size = self.size
        review = Review()
        review.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.review = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
