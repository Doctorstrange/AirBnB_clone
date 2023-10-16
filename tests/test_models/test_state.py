#!/usr/bin/python3
"""Defines unittests for console.py."""


import os
import sys
import unittest
from unittest.mock import patch
from models.state import State
import models
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO


class TestState_instantiation(unittest.TestCase):
    """testing instance of the State class"""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))


if __name__ == "__main__":
    unittest.main()
