#!/usr/bin/python3
"""Defines unittests for console.py."""


import os
import sys
import unittest
from unittest.mock import patch
from models.user import User
import models
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO

class TestUser_instantiation(unittest.TestCase):
    """testing instance of the User class"""

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

if __name__ == "__main__":
    unittest.main()
