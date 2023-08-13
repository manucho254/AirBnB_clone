#!/usr/bin/python3
""" module to test Console.
"""

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ class TestConsole
    """

    def setUp(self):
        """ initialize class
        """
        self.create = "Create User"

    def test_help(self):
        """ test command help
        """

    def test_command_create(self):
        """ test command create
        """

    def test_command_all(self):
        """ test command all
        """
    def test_command_show(self):
        """ test command show
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            print(f.getvalue())

    def test_command_destroy(self):
        """ test command destroy
        """

    def tearDown(self):
        """ Teardown method
        """
        self.create = None


if __name__ == "__main__":
    unittest.main()
