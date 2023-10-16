#!/usr/bin/python3
"""Defines unittests for console.py."""


import os
import sys
import unittest
from unittest.mock import patch
from models.place import Place
import models
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import


class TestPlace_instantiation(unittest.TestCase):
    """testing instance of the Place"""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
