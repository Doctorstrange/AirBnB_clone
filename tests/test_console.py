#!/usr/bin/python3
"""Defines unittests for console.py."""


import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_create(self):
        ask = ("Usage: create <class>\n        "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(ask, output.getvalue().strip())

    def test_EOF(self):
        ask = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(ask, output.getvalue().strip())

    def test_quit(self):
        ask = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(ask, output.getvalue().strip())

    class TestHBNBCommand_create(unittest.TestCase):
    """test create command"""

    def test_create_missing_class(self):
        ex = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(ex, output.getvalue().strip())

    def test_create_invalid_class(self):
        ex = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(ex, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        ex = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(ex, output.getvalue().strip())
        ex = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(ex, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
