#!/usr/bin/python3
""" module to test Console.
"""

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand


    def test_Console_prompt(self):
        """Check the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_Console_prompt_empty_line(self):
        """Check empty line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue())

    def test_Console_prompt_new_line(self):
        """Check new line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual("", output.getvalue())

    def test_Console_quit(self):
        """Check quit exists."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_Console_eof(self):
        """Check eof exists."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
