#!/usr/bin/python3
"""Defines the HBnB console."""


import unittest
from time import sleep
from datetime import datetime
import os
import models
from models import storage
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestBaseModel_save(unittest.TestCase):
    """to the test the save funtion of the basemodel"""

    def test_a_save(self):
        instance = BaseModel()
        sleep(0.1)
        before_save_time = instance.updated_at
        instance.save()
        self.assertLess(before_save_time, instance.updated_at)

    def test_second_save(self):
        instance = BaseModel()
        sleep(0.1)
        one_save_time = instance.updated_at
        instance.save()
        two_save_time = instance.updated_at
        instance.save()
        three_save_time = instance.updated_at
        self.assertLess(one_save_time, two_save_time)
        self.assertLess(two_save_time, three_save_time)

    def test_saveclass_id(self):
        instance = BaseModel()
        instance.save()
        class_id = "BaseModel." + instance.id
        with open("file.json", "r") as file:
            self.assertIn(class_id, file.read())


if __name__ == "__main__":
    unittest.main()
