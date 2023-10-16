#!/usr/bin/python3
"""Defines unittests for console.py."""


import os
import sys
import unittest
from unittest.mock import patch
from models.city import City
import models
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO


class TestCity_instantiation(unittest.TestCase):
    """testing instance of the City."""

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        place = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(place))
        self.assertNotIn("state_id", place.__dict__)

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))


if __name__ == "__main__":
    unittest.main()
