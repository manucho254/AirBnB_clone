#!/usr/bin/python3
""" State class test module
"""

import unittest

from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ class TestState
    """
    def setUp(self):
        """ initialize class
        """
        self.state = State()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)  # number of items in storage

    def test_all_attributes_are_present(self):
        """ test all attributes are present
        """

        self.assertTrue(hasattr(self.state, "name"))

    def test_state_subclass_of_base_model(self):
        """ check if State inherits from BaseModel
        """
        assert issubclass(type(self.state), (BaseModel,))

    def test_save_state(self):
        """ test save method
        """
        new_size = self.size
        state = State()
        state.save()
        self.all_objs = storage.all()
        self.size = len(self.all_objs)

        self.assertIsInstance(self.all_objs, dict)
        self.assertGreater(self.size, new_size)

    def tearDown(self):
        self.state = None
        self.all_objects = None
        self.size = 0


if __name__ == "__main__":
    unittest.main()
