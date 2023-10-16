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
from models.amenity import Amenity
import models
from datetime import datetime

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


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)


if __name__ == "__main__":
    unittest.main()
